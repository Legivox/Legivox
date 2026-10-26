#!/usr/bin/env python3
"""Discover useful technology across developer, AI, commerce and indie-business categories.

This is a research-only pipeline. It never drafts, publishes, likes, follows, or replies on X.
All candidates remain unverified until a human checks the original product/project page.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import math
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "data" / "discovery_sources.json"
DEFAULT_OUTPUT_DIR = ROOT / "output" / "discovery"
IST = ZoneInfo("Asia/Kolkata")
USER_AGENT = "LegivoxDiscovery/1.0 (+https://github.com/Legivox/Legivox)"
MAX_DESCRIPTION = 1200
GITHUB_SEARCH_MIN_INTERVAL_SECONDS = 6.5
_GITHUB_SEARCH_LOCK = threading.Lock()
_GITHUB_SEARCH_NEXT_AT = 0.0


def github_search_json(url: str, headers: dict, timeout: int = 15) -> dict:
    """Rate-limit concurrent repository queries and retry once on likely throttling."""
    global _GITHUB_SEARCH_NEXT_AT

    for attempt in range(2):
        with _GITHUB_SEARCH_LOCK:
            wait_seconds = max(0.0, _GITHUB_SEARCH_NEXT_AT - time.monotonic())
            if wait_seconds:
                time.sleep(wait_seconds)
            _GITHUB_SEARCH_NEXT_AT = time.monotonic() + GITHUB_SEARCH_MIN_INTERVAL_SECONDS

        try:
            return json.loads(fetch_bytes(url, headers=headers, timeout=timeout).decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if attempt > 0 or exc.code not in (403, 429):
                raise
            retry_after = exc.headers.get("Retry-After") if exc.headers else None
            remaining = exc.headers.get("X-RateLimit-Remaining") if exc.headers else None
            reset_at = exc.headers.get("X-RateLimit-Reset") if exc.headers else None
            delay = 8.0
            if retry_after:
                try:
                    delay = max(delay, float(retry_after))
                except ValueError:
                    pass
            elif remaining == "0" and reset_at:
                try:
                    delay = max(delay, float(reset_at) - time.time() + 1.0)
                except ValueError:
                    pass
            # Do not burn an entire workflow job waiting on a long rate-limit reset.
            time.sleep(min(30.0, max(1.0, delay)))

    raise RuntimeError("GitHub Search failed after one throttling retry")


def clean_text(value: object) -> str:
    """Decode HTML and collapse whitespace for readable, comparable text."""
    text = html.unescape(str(value or ""))
    text = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return " ".join(text.split()).strip()


def parse_datetime(value: object) -> datetime | None:
    """Parse common RSS, Atom, ISO-8601 and GitHub timestamps to UTC."""
    raw = str(value or "").strip()
    if not raw:
        return None
    try:
        parsed = parsedate_to_datetime(raw)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except (TypeError, ValueError, OverflowError):
        pass
    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except (TypeError, ValueError, OverflowError):
        return None


def iso_utc(value: datetime | None) -> str | None:
    if value is None:
        return None
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc).isoformat(timespec="seconds")


def canonicalize_url(value: object) -> str:
    """Remove tracking query parameters so the same item is merged across sources."""
    raw = str(value or "").strip()
    if not raw:
        return ""
    try:
        parts = urllib.parse.urlsplit(raw)
        query = [
            (key, val) for key, val in urllib.parse.parse_qsl(parts.query, keep_blank_values=True)
            if not key.lower().startswith("utm_")
            and key.lower() not in {"ref", "referrer", "source", "campaign", "fbclid", "gclid"}
        ]
        path = parts.path.rstrip("/") or "/"
        return urllib.parse.urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, urllib.parse.urlencode(query), ""))
    except ValueError:
        return raw


def load_config() -> dict:
    try:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError("Could not load data/discovery_sources.json: " + type(exc).__name__) from exc
    for key in ("feeds", "github_searches", "hn_searches", "wordpress_searches", "categories", "source_weights"):
        if key not in config:
            raise RuntimeError("Discovery source registry is missing key: " + key)
    return config


def category_matches(text: object, config: dict, category_hint: str | None = None) -> list[str]:
    """Return the strongest category matches; this is routing, not a quality verdict."""
    folded = clean_text(text).casefold()
    scores: dict[str, int] = {}
    for category, spec in config.get("categories", {}).items():
        matched = sum(1 for keyword in spec.get("keywords", []) if str(keyword).casefold() in folded)
        if matched:
            scores[category] = matched
    ordered = sorted(scores, key=lambda key: (-scores[key], key))
    if category_hint in config.get("categories", {}) and category_hint not in ordered:
        ordered.append(category_hint)
    elif category_hint in ordered:
        ordered.remove(category_hint)
        ordered.insert(0, category_hint)
    if not ordered:
        fallback = category_hint if category_hint in config.get("categories", {}) else "product_and_workflow_tools"
        ordered = [fallback]
    return ordered[:3]


def source_weight(source_name: str, config: dict) -> int:
    weights = config.get("source_weights", {})
    if source_name in weights:
        return int(weights[source_name])
    for known, weight in weights.items():
        if known.casefold() in source_name.casefold():
            return int(weight)
    return 10


def normalize_candidate(
    *,
    source: str,
    source_kind: str,
    title: object,
    url: object,
    summary: object = "",
    published_at: object = None,
    category_hint: str | None = None,
    signals: dict | None = None,
    evidence_urls: list[str] | None = None,
    extra_text: object = "",
    config: dict,
    now: datetime,
) -> dict | None:
    clean_title = clean_text(title)[:300]
    clean_url = str(url or "").strip()
    canonical = canonicalize_url(clean_url)
    if not clean_title or not canonical or not canonical.startswith(("http://", "https://")):
        return None

    summary_text = clean_text(summary)[:MAX_DESCRIPTION]
    # Do not promote an individual's support case as general audience content.
    # Support-ticket IDs are not useful editorial evidence and can unnecessarily
    # amplify a user-specific dispute when the forum page is publicly indexed.
    if source == "Shopify Community" and re.search(
        r"\b(?:support\s+)?ticket\b[^\d]{0,20}\d{4,}\b",
        clean_title + " " + summary_text,
        flags=re.I,
    ):
        return None
    pub_dt = parse_datetime(published_at)
    search_text = " ".join([clean_title, summary_text, clean_text(extra_text)])
    categories = category_matches(search_text, config, category_hint)
    signal_values = signals or {}
    source_points = source_weight(source, config)
    days_old = None
    if pub_dt:
        days_old = max(0.0, (now.astimezone(timezone.utc) - pub_dt).total_seconds() / 86400.0)

    if days_old is None:
        recency_points = 8
    elif days_old <= 1:
        recency_points = 30
    elif days_old <= 3:
        recency_points = 26
    elif days_old <= 7:
        recency_points = 21
    elif days_old <= 14:
        recency_points = 15
    elif days_old <= 30:
        recency_points = 8
    else:
        recency_points = 2

    stars = max(0, int(signal_values.get("stars") or 0))
    points = max(0, int(signal_values.get("points") or 0))
    comments = max(0, int(signal_values.get("comments") or 0))
    forks = max(0, int(signal_values.get("forks") or 0))
    # Cumulative GitHub stars are deliberately a weak signal. They reward old,
    # famous repositories and do not establish that something is trending now.
    # Actual hourly star velocity is added later from persisted snapshots.
    traction_points = 0
    if stars:
        traction_points += min(4, round(1.0 * math.log1p(stars)))
        traction_points += min(1, round(0.25 * math.log1p(forks)))
    if points:
        traction_points += min(10, round(2.5 * math.log1p(points)))
    if comments:
        traction_points += min(4, round(1.2 * math.log1p(comments)))
    # Directory adoption counts are weak context, not editorial quality or recency.
    # Cap the combined effect so popular plugin listings cannot dominate timely,
    # independently useful articles and release notes on popularity alone.
    active_installs = max(0, int(signal_values.get("active_installs") or 0))
    num_ratings = max(0, int(signal_values.get("num_ratings") or 0))
    downloaded = max(0, int(signal_values.get("downloaded") or 0))
    if active_installs:
        traction_points += min(2, round(0.5 * math.log10(active_installs + 1)))
    if num_ratings:
        traction_points += min(1, round(0.25 * math.log1p(num_ratings)))
    if downloaded:
        traction_points += min(1, round(0.25 * math.log10(downloaded + 1)))
    traction_points = min(12, traction_points)

    technical_markers = (
        "api", "sdk", "integration", "extension", "plugin", "automation", "workflow",
        "open source", "open-source", "self-hosted", "shopify", "checkout", "analytics",
        "webhook", "cli", "mcp", "docker", "payments", "digital product", "storefront",
    )
    marker_hits = sum(1 for word in technical_markers if word in search_text.casefold())
    technical_points = min(20, 5 + 3 * min(5, marker_hits))
    specificity_points = min(10, len(summary_text) // 45)
    priority = min(100, source_points + recency_points + traction_points + technical_points + specificity_points)

    evidence = []
    for item in (evidence_urls or []) + [clean_url]:
        item = str(item or "").strip()
        if item.startswith(("https://", "http://")) and item not in evidence:
            evidence.append(item)

    identity = hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]
    return {
        "id": identity,
        "title": clean_title,
        "url": clean_url,
        "canonical_url": canonical,
        "summary": summary_text,
        "source": source,
        "source_kind": source_kind,
        "categories": categories,
        "primary_category": categories[0],
        "published_at": iso_utc(pub_dt),
        "days_old": round(days_old, 2) if days_old is not None else None,
        "retrieved_at_utc": iso_utc(now),
        "evidence_urls": evidence,
        "signals": signal_values,
        "priority_score": int(priority),
        "score_components": {
            "source": source_points,
            "recency": recency_points,
            "public_signal": traction_points,
            "technical_specificity": technical_points,
            "summary_detail": specificity_points,
        },
        "verification_status": "needs_primary_source_review",
        "editorial_note": "Discovery signal only. Verify functionality, pricing/licence, recency and claims at the original source.",
    }


def _direct_child_text(node: ET.Element, names: set[str]) -> str:
    for child in list(node):
        local = child.tag.rsplit("}", 1)[-1].casefold()
        if local in names:
            if local == "link" and child.attrib.get("href"):
                return child.attrib["href"]
            return "".join(child.itertext()).strip()
    return ""


def parse_feed_xml(
    xml_text: str | bytes,
    feed: dict,
    config: dict,
    now: datetime | None = None,
) -> list[dict]:
    """Parse basic RSS 2.0 and Atom without a third-party dependency."""
    now = now or datetime.now(timezone.utc)
    root = ET.fromstring(xml_text)
    items = root.findall(".//item")
    if not items:
        items = [node for node in root.iter() if node.tag.rsplit("}", 1)[-1].casefold() == "entry"]

    found: list[dict] = []
    for item in items:
        title = _direct_child_text(item, {"title"})
        link = _direct_child_text(item, {"link"})
        if not link:
            for node in list(item):
                if node.tag.rsplit("}", 1)[-1].casefold() == "link":
                    link = str(node.attrib.get("href") or "")
                    if node.attrib.get("rel", "alternate") in {"alternate", ""}:
                        break
        summary = _direct_child_text(item, {"description", "summary", "content", "encoded"})
        date_value = _direct_child_text(item, {"pubdate", "published", "updated", "date", "dc:date"})
        if not date_value:
            for node in item.iter():
                if node.tag.rsplit("}", 1)[-1].casefold() in {"pubdate", "published", "updated", "date"}:
                    date_value = "".join(node.itertext()).strip()
                    if date_value:
                        break
        categories = [
            clean_text("".join(node.itertext()))
            for node in list(item)
            if node.tag.rsplit("}", 1)[-1].casefold() == "category"
        ]
        candidate = normalize_candidate(
            source=feed["name"],
            source_kind="official_changelog" if "changelog" in feed["id"] else "rss",
            title=title,
            url=link,
            summary=summary,
            published_at=date_value,
            category_hint=feed.get("category_hint"),
            signals={"feed_categories": categories} if categories else {},
            evidence_urls=[link],
            extra_text=" ".join(categories),
            config=config,
            now=now,
        )
        if candidate:
            found.append(candidate)
    return found


def fetch_bytes(url: str, headers: dict | None = None, timeout: int = 15) -> bytes:
    request_headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json, application/atom+xml, application/rss+xml, application/xml, text/xml, */*",
    }
    request_headers.update(headers or {})
    request = urllib.request.Request(url, headers=request_headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def discover_feed(feed: dict, config: dict, now: datetime, lookback_days: int) -> tuple[list[dict], dict]:
    try:
        data = fetch_bytes(feed["url"])
        candidates = parse_feed_xml(data, feed, config, now)
        candidates = [
            item for item in candidates
            if item["days_old"] is None or item["days_old"] <= lookback_days
        ]
        return candidates, {"source": feed["name"], "kind": "rss", "items_kept": len(candidates), "status": "ok"}
    except Exception as exc:
        return [], {"source": feed["name"], "kind": "rss", "items_kept": 0, "status": "error", "error": type(exc).__name__}


def discover_github_search(
    search: dict,
    config: dict,
    now: datetime,
    lookback_days: int,
    per_source: int,
) -> tuple[list[dict], dict]:
    active_since = (now - timedelta(days=lookback_days)).date().isoformat()
    query = search["query"].replace("{created_since}", active_since).replace("{active_since}", active_since)
    params = urllib.parse.urlencode({"q": query, "sort": "updated", "order": "desc", "per_page": str(min(50, per_source))})
    url = "https://api.github.com/search/repositories?" + params
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        headers["Authorization"] = "Bearer " + token
    try:
        payload = github_search_json(url, headers=headers)
        candidates = []
        for repo in payload.get("items", []):
            if repo.get("archived") or repo.get("disabled"):
                continue
            license_info = repo.get("license") or {}
            description = clean_text(repo.get("description") or "")
            signals = {
                "stars": int(repo.get("stargazers_count") or 0),
                "github_repo_id": str(repo.get("id") or ""),
                "full_name": str(repo.get("full_name") or repo.get("name") or ""),
                "forks": int(repo.get("forks_count") or 0),
                "open_issues": int(repo.get("open_issues_count") or 0),
                "language": repo.get("language") or "",
                "license_spdx": license_info.get("spdx_id") or "",
                "created_at": repo.get("created_at") or "",
                "updated_at": repo.get("updated_at") or "",
                "pushed_at": repo.get("pushed_at") or "",
                "archived": False,
                "query_id": search["id"],
            }
            candidate = normalize_candidate(
                source="GitHub Search",
                source_kind="github_repository",
                title=repo.get("full_name") or repo.get("name"),
                url=repo.get("html_url"),
                summary=description,
                published_at=repo.get("pushed_at") or repo.get("updated_at") or repo.get("created_at"),
                category_hint=search.get("category"),
                signals=signals,
                evidence_urls=[repo.get("html_url", ""), repo.get("homepage") or ""],
                extra_text=" ".join([str(repo.get("language") or ""), " ".join(repo.get("topics") or [])]),
                config=config,
                now=now,
            )
            if candidate:
                candidates.append(candidate)
        return candidates, {
            "source": "GitHub Search · " + search["id"],
            "kind": "github_repository",
            "items_kept": len(candidates),
            "status": "ok",
            "total_count": int(payload.get("total_count") or 0),
        }
    except urllib.error.HTTPError as exc:
        return [], {
            "source": "GitHub Search · " + search["id"],
            "kind": "github_repository",
            "items_kept": 0,
            "status": "error",
            "error": "HTTP " + str(exc.code),
        }
    except Exception as exc:
        return [], {
            "source": "GitHub Search · " + search["id"],
            "kind": "github_repository",
            "items_kept": 0,
            "status": "error",
            "error": type(exc).__name__,
        }


def discover_hn_search(
    search: dict,
    config: dict,
    now: datetime,
    lookback_days: int,
    per_source: int,
) -> tuple[list[dict], dict]:
    params: dict[str, str] = {"tags": search.get("tags", "story"), "hitsPerPage": str(min(50, per_source))}
    if search.get("query"):
        params["query"] = search["query"]
    url = "https://hn.algolia.com/api/v1/search_by_date?" + urllib.parse.urlencode(params)
    try:
        payload = json.loads(fetch_bytes(url, headers={"Accept": "application/json"}).decode("utf-8"))
        candidates = []
        for hit in payload.get("hits", []):
            title = clean_text(hit.get("story_title") or hit.get("title") or "")
            if not title:
                continue
            story_id = hit.get("story_id") or hit.get("objectID")
            discussion_url = "https://news.ycombinator.com/item?id=" + urllib.parse.quote(str(story_id))
            external_url = hit.get("story_url") or hit.get("url") or discussion_url
            date_value = hit.get("created_at") or ""
            signal_values = {
                "points": int(hit.get("points") or 0),
                "comments": int(hit.get("num_comments") or 0),
                "hn_story_id": str(story_id or ""),
                "query_id": search["id"],
            }
            candidate = normalize_candidate(
                source="Hacker News",
                source_kind="hacker_news",
                title=title,
                url=external_url,
                summary=hit.get("story_text") or hit.get("comment_text") or "",
                published_at=date_value,
                category_hint=search.get("category"),
                signals=signal_values,
                evidence_urls=[discussion_url, external_url],
                config=config,
                now=now,
            )
            if candidate and (candidate["days_old"] is None or candidate["days_old"] <= lookback_days):
                candidates.append(candidate)
        return candidates, {
            "source": "Hacker News · " + search["id"],
            "kind": "hacker_news",
            "items_kept": len(candidates),
            "status": "ok",
            "total_count": len(payload.get("hits", [])),
        }
    except Exception as exc:
        return [], {
            "source": "Hacker News · " + search["id"],
            "kind": "hacker_news",
            "items_kept": 0,
            "status": "error",
            "error": type(exc).__name__,
        }



def parse_wordpress_datetime(value: object) -> str | None:
    """Normalize the WordPress.org Plugin API's human-readable last-updated timestamp."""
    raw = str(value or "").strip()
    parsed = parse_datetime(raw)
    if parsed:
        return iso_utc(parsed)
    match = re.fullmatch(
        r"(\d{4}-\d{2}-\d{2})\s+(\d{1,2}):(\d{2})\s*(am|pm)\s+GMT",
        raw,
        flags=re.I,
    )
    if not match:
        return None
    try:
        hour = int(match.group(2)) % 12
        if match.group(4).casefold() == "pm":
            hour += 12
        parsed_dt = datetime.fromisoformat(
            f"{match.group(1)}T{hour:02d}:{int(match.group(3)):02d}:00+00:00"
        )
        return iso_utc(parsed_dt)
    except ValueError:
        return None


