#!/usr/bin/env python3
"""Prepare a daily Legivox plan from free public signals and curated draft text.

This script does not call a paid language-model API. It uses Hacker News'
public Algolia search as a lightweight topic-selection signal. That is useful
for finding discussion activity, not proof of market demand.
"""
from __future__ import annotations

import hashlib
import html
import json
import math
import os
import re
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
IDEAS_PATH = ROOT / "data" / "ideas.json"
OUTPUT_DIR = ROOT / "output"
STATE_PATH = OUTPUT_DIR / "queue-state.json"
PLAN_PATH = OUTPUT_DIR / "daily-plan.json"
REPORT_PATH = OUTPUT_DIR / "content-queue.md"
ENGAGEMENT_PATH = OUTPUT_DIR / "engagement-shortlist.md"
IST = ZoneInfo("Asia/Kolkata")
USER_AGENT = "LegivoxResearch/1.0 (https://github.com/Legivox/Legivox)"
POSTS_PER_DAY = 3
RESEARCH_DAYS = 30


def get_json(url: str, timeout: int = 12) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def clean(value: object) -> str:
    return " ".join(str(value or "").split()).strip()


def search_signal(idea: dict, since_epoch: int) -> dict:
    query = clean(idea.get("research_query") or idea.get("niche"))
    params = urllib.parse.urlencode({
        "query": query,
        "tags": "story",
        "hitsPerPage": "8",
        "numericFilters": "created_at_i>" + str(since_epoch),
    })
    url = "https://hn.algolia.com/api/v1/search_by_date?" + params
    try:
        payload = get_json(url)
        hits = []
        for row in payload.get("hits", []):
            title = clean(row.get("story_title") or row.get("title"))
            if not title:
                continue
            object_id = clean(row.get("objectID"))
            hits.append({
                "title": title[:240],
                "url": ("https://news.ycombinator.com/item?id=" + object_id) if object_id else clean(row.get("url")),
                "external_url": clean(row.get("story_url") or row.get("url")),
                "points": int(row.get("points") or 0),
                "comments": int(row.get("num_comments") or 0),
                "created_at": clean(row.get("created_at")),
            })
        points = sum(min(100, row["points"]) for row in hits)
        comments = sum(min(100, row["comments"]) for row in hits)
        # Conversation count is a weak prioritisation signal, never a demand claim.
        score = len(hits) * 5.0 + math.log1p(points) * 0.5 + math.log1p(comments) * 1.25
        return {"query": query, "hits": hits, "score": round(score, 3), "error": None}
    except Exception as exc:
        return {"query": query, "hits": [], "score": 0.0, "error": type(exc).__name__}


def draft_options(idea: dict) -> list[str]:
    base = [idea.get("publish_text", "")]
    base.extend(idea.get("alternate_posts", []))
    unique = []
    seen = set()
    for value in base:
        draft = clean(value)
        if not draft or len(draft) > 280 or draft in seen:
            continue
        unique.append(draft)
        seen.add(draft)
    return unique


