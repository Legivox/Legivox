#!/usr/bin/env python3
"""Publish one curated Legivox post; never print or persist the X session cookie."""
from __future__ import annotations
import hashlib, json, os, sys
from datetime import datetime, timezone
from pathlib import Path
from tweetkit_x import TweetKit

ROOT = Path(__file__).resolve().parents[1]
IDEAS_PATH = ROOT / "data" / "ideas.json"
OUTPUT_DIR = ROOT / "output"
STATE_PATH = OUTPUT_DIR / "queue-state.json"
REPORT_PATH = OUTPUT_DIR / "content-queue.md"
PUBLISHED_PATH = OUTPUT_DIR / "published.jsonl"
EXPECTED_USERNAME = "Legivox"

def fail(message: str) -> None:
    print("Legivox publisher: " + message, file=sys.stderr)
    raise SystemExit(1)

def clean(value: str) -> str:
    return " ".join(str(value).split())

def write_state(state: dict) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")

def write_report(item: dict, draft: str, message: str, result: dict | None = None) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Legivox content queue", "", "Generated: " + now, "",
        "> Individually written drafts. Research records are hypotheses unless source links and evidence are added.", "",
        "## Latest post draft", "", draft, "",
        "## Research record", "",
        "- Niche: " + clean(item["niche"]),
        "- Problem: " + clean(item["problem"]),
        "- Evidence status: " + clean(item["evidence"]),
        "- Product hypothesis: " + clean(item["solution_hypothesis"]),
        "- Idea ID: " + clean(item["id"]),
        "- Result: " + message,
    ]
    if result and result.get("url"):
        lines += ["- Published URL: " + result["url"]]
    lines += ["", "## Publishing scope", "",
        "One original standalone post only. No replies, likes, follows, reposts, or DMs.",
        "Only publish_text from data/ideas.json is eligible; the publisher does not create public copy from research labels.", ""]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")

def main() -> int:
    cookie = os.environ.get("TWEETKIT_COOKIE", "").strip()
    if not cookie:
        fail("Missing Actions secret X_SESSION_COOKIE. Add it in repository Settings > Secrets and variables > Actions.")
    try:
        client = TweetKit(cookie=cookie, timeout=25)
        identity = client.whoami()
    except Exception:
        fail("Could not initialise the X session. Check that the cookie secret contains auth_token, ct0, and twid; details suppressed.")
    if not identity.get("ready") or not identity.get("user_id"):
        fail("Session cookie is incomplete. A valid auth_token, ct0, and twid are required; details suppressed.")
    try:
        profile = client.user_profile(EXPECTED_USERNAME)
    except Exception:
        fail("Could not verify the @Legivox X profile. No post was attempted.")
    if not profile.get("ok") or str(profile.get("username", "")).lower() != EXPECTED_USERNAME.lower():
        fail("Could not verify the public @Legivox profile. No post was attempted.")
    if str(identity.get("user_id")) != str(profile.get("id")):
        fail("The cookie belongs to a different X account, not @Legivox. No post was attempted.")

    try:
        ideas = json.loads(IDEAS_PATH.read_text(encoding="utf-8"))
        state = json.loads(STATE_PATH.read_text(encoding="utf-8")) if STATE_PATH.exists() else {}
    except Exception:
        fail("Could not read the idea queue or state JSON.")
    required = ("id", "niche", "problem", "evidence", "solution_hypothesis", "publish_text")
    ideas = [row for row in ideas if isinstance(row, dict) and all(row.get(key) for key in required)]
    if not ideas:
        fail("No curated posts found. Add publish_text to a reviewed entry in data/ideas.json.")
    for item in ideas:
        item["publish_text"] = clean(item["publish_text"])
        if not item["publish_text"] or len(item["publish_text"]) > 280:
            fail("Every publish_text must contain 1-280 characters. Fix the queue before publishing.")

    try:
        recent = client.get_tweets(limit=100, include_replies=False)
    except Exception:
        fail("Could not safely check recent @Legivox posts for duplicates. No post was attempted.")
    recent_texts = {clean(row.get("text", "")) for row in recent if row.get("text")}
    used_hashes = set(state.get("used_draft_hashes", []))
    last_id = state.get("last_idea_id")
    idea_ids = [row["id"] for row in ideas]
    last_index = idea_ids.index(last_id) if last_id in idea_ids else -1
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for step in range(1, len(ideas) + 1):
        item = ideas[(last_index + step) % len(ideas)]
        draft = item["publish_text"]
        digest = hashlib.sha256(draft.encode("utf-8")).hexdigest()
        if digest in used_hashes:
            continue
        if draft in recent_texts:
            used_hashes.add(digest)
            state.update({"last_idea_id": item["id"], "used_draft_hashes": sorted(used_hashes)})
            continue
        try:
            result = client.post(draft)
        except Exception:
            fail("The posting request failed. It was not retried to avoid accidental duplicate posts; check Actions logs and the X profile before retrying.")
        if not isinstance(result, dict) or not result.get("ok"):
            status = result.get("status") if isinstance(result, dict) else None
            fail("X did not confirm the post (HTTP status " + str(status or "unknown") + "). The request was not retried; check the profile before rerunning.")
        now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        used_hashes.add(digest)
        state.update({
            "last_idea_id": item["id"], "used_draft_hashes": sorted(used_hashes),
            "published_count": int(state.get("published_count", 0)) + 1,
            "last_published_at": now, "last_published_url": result.get("url", ""),
        })
        with PUBLISHED_PATH.open("a", encoding="utf-8") as out:
            out.write(json.dumps({"timestamp": now, "idea_id": item["id"], "text": draft,
                "tweet_id": result.get("id"), "url": result.get("url")}, ensure_ascii=False) + "\n")
        write_state(state)
        write_report(item, draft, "Published successfully", result)
        print("Published one curated original post for @Legivox: " + str(result.get("url", "URL unavailable")))
        print("Idea ID: " + str(item["id"]) + "; character count: " + str(len(draft)))
        return 0
    state["used_draft_hashes"] = sorted(used_hashes)
    write_state(state)
    fail("All curated posts have been used. Add new reviewed drafts to data/ideas.json before resuming.")

if __name__ == "__main__":
    raise SystemExit(main())