def parse_wordpress_plugin_response(
    payload: dict,
    search: dict,
    config: dict,
    now: datetime,
) -> list[dict]:
    """Convert official WordPress.org Plugin Directory API results into discovery candidates."""
    results: list[dict] = []
    for plugin in payload.get("plugins", []):
        slug = clean_text(plugin.get("slug") or "")
        title = clean_text(plugin.get("name") or "")
        if not slug or not title:
            continue
        # Keep the official directory page as the primary URL; the vendor homepage
        # is a secondary evidence link, not a substitute for independent metadata.
        url = f"https://wordpress.org/plugins/{urllib.parse.quote(slug)}/"
        description = clean_text(
            plugin.get("short_description") or plugin.get("description") or ""
        )
        try:
            active_installs = max(0, int(plugin.get("active_installs") or 0))
        except (TypeError, ValueError):
            active_installs = 0
        try:
            num_ratings = max(0, int(plugin.get("num_ratings") or 0))
        except (TypeError, ValueError):
            num_ratings = 0
        try:
            rating_percent = max(0.0, min(100.0, float(plugin.get("rating") or 0)))
        except (TypeError, ValueError):
            rating_percent = 0.0
        try:
            downloaded = max(0, int(plugin.get("downloaded") or 0))
        except (TypeError, ValueError):
            downloaded = 0
        last_updated = parse_wordpress_datetime(plugin.get("last_updated"))
        signals = {
            "wordpress_slug": slug,
            "active_installs": active_installs,
            "rating_percent": rating_percent,
            "num_ratings": num_ratings,
            "downloaded": downloaded,
            "last_updated": str(plugin.get("last_updated") or ""),
            "query_id": search.get("id", ""),
            "signal_interpretation": "free-plugin adoption and review activity; not paid-revenue evidence",
        }
        candidate = normalize_candidate(
            source="WordPress Plugin Directory",
            source_kind="wordpress_plugin",
            title=title,
            url=url,
            summary=description,
            published_at=last_updated,
            category_hint=search.get("category"),
            signals=signals,
            evidence_urls=[url, str(plugin.get("homepage") or "")],
            extra_text=" ".join((slug, " ".join((plugin.get("tags") or {}).keys()))),
            config=config,
            now=now,
        )
        if candidate:
            results.append(candidate)
    return results


