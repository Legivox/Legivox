#!/usr/bin/env python3
"""Publish one of today's curated Legivox posts with optional licensed media."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import tempfile
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from tweetkit_x import TweetKit
from prepare_daily_plan import write_queue_report

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output"
STATE_PATH = OUTPUT_DIR / "queue-state.json"
PLAN_PATH = OUTPUT_DIR / "daily-plan.json"
PUBLISHED_PATH = OUTPUT_DIR / "published.jsonl"
EXPECTED_USERNAME = "Legivox"
IST = ZoneInfo("Asia/Kolkata")
USER_AGENT = "LegivoxPublisher/1.0 (https://github.com/Legivox/Legivox)"
MAX_IMAGE_BYTES = 8 * 1024 * 1024


def fail(message: str) -> None:
    print("Legivox publisher: " + message, file=sys.stderr)
    raise SystemExit(1)


def clean(value: object) -> str:
    return " ".join(str(value or "").split()).strip()


def plain_html(value: object) -> str:
    raw = html.unescape(str(value or ""))
    raw = re.sub(r"<[^>]+>", " ", raw)
    return clean(raw)


def get_json(url: str, timeout: int = 12) -> dict:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def find_free_image(query: str, idea_id: str) -> tuple[str | None, dict | None]:
    """Find a relevant Commons bitmap with CC0 or public-domain metadata."""
    params = urllib.parse.urlencode({
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrnamespace": "6",
        "gsrlimit": "10",
        "prop": "imageinfo",
        "iiprop": "url|mime|extmetadata",
        "iiurlwidth": "1200",
        "format": "json",
    })
    endpoint = "https://commons.wikimedia.org/w/api.php?" + params
    try:
        payload = get_json(endpoint)
    except Exception:
        print("Image search unavailable for " + idea_id + "; publishing without media.")
        return None, None

    pages = list((payload.get("query", {}).get("pages") or {}).values())
    query_terms = {
        term.lower() for term in re.findall(r"[a-zA-Z]{4,}", query)
        if term.lower() not in {"with", "from", "small", "work", "idea", "image"}
    }
    temp_dir = Path(tempfile.gettempdir()) / "legivox-media"
    temp_dir.mkdir(parents=True, exist_ok=True)

    for page in pages:
        info_list = page.get("imageinfo") or []
        if not info_list:
            continue
        info = info_list[0]
        mime = clean(info.get("mime")).lower()
        if mime not in {"image/jpeg", "image/png", "image/webp"}:
            continue
        meta = info.get("extmetadata") or {}
        licence = plain_html((meta.get("LicenseShortName") or {}).get("value"))
        license_lower = licence.lower()
        # Only use licenses where this workflow can safely reuse the image
        # without needing to squeeze a long attribution into a short post.
        if not (license_lower.startswith("cc0") or "public domain" in license_lower or license_lower in {"pd", "pd-self"}):
            continue

        title = clean(page.get("title"))
        description = plain_html((meta.get("ImageDescription") or {}).get("value"))
        search_text = (title + " " + description).lower()
        if query_terms and not any(term in search_text for term in query_terms):
            continue

        image_url = clean(info.get("thumburl") or info.get("url"))
        page_url = clean(info.get("descriptionurl"))
        if not image_url or not page_url:
            continue
        extension = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp"}[mime]
        local_path = temp_dir / (idea_id + extension)
        try:
            request = urllib.request.Request(image_url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=15) as response:
                data = response.read(MAX_IMAGE_BYTES + 1)
            if not data or len(data) > MAX_IMAGE_BYTES:
                continue
            local_path.write_bytes(data)
        except Exception:
            continue

        creator = plain_html((meta.get("Artist") or {}).get("value"))
        if not creator:
            creator = plain_html((meta.get("Credit") or {}).get("value")) or "Creator not stated"
        alt_description = description or title.replace("File:", "")
        credit = {
            "title": title,
            "creator": creator[:240],
            "license": licence,
            "file_page": page_url,
            "direct_url": image_url,
            "mime": mime,
            "alt_text": (alt_description[:700] + " Source: Wikimedia Commons, " + creator[:160] + ". License: " + licence + ". File: " + page_url)[:950],
        }
        return str(local_path), credit

    print("No matching CC0/public-domain bitmap found for " + idea_id + "; publishing without media.")
    return None, None


def write_plan(plan: dict) -> None:
    PLAN_PATH.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slot", type=int, choices=(0, 1, 2), required=True, help="Today's post slot: 0, 1, or 2.")
    args = parser.parse_args()

    cookie = os.environ.get("TWEETKIT_COOKIE", "").strip()
    if not cookie:
        fail("Missing Actions secret X_SESSION_COOKIE. No post was attempted.")
    try:
        client = TweetKit(cookie=cookie, timeout=25)
        identity = client.whoami()
    except Exception:
        fail("Could not initialise the X session. Check the secret; details suppressed.")
    if not identity.get("ready") or not identity.get("user_id"):
        fail("Session cookie is incomplete. No post was attempted.")
    try:
        profile = client.user_profile(EXPECTED_USERNAME)
    except Exception:
        fail("Could not verify the @Legivox profile. No post was attempted.")
    if not profile.get("ok") or str(profile.get("username", "")).lower() != EXPECTED_USERNAME.lower():
        fail("Could not verify the public @Legivox profile. No post was attempted.")
    if str(identity.get("user_id")) != str(profile.get("id")):
        fail("The cookie belongs to a different X account, not @Legivox. No post was attempted.")

    try:
        plan = json.loads(PLAN_PATH.read_text(encoding="utf-8"))
        state = json.loads(STATE_PATH.read_text(encoding="utf-8")) if STATE_PATH.exists() else {}
    except Exception:
        fail("Could not read today's plan or publisher state.")
    today = datetime.now(IST).date().isoformat()
    if plan.get("date_ist") != today:
        fail("No current daily plan exists. The 06:00 IST planning run must complete before posts can be published.")
    posts = plan.get("posts") or []
    if len(posts) != 3 or args.slot >= len(posts):
        fail("Today's plan does not contain three posts. No post was attempted.")
    item = posts[args.slot]
    draft = clean(item.get("text"))
    if not draft or len(draft) > 280:
        fail("The selected draft is empty or exceeds 280 characters.")
    digest = hashlib.sha256(draft.encode("utf-8")).hexdigest()
    used_hashes = set(state.get("used_draft_hashes", []))
    if digest in used_hashes:
        item["status"] = "skipped: draft hash already used"
        write_plan(plan)
        write_queue_report(plan)
        print("Skipping slot " + str(args.slot) + ": draft already used.")
        return 0

    try:
        recent = client.get_tweets(limit=100, include_replies=False)
    except Exception:
        fail("Could not safely check recent @Legivox posts for duplicates. No post was attempted.")
    recent_texts = {clean(row.get("text", "")) for row in recent if row.get("text")}
    if draft in recent_texts:
        used_hashes.add(digest)
        state["used_draft_hashes"] = sorted(used_hashes)
        item["status"] = "skipped: exact duplicate found in recent timeline"
        save_state(state)
        write_plan(plan)
        write_queue_report(plan)
        print("Skipping slot " + str(args.slot) + ": exact duplicate found.")
        return 0

    image_path = None
    image_credit = None
    image_query = clean(item.get("image_query") or item.get("niche"))
    if image_query:
        image_path, image_credit = find_free_image(image_query, clean(item.get("idea_id") or ("slot-" + str(args.slot))))

    try:
        if image_path:
            result = client.post(draft, image_path=image_path, alt_texts=[image_credit["alt_text"]])
        else:
            result = client.post(draft)
    except Exception:
        item["status"] = "failed: posting exception; request was not retried"
        write_plan(plan)
        write_queue_report(plan)
        fail("The posting request raised an exception. It was not retried; check X before rerunning.")
    if not isinstance(result, dict) or not result.get("ok"):
        item["status"] = "failed: X did not confirm post"
        write_plan(plan)
        write_queue_report(plan)
        status = result.get("status") if isinstance(result, dict) else None
        fail("X did not confirm the post (HTTP status " + str(status or "unknown") + "). The request was not retried.")

    now = datetime.now(IST).isoformat(timespec="seconds")
    used_hashes.add(digest)
    recent_idea_ids = list(state.get("recent_idea_ids", []))
    recent_idea_ids.append(item["idea_id"])
    state.update({
        "used_draft_hashes": sorted(used_hashes),
        "published_count": int(state.get("published_count", 0)) + 1,
        "last_idea_id": item["idea_id"],
        "recent_idea_ids": recent_idea_ids[-9:],
        "last_published_at": now,
        "last_published_url": result.get("url", ""),
    })
    published = {
        "timestamp": now,
        "date_ist": today,
        "slot": args.slot,
        "idea_id": item["idea_id"],
        "text": draft,
        "tweet_id": result.get("id"),
        "url": result.get("url"),
        "research_query": (item.get("research") or {}).get("query"),
        "research_sources": [
            {"title": row.get("title"), "url": row.get("url"), "points": row.get("points"), "comments": row.get("comments")}
            for row in (item.get("research") or {}).get("hits", [])[:3]
        ],
        "image": image_credit,
    }
    with PUBLISHED_PATH.open("a", encoding="utf-8") as out:
        out.write(json.dumps(published, ensure_ascii=False) + "\n")
    item["status"] = "published: " + clean(result.get("url") or "URL unavailable")
    item["published_at_ist"] = now
    item["published_url"] = result.get("url", "")
    item["image"] = image_credit
    save_state(state)
    write_plan(plan)
    write_queue_report(plan)
    print("Published slot " + str(args.slot) + " for @Legivox: " + str(result.get("url", "URL unavailable")))
    print("Idea ID: " + str(item["idea_id"]) + "; character count: " + str(len(draft)))
    print("Image attached: " + ("yes (" + image_credit["license"] + ")" if image_credit else "no suitable verified image"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
