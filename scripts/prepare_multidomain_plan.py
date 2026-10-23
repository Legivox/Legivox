#!/usr/bin/env python3
"""Convert the latest quality-gated multidomain report into a single-slot plan.

This script prepares a plan only. It never accesses X credentials or publishes.
An absent, stale, incomplete, or failed report invalidates today's previous plan
so the live workflow can skip this slot instead of falling back to older copy.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo

from plan_sources import MULTIDOMAIN_PLAN_SOURCE

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPORT = ROOT / "output" / "discovery" / "hourly-latest.json"
DEFAULT_PLAN = ROOT / "output" / "daily-plan.json"
IST = ZoneInfo("Asia/Kolkata")
REQUIRED_EDITOR_SCORES = (
    "clarity_score",
    "technical_coherence_score",
    "takeaway_value_score",
    "source_faithfulness_score",
    "originality_score",
)
URL_RE = re.compile(r"https://[^\s]+")


class ReportRejected(ValueError):
    """The latest discovery result is not safe to pass to the publishing workflow."""


def clean(value: object) -> str:
    return " ".join(str(value or "").split()).strip()


def as_aware_datetime(value: object, field: str) -> datetime:
    raw = clean(value)
    if not raw:
        raise ReportRejected(f"Report is missing {field}.")
    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ReportRejected(f"Report has invalid {field}.") from exc
    if parsed.tzinfo is None:
        raise ReportRejected(f"Report {field} must include a timezone.")
    return parsed


def current_ist(now: datetime | None = None) -> datetime:
    now = now or datetime.now(IST)
    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    return now.astimezone(IST)


def validate_report(
    report: object,
    slot: int,
    *,
    now: datetime | None = None,
    max_age_minutes: int = 90,
) -> dict:
    """Validate freshness, provenance, quality-gate and post shape before handoff."""
    if not isinstance(report, dict):
        raise ReportRejected("Latest discovery report is not a JSON object.")
    if max_age_minutes < 1:
        raise ValueError("max_age_minutes must be positive")
    if slot not in (0, 1, 2):
        raise ValueError("slot must be 0, 1, or 2")

    if report.get("mode") != "hourly_dry_run_only":
        raise ReportRejected("Report did not come from the research-only workflow.")
    if report.get("outcome") != "dry_run_passed":
        raise ReportRejected("Latest research run did not pass its complete quality gate.")
    if report.get("posted_to_x") is not False:
        raise ReportRejected("Report does not prove that it remained in dry-run mode.")

    current = current_ist(now)
    generated = as_aware_datetime(report.get("generated_at_ist"), "generated_at_ist").astimezone(IST)
    age = current - generated
    if age < timedelta(minutes=-5):
        raise ReportRejected("Latest discovery report is timestamped too far in the future.")
    if age > timedelta(minutes=max_age_minutes):
        raise ReportRejected(
            f"Latest discovery report is stale ({int(age.total_seconds() // 60)} minutes old; "
            f"maximum is {max_age_minutes})."
        )

    star_tracking = report.get("star_tracking")
    if not isinstance(star_tracking, dict):
        raise ReportRejected("Report is missing GitHub star-history status.")
    try:
        baseline_count = int(star_tracking.get("repositories_with_20_to_36_hour_baseline", 0))
    except (TypeError, ValueError) as exc:
        raise ReportRejected("Report has invalid star-history baseline count.") from exc
    if baseline_count < 1:
        raise ReportRejected("No valid 20–36-hour GitHub star-history baseline is available yet.")

    review_summary = report.get("editorial_review")
    if (
        not isinstance(review_summary, dict)
        or int(review_summary.get("submitted_for_independent_review", 0) or 0) < 1
        or int(review_summary.get("passed_independent_review", 0) or 0) < 1
        or review_summary.get("review_error")
    ):
        raise ReportRejected("Independent editorial review did not succeed.")

    draft = report.get("recommended_draft")
    if not isinstance(draft, dict):
        raise ReportRejected("Passing report has no recommended draft.")
    if draft.get("status") != "dry_run_passed_not_published" or draft.get("published_to_x") is not False:
        raise ReportRejected("Recommended draft does not have the expected unpublished dry-run status.")
    if draft.get("primary_source_verified") is not True:
        raise ReportRejected("Recommended draft has no verified primary source.")
    try:
        source_status = int(draft.get("primary_source_http_status", 0))
    except (TypeError, ValueError) as exc:
        raise ReportRejected("Recommended draft has an invalid primary-source status.") from exc
    if not 200 <= source_status < 300:
        raise ReportRejected("Recommended draft's primary source did not return a successful HTTP status.")

    title = clean(draft.get("title"))
    candidate_id = clean(draft.get("candidate_id"))
    category = clean(draft.get("category"))
    post_text = clean(draft.get("post_text"))
    source_url = clean(draft.get("url"))
    final_url = clean(draft.get("primary_source_final_url") or source_url)
    angle = clean(draft.get("editorial_takeaway") or draft.get("angle"))
    evidence_quote = clean(draft.get("evidence_quote"))
    claim_evidence = draft.get("claim_evidence")
    if not all((title, candidate_id, category, post_text, source_url, final_url, angle, evidence_quote)):
        raise ReportRejected("Recommended draft is missing identity, source, text, angle, or evidence.")
    for value, name in ((source_url, "source URL"), (final_url, "final source URL")):
        parsed_url = urlsplit(value)
        if parsed_url.scheme != "https" or not parsed_url.netloc:
            raise ReportRejected(f"Recommended draft has an invalid {name}.")
    if source_url != final_url:
        raise ReportRejected("Draft URL differs from the URL verified by the primary-source check.")

    if len(post_text) > 280:
        raise ReportRejected(f"Post copy is too long ({len(post_text)} characters).")
    found_urls = URL_RE.findall(post_text)
    if found_urls != [source_url]:
        raise ReportRejected("Post copy must contain exactly its own verified primary-source URL.")
    if int(draft.get("character_count", -1)) != len(post_text):
        raise ReportRejected("Recorded character count does not match the proposed post text.")
    if not isinstance(claim_evidence, list) or not any(
        isinstance(item, dict) and clean(item.get("claim")) and clean(item.get("quote"))
        for item in claim_evidence
    ):
        raise ReportRejected("Recommended draft has no claim-by-claim source evidence.")

    scores = draft.get("scores")
    if not isinstance(scores, dict):
        raise ReportRejected("Recommended draft is missing model quality scores.")
    try:
        model_scores = [
            float(scores.get(name, 0))
            for name in ("timeliness", "usefulness", "novelty", "evidence", "insight")
        ]
        overall_score = float(draft.get("editorial_score", 0))
    except (TypeError, ValueError) as exc:
        raise ReportRejected("Recommended draft contains invalid model quality scores.") from exc
    if any(score < 7 for score in model_scores):
        raise ReportRejected("At least one model quality score is below 7/10.")
    if overall_score < 7:
        raise ReportRejected("Overall editorial score is below 7/10.")

    editor = draft.get("editorial_review")
    if not isinstance(editor, dict) or editor.get("passed") is not True:
        raise ReportRejected("Recommended draft did not pass the independent editorial review.")
    try:
        editor_scores = [float(editor.get(name, 0)) for name in REQUIRED_EDITOR_SCORES]
    except (TypeError, ValueError) as exc:
        raise ReportRejected("Recommended draft contains invalid independent editor scores.") from exc
    if any(score < 7 for score in editor_scores):
        raise ReportRejected("At least one independent editor score is below 7/10.")

    idea_id = "multidomain-" + candidate_id
    research_score = round(float(draft["editorial_score"]), 2)
    prepared_at = current.strftime("%Y-%m-%d %H:%M:%S %Z")
    plan_post = {
        "idea_id": idea_id,
        "niche": category,
        "problem": title,
        "evidence": (
            f"Primary source verified (HTTP {source_status}): {source_url}. "
            f"Exact evidence: {evidence_quote}"
        ),
        "solution_hypothesis": angle,
        "text": post_text,
        "text_hash": hashlib.sha256(post_text.encode("utf-8")).hexdigest(),
        "image_query": "",
        "research": {
            "query": "Multidomain primary-source discovery and independent editorial review",
            "score": research_score,
            "hits": [{
                "title": title,
                "url": source_url,
                "external_url": source_url,
                "points": 0,
                "comments": 0,
                "created_at": clean(draft.get("published_at") or report.get("generated_at_ist")),
                "matched_terms": [],
            }],
            "error": None,
        },
        "status": "planned",
        "slot": slot,
        "editorial_scores": {
            "model": scores,
            "overall": research_score,
            "independent_review": editor,
        },
    }
    return {
        "date_ist": current.date().isoformat(),
        "prepared_at_ist": prepared_at,
        "research_window_days": 1,
        "research_source": MULTIDOMAIN_PLAN_SOURCE,
        "source_report_generated_at_ist": generated.isoformat(timespec="seconds"),
        "source_report_age_minutes": max(0, int(age.total_seconds() // 60)),
        "star_baseline_repositories": baseline_count,
        "posts": [plan_post],
    }


def invalidate_current_plan(path: Path, now: datetime | None = None) -> None:
    """Remove today's existing plan after a rejection to prevent unsafe fallback."""
    if not path.exists():
        return
    current_date = current_ist(now).date().isoformat()
    try:
        previous = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        path.unlink(missing_ok=True)
        return
    if isinstance(previous, dict) and previous.get("date_ist") == current_date:
        path.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=str(DEFAULT_REPORT), help="Latest JSON report from the state branch.")
    parser.add_argument("--output", default=str(DEFAULT_PLAN), help="Daily plan path consumed by the existing publisher.")
    parser.add_argument("--slot", type=int, required=True, choices=(0, 1, 2))
    parser.add_argument("--max-age-minutes", type=int, default=90)
    args = parser.parse_args(argv)
    report_path = Path(args.input)
    plan_path = Path(args.output)
    now = datetime.now(IST)

    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
        plan = validate_report(report, args.slot, now=now, max_age_minutes=args.max_age_minutes)
    except (OSError, json.JSONDecodeError, ReportRejected, ValueError) as exc:
        invalidate_current_plan(plan_path, now)
        print(f"Multidomain preparation skipped safely: {exc}", file=sys.stderr)
        return 2

    plan_path.parent.mkdir(parents=True, exist_ok=True)
    plan_path.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Prepared one multidomain source-grounded post for slot " + str(args.slot) + ".")
    print("Source report generated at: " + plan["source_report_generated_at_ist"])
    print("Post characters including source URL: " + str(len(plan["posts"][0]["text"])) + "/280")
    print("No X publishing was attempted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