def discover_wordpress_search(
    search: dict,
    config: dict,
    now: datetime,
    lookback_days: int,
    per_source: int,
) -> tuple[list[dict], dict]:
    """Search the official WordPress.org plugin directory for product/use-case signals."""
    params = {
        "action": "query_plugins",
        "request[search]": str(search.get("query") or ""),
        "request[per_page]": str(min(50, per_source)),
        "request[fields][active_installs]": "1",
        "request[fields][rating]": "1",
        "request[fields][num_ratings]": "1",
        "request[fields][downloaded]": "1",
        "request[fields][last_updated]": "1",
        "request[fields][homepage]": "1",
        "request[fields][short_description]": "1",
        "request[fields][tags]": "1",
    }
    url = "https://api.wordpress.org/plugins/info/1.2/?" + urllib.parse.urlencode(params)
    try:
        payload = json.loads(fetch_bytes(url, headers={"Accept": "application/json"}).decode("utf-8"))
        candidates = parse_wordpress_plugin_response(payload, search, config, now)
        # Do not apply the release-news freshness cutoff to established plugins:
        # their current install/review footprint can be useful even between updates.
        return candidates, {
            "source": "WordPress Plugin Directory · " + str(search.get("id") or ""),
            "kind": "wordpress_plugin",
            "items_kept": len(candidates),
            "status": "ok",
            "total_count": int((payload.get("info") or {}).get("results") or len(payload.get("plugins") or [])),
        }
    except urllib.error.HTTPError as exc:
        return [], {
            "source": "WordPress Plugin Directory · " + str(search.get("id") or ""),
            "kind": "wordpress_plugin",
            "items_kept": 0,
            "status": "error",
            "error": "HTTP " + str(exc.code),
        }
    except Exception as exc:
        return [], {
            "source": "WordPress Plugin Directory · " + str(search.get("id") or ""),
            "kind": "wordpress_plugin",
            "items_kept": 0,
            "status": "error",
            "error": type(exc).__name__,
        }