def write_queue_report(plan: dict) -> None:
    lines = [
        "# Legivox daily content plan",
        "",
        "Prepared: " + plan["prepared_at_ist"],
        "",
        "> Topics are prioritised using recent public Hacker News discussion signals plus a rotation fallback. These signals are not proof of willingness to pay. Copy is selected from the reviewed draft library, not generated from research labels.",
        "",
    ]
    for index, post in enumerate(plan["posts"], start=1):
        lines += [
            "## Post " + str(index) + " · " + post["idea_id"],
            "",
            "**Planned copy**",
            "",
            post["text"],
            "",
            "- Topic: " + post["niche"],
            "- Research query: " + post["research"]["query"],
            "- Recent discussion signal score: " + str(post["research"]["score"]),
        ]
        signals = post["research"].get("hits", [])
        if signals:
            lines += ["", "**Recent public discussion signals**", ""]
            for signal in signals[:3]:
                title = signal["title"].replace("[", "\\[").replace("]", "\\]")
                lines.append("- [" + title + "](" + signal["url"] + ") · " + str(signal["points"]) + " points · " + str(signal["comments"]) + " comments")
        else:
            lines += ["", "_No recent matching Hacker News signal was found; the topic was chosen by rotation._"]
        lines += ["", "- Status: " + post.get("status", "planned"), ""]
    lines += [
        "## Image policy",
        "",
        "The publisher searches Wikimedia Commons for matching CC0 or public-domain images. It records the file page and license metadata. If a suitable image cannot be verified, the post is published without one rather than using a random or unclear-license image.",
        "",
    ]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_engagement_shortlist(plan: dict) -> None:
    lines = [
        "# Legivox engagement shortlist",
        "",
        "Generated: " + plan["prepared_at_ist"],
        "",
        "These are candidates to review manually. No likes, replies, reposts, or follows are automated by this workflow.",
        "",
    ]
    cookie = os.environ.get("TWEETKIT_COOKIE", "").strip()
    if not cookie:
        lines += ["X search was skipped because the optional session secret was not available to the planning step.", ""]
        ENGAGEMENT_PATH.write_text("\n".join(lines), encoding="utf-8")
        return

    try:
        from tweetkit_x import TweetKit
        client = TweetKit(cookie=cookie, timeout=15)
        identity = client.whoami()
        profile = client.user_profile("Legivox")
        if not identity.get("ready") or str(identity.get("user_id")) != str(profile.get("id")):
            raise RuntimeError("session is not for @Legivox")
    except Exception:
        lines += ["X search was skipped because the session could not be safely verified. No credentials or error details are recorded.", ""]
        ENGAGEMENT_PATH.write_text("\n".join(lines), encoding="utf-8")
        return

    seen = set()
    for post in plan["posts"]:
        query = post.get("research", {}).get("query", "")
        lines += ["## " + post["niche"], "", "Search: `" + query + "`", ""]
        try:
            candidates = client.search_x(query, product="Top", limit=8)
        except Exception:
            candidates = []
        added = 0
        for candidate in candidates or []:
            url = clean(candidate.get("url"))
            text = clean(candidate.get("text"))
            author = clean(candidate.get("author") or candidate.get("username") or "X user")
            if not url or not text or url in seen or "/Legivox/status/" in url:
                continue
            seen.add(url)
            lines.append("- [" + author.replace("[", "(").replace("]", ")") + "](" + url + "): " + text[:220])
            added += 1
            if added >= 3:
                break
        if not added:
            lines.append("- No usable candidates returned for this query.")
        lines.append("")
    ENGAGEMENT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    try:
        ideas = json.loads(IDEAS_PATH.read_text(encoding="utf-8"))
        state = json.loads(STATE_PATH.read_text(encoding="utf-8")) if STATE_PATH.exists() else {}
    except Exception as exc:
        raise SystemExit("Could not read idea library/state: " + type(exc).__name__)

    if not isinstance(ideas, list) or not ideas:
        raise SystemExit("data/ideas.json must contain a non-empty list.")
    ideas = [row for row in ideas if isinstance(row, dict) and row.get("id") and draft_options(row)]
    if len(ideas) < POSTS_PER_DAY:
        raise SystemExit("At least three ideas with valid curated copy are required.")

    today = datetime.now(IST).date().isoformat()
    now_ist = datetime.now(IST)
    since_epoch = int((datetime.now(timezone.utc) - timedelta(days=RESEARCH_DAYS)).timestamp())
    used_hashes = set(state.get("used_draft_hashes", []))
    recent_ideas = set(state.get("recent_idea_ids", []))
    last_id = state.get("last_idea_id")
    ids = [row["id"] for row in ideas]
    last_index = ids.index(last_id) if last_id in ids else -1
    rotation_rank = {ids[(last_index + offset) % len(ids)]: offset for offset in range(1, len(ids) + 1)}

    signals = {}
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = {pool.submit(search_signal, idea, since_epoch): idea["id"] for idea in ideas}
        for future in as_completed(futures):
            signals[futures[future]] = future.result()

    scored = []
    for idea in ideas:
        options = [text for text in draft_options(idea)
                   if hashlib.sha256(text.encode("utf-8")).hexdigest() not in used_hashes]
        if not options:
            continue
        signal = signals.get(idea["id"], {"query": idea.get("research_query", idea["niche"]), "hits": [], "score": 0.0, "error": "missing"})
        # Use the next unused draft for an idea; never synthesize public copy from internal fields.
        score = float(signal["score"])
        if idea["id"] in recent_ideas:
            score -= 1000.0
        scored.append({
            "idea": idea,
            "text": options[0],
            "text_hash": hashlib.sha256(options[0].encode("utf-8")).hexdigest(),
            "signal": signal,
            "score": score,
            "rotation_rank": rotation_rank.get(idea["id"], len(ideas)),
        })

    scored.sort(key=lambda row: (-row["score"], row["rotation_rank"]))
    # When few topics have actual signal, select remaining topics through rotation.
    selected = scored[:POSTS_PER_DAY]
    if len(selected) < POSTS_PER_DAY:
        raise SystemExit("Fewer than three unused curated drafts remain. Add reviewed copy before continuing.")

    posts = []
    for row in selected:
        idea = row["idea"]
        signal = row["signal"]
        posts.append({
            "idea_id": idea["id"],
            "niche": clean(idea["niche"]),
            "problem": clean(idea["problem"]),
            "evidence": clean(idea["evidence"]),
            "solution_hypothesis": clean(idea["solution_hypothesis"]),
            "text": row["text"],
            "text_hash": row["text_hash"],
            "image_query": clean(idea.get("image_query") or idea["niche"]),
            "research": {
                "query": clean(signal.get("query") or idea.get("research_query") or idea["niche"]),
                "score": row["score"],
                "hits": signal.get("hits", [])[:5],
                "error": signal.get("error"),
            },
            "status": "planned",
        })

    plan = {
        "date_ist": today,
        "prepared_at_ist": now_ist.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "research_window_days": RESEARCH_DAYS,
        "research_source": "Hacker News Algolia Search API",
        "posts": posts,
    }
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    PLAN_PATH.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_queue_report(plan)
    write_engagement_shortlist(plan)
    print("Prepared daily plan for " + today + " with topics: " + ", ".join(post["idea_id"] for post in posts))
    print("The research score helps prioritise discussion activity; it does not establish market demand.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