def merge_duplicates(candidates: list[dict]) -> list[dict]:
    merged: dict[str, dict] = {}
    for candidate in candidates:
        key = candidate["canonical_url"]
        if key not in merged:
            item = dict(candidate)
            item["discovered_via"] = [candidate["source"]]
            merged[key] = item
            continue
        current = merged[key]
        for source in candidate.get("discovered_via", [candidate["source"]]):
            if source not in current["discovered_via"]:
                current["discovered_via"].append(source)
        for url in candidate.get("evidence_urls", []):
            if url not in current["evidence_urls"]:
                current["evidence_urls"].append(url)
        for category in candidate.get("categories", []):
            if category not in current["categories"]:
                current["categories"].append(category)
        for name, value in candidate.get("signals", {}).items():
            if name not in current["signals"] or (
                isinstance(value, (int, float)) and isinstance(current["signals"].get(name), (int, float))
                and value > current["signals"][name]
            ):
                current["signals"][name] = value
        if candidate["priority_score"] > current["priority_score"]:
            for field in ("source", "source_kind", "summary", "published_at", "days_old", "priority_score", "score_components"):
                current[field] = candidate[field]
            current["primary_category"] = candidate["primary_category"]
        current["categories"] = current["categories"][:3]
    return sorted(merged.values(), key=lambda item: (-item["priority_score"], item["title"].casefold()))


def discover(config: dict, lookback_days: int = 14, per_source: int = 15) -> tuple[list[dict], list[dict]]:
    now = datetime.now(timezone.utc)
    jobs = []
    candidates: list[dict] = []
    diagnostics: list[dict] = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        for feed in config["feeds"]:
            jobs.append(pool.submit(discover_feed, feed, config, now, lookback_days))
        for search in config["github_searches"]:
            jobs.append(pool.submit(discover_github_search, search, config, now, lookback_days, per_source))
        for search in config["hn_searches"]:
            jobs.append(pool.submit(discover_hn_search, search, config, now, lookback_days, per_source))
        for search in config.get("wordpress_searches", []):
            jobs.append(pool.submit(discover_wordpress_search, search, config, now, lookback_days, per_source))
        for future in as_completed(jobs):
            found, diagnostic = future.result()
            candidates.extend(found)
            diagnostics.append(diagnostic)

    unique = merge_duplicates(candidates)
    unique = [item for item in unique if item.get("priority_score", 0) > 0]
    diagnostics.sort(key=lambda row: (row["kind"], row["source"]))
    return unique, diagnostics


def select_preview_candidates(candidates: list[dict], limit: int) -> list[dict]:
    """Return a priority-ranked preview with representation from healthy sources.

    This selection affects only the read-only review report. The hourly publishing
    selector has its own ranking/diversity rules and never consumes this preview.
    """
    if limit <= 0:
        return []

    def source_group(item: dict) -> str:
        source = str(item.get("source") or "Unknown source")
        if source.startswith("GitHub Search"):
            return "GitHub Search"
        if source.startswith("Hacker News"):
            return "Hacker News"
        if source.startswith("WordPress Plugin Directory"):
            return "WordPress Plugin Directory"
        return source

    def identity(item: dict) -> str:
        return str(item.get("id") or item.get("canonical_url") or item.get("url") or id(item))

    # Preserve the original priority order within each source.
    grouped: dict[str, list[dict]] = {}
    for item in candidates:
        grouped.setdefault(source_group(item), []).append(item)

    selected_ids: set[str] = set()
    selected: list[dict] = []
    source_counts: dict[str, int] = {}
    category_counts: dict[str, int] = {}
    max_per_source_group = 3
    max_per_category = 8

    # Reserve one slot per source before applying category caps. Coverage of
    # configured sources is the primary purpose of this report.
    for source, items in grouped.items():
        if len(selected) >= limit:
            break
        item = next((candidate for candidate in items if identity(candidate) not in selected_ids), None)
        if item is None:
            continue
        key = identity(item)
        category = str(item.get("primary_category") or "unknown")
        selected.append(item)
        selected_ids.add(key)
        source_counts[source] = 1
        category_counts[category] = category_counts.get(category, 0) + 1

    # Fill the remaining slots by priority, applying soft caps to limit source
    # concentration without dropping the reserved representation.
    for item in candidates:
        if len(selected) >= limit:
            break
        key = identity(item)
        if key in selected_ids:
            continue
        source = source_group(item)
        category = str(item.get("primary_category") or "unknown")
        if source_counts.get(source, 0) >= max_per_source_group:
            continue
        if category_counts.get(category, 0) >= max_per_category:
            continue
        selected.append(item)
        selected_ids.add(key)
        source_counts[source] = source_counts.get(source, 0) + 1
        category_counts[category] = category_counts.get(category, 0) + 1

    # Keep the rendered report ordered by the original priority sort.
    selected_set = {identity(item) for item in selected}
    ordered: list[dict] = []
    emitted: set[str] = set()
    for item in candidates:
        key = identity(item)
        if key in selected_set and key not in emitted:
            ordered.append(item)
            emitted.add(key)
        if len(ordered) >= limit:
            break
    return ordered


def write_report(
    candidates: list[dict],
    diagnostics: list[dict],
    config: dict,
    lookback_days: int,
    limit: int,
    output_dir: Path,
) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    now_ist = datetime.now(IST).isoformat(timespec="seconds")
    visible = select_preview_candidates(candidates, limit)
    payload = {
        "generated_at_ist": now_ist,
        "mode": "research_only_dry_run",
        "posted_to_x": False,
        "lookback_days": lookback_days,
        "candidate_count_total": len(candidates),
        "candidate_count_shown": len(visible),
        "preview_selection": {
            "policy": "priority-ranked source/category-diverse sample; preview-only, not used by the publisher",
            "max_per_source_group": 3,
            "max_per_category": 8,
        },
        "source_diagnostics": diagnostics,
        "candidates": visible,
        "editorial_safety": [
            "No candidate has been published or automatically drafted into a post.",
            "Priority score is a queue-ordering heuristic, not a quality or factual-accuracy verdict.",
            "Stars, votes and comments are weak activity signals and can be gamed; do not present them as proof of quality or sustained use.",
            "Review the product/project's own page, documentation, price, licence, target user, privacy implications and last update.",
            "WordPress active installs, downloads and ratings are directory metadata and feedback, not independent verification of quality, compatibility, maintenance or security.",
            "For news or platform changes, confirm the effective date and affected versions against the primary source.",
        ],
    }
    json_path = output_dir / "discovery-candidates.json"
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    okay = sum(1 for row in diagnostics if row["status"] == "ok")
    lines = [
        "# Legivox multidomain discovery preview",
        "",
        f"- Generated: {now_ist}",
        "- Mode: research-only dry run; nothing was posted to X",
        f"- Lookback: {lookback_days} days",
        f"- Candidates found: {len(candidates)}",
        f"- Candidates shown: {len(visible)}",
        f"- Source checks successful: {okay}/{len(diagnostics)}",
        "",
        "Legivox discovers useful developer tools, AI and automation projects, creator tools, digital-product platforms, commerce workflows, marketing tactics and technology. The priority score ranks candidates, but this report applies source/category caps to show a more representative review sample.",
        "",
        "The preview diversity caps affect only this report. The hourly publishing selector uses its own ranking and diversity rules; this file is not consumed by the publisher.",
        "",
        "## Source health",
        "",
        "| Source | Items kept | Result |",
        "|---|---:|---|",
    ]
    for row in diagnostics:
        result = row["status"].upper()
        if row.get("error"):
            result += " (" + row["error"] + ")"
        lines.append(f'| {row["source"]} | {row["items_kept"]} | {result} |')

    lines += ["", "## Review queue", ""]
    if not visible:
        lines += ["No candidates were retrieved in this run. Check the source-health table before interpreting this as a quiet day.", ""]
    for index, item in enumerate(visible, 1):
        category = config["categories"].get(item["primary_category"], {}).get("label", item["primary_category"])
        description = item.get("summary") or "_No useful summary was provided by the source._"
        published = item.get("published_at") or "Date not provided"
        discovered_via = ", ".join(item.get("discovered_via", [item.get("source", "Unknown source")]))
        lines += [
            f'### {index}. [{item["title"]}]({item["url"]})',
            "",
            f'- **Lane:** {category}',
            f'- **Priority:** {item["priority_score"]}/100 · **Source:** {discovered_via}',
            f'- **Date/activity:** {published}',
            f'- **What the source says:** {description}',
            f'- **Verification:** {item["verification_status"]}',
        ]
        signals = item.get("signals", {})
        signal_bits = []
        for key in ("stars", "forks", "points", "comments", "language", "license_spdx", "pushed_at", "active_installs", "rating_percent", "num_ratings", "downloaded", "last_updated"):
            value = signals.get(key)
            if value not in (None, "", 0):
                signal_bits.append(f"{key}={value}")
        if signal_bits:
            lines.append("- **Public metadata:** " + ", ".join(signal_bits))
        evidence = item.get("evidence_urls", [])
        if evidence:
            lines.append("- **Evidence links:** " + " · ".join("[" + str(i + 1) + "](" + url + ")" for i, url in enumerate(evidence[:3])))
        lines.append("")

    lines += [
        "## Human editorial gate",
        "",
        "Before anything becomes a Legivox post, a reviewer should be able to answer:",
        "",
        "1. **What does it actually do?** Explain the real workflow or technical capability, not the tagline.",
        "2. **Who benefits and why now?** Developers, Shopify merchants, creators, solo founders, data teams, or another clear user.",
        "3. **What is verified?** Check the primary page, documentation, changelog, demo and effective date. Separate fact from inference.",
        "4. **What are the trade-offs?** Price, free-tier limits, licence, lock-in, privacy/security, integrations and maintenance.",
        "5. **Can we demonstrate value?** A short example, implementation path, comparison, or honest limitation is better than launch-day cheerleading.",
        "",
        "## Important interpretation notes",
        "",
        "- A Product Hunt launch or Hacker News discussion is a discovery lead, not proof that the product works well.",
        "- GitHub stars are cumulative, not star growth. This version does not yet compute daily star deltas.",
        "- Product pages, commercial terms and licences may change. Recheck them when preparing a post.",
        "- This pipeline only saves a candidate queue. It does not generate copy or interact with X.",
        "",
    ]
    markdown_path = output_dir / "discovery-report.md"
    markdown_path.write_text("\n".join(lines), encoding="utf-8")
    return markdown_path, json_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lookback-days", type=int, default=14, help="How recent discovered items should be (1-60).")
    parser.add_argument("--limit", type=int, default=50, help="Maximum candidates shown in the report (1-100).")
    parser.add_argument("--per-source", type=int, default=15, help="Maximum GitHub/HN results to ask for per query (1-50).")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Output directory; defaults to output/discovery.")
    args = parser.parse_args(argv)
    if not 1 <= args.lookback_days <= 60:
        parser.error("--lookback-days must be between 1 and 60")
    if not 1 <= args.limit <= 100:
        parser.error("--limit must be between 1 and 100")
    if not 1 <= args.per_source <= 50:
        parser.error("--per-source must be between 1 and 50")

    try:
        config = load_config()
        candidates, diagnostics = discover(config, args.lookback_days, args.per_source)
        markdown_path, json_path = write_report(
            candidates, diagnostics, config, args.lookback_days, args.limit, Path(args.output_dir)
        )
    except Exception as exc:
        print("Discovery pipeline failed: " + type(exc).__name__, file=sys.stderr)
        return 1

    print("Legivox multidomain discovery preview complete; nothing was published.")
    print(f"Candidates: {len(candidates)}")
    print(f"Sources responding: {sum(row['status'] == 'ok' for row in diagnostics)}/{len(diagnostics)}")
    print("Report: " + str(markdown_path))
    print("JSON: " + str(json_path))
    if diagnostics and not any(row["status"] == "ok" for row in diagnostics):
        print("Every configured source failed; inspect network/API access before using this run.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
