from __future__ import annotations

import copy
import hashlib
import sys
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from prepare_multidomain_plan import (
    MULTIDOMAIN_PLAN_SOURCE,
    ReportRejected,
    invalidate_current_plan,
    validate_report,
)

IST = ZoneInfo("Asia/Kolkata")
SOURCE_URL = "https://example.com/changelog/store-location-tools"


def valid_report(now: datetime) -> dict:
    generated = now - timedelta(minutes=6)
    post_text = (
        "A source-backed workflow idea: verify location results against known coordinates. "
        + SOURCE_URL
    )
    editor = {
        "clarity_score": 8,
        "technical_coherence_score": 8,
        "takeaway_value_score": 8,
        "source_faithfulness_score": 8,
        "originality_score": 8,
        "passed": True,
        "reason": "Clear, grounded, and useful.",
    }
    return {
        "generated_at_ist": generated.isoformat(timespec="seconds"),
        "mode": "hourly_dry_run_only",
        "outcome": "dry_run_passed",
        "posted_to_x": False,
        "star_tracking": {"repositories_with_20_to_36_hour_baseline": 19},
        "editorial_review": {
            "submitted_for_independent_review": 1,
            "passed_independent_review": 1,
            "review_error": None,
        },
        "recommended_draft": {
            "candidate_id": "candidate-abc123",
            "title": "Store location tools",
            "category": "commerce_and_digital_products",
            "url": SOURCE_URL,
            "primary_source_final_url": SOURCE_URL,
            "primary_source_verified": True,
            "primary_source_http_status": 200,
            "post_text": post_text,
            "character_count": len(post_text),
            "editorial_takeaway": "Verify distance results against known coordinates.",
            "evidence_quote": "The source lists the store-location search and lookup tools.",
            "claim_evidence": [{
                "claim": "The source describes store-location search and lookup.",
                "quote": "The source lists the store-location search and lookup tools.",
            }],
            "scores": {
                "timeliness": 8,
                "usefulness": 8,
                "novelty": 7,
                "evidence": 9,
                "insight": 8,
            },
            "editorial_score": 8.1,
            "status": "dry_run_passed_not_published",
            "published_to_x": False,
            "editorial_review": editor,
        },
    }


class MultidomainPlanValidationTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 10, 23, 11, 36, tzinfo=IST)
        self.report = valid_report(self.now)

    def test_passed_report_becomes_a_single_slot_plan(self):
        plan = validate_report(self.report, 1, now=self.now)
        self.assertEqual(plan["research_source"], MULTIDOMAIN_PLAN_SOURCE)
        self.assertEqual(plan["date_ist"], "2026-10-23")
        self.assertEqual(plan["source_report_age_minutes"], 6)
        self.assertEqual(len(plan["posts"]), 1)
        post = plan["posts"][0]
        self.assertEqual(post["slot"], 1)
        self.assertEqual(post["text"], self.report["recommended_draft"]["post_text"])
        self.assertEqual(post["text_hash"], hashlib.sha256(post["text"].encode()).hexdigest())
        self.assertEqual(post["image_query"], "")
        self.assertEqual(plan["star_baseline_repositories"], 19)

    def test_stale_report_is_rejected(self):
        report = copy.deepcopy(self.report)
        report["generated_at_ist"] = (self.now - timedelta(minutes=91)).isoformat()
        with self.assertRaisesRegex(ReportRejected, "stale"):
            validate_report(report, 0, now=self.now)

    def test_skip_outcome_is_rejected(self):
        report = copy.deepcopy(self.report)
        report["outcome"] = "skip"
        with self.assertRaisesRegex(ReportRejected, "did not pass"):
            validate_report(report, 0, now=self.now)

    def test_report_that_claims_to_have_published_is_rejected(self):
        report = copy.deepcopy(self.report)
        report["posted_to_x"] = True
        with self.assertRaisesRegex(ReportRejected, "dry-run mode"):
            validate_report(report, 0, now=self.now)

    def test_missing_star_baseline_is_rejected(self):
        report = copy.deepcopy(self.report)
        report["star_tracking"]["repositories_with_20_to_36_hour_baseline"] = 0
        with self.assertRaisesRegex(ReportRejected, "baseline"):
            validate_report(report, 0, now=self.now)

    def test_unverified_primary_source_is_rejected(self):
        report = copy.deepcopy(self.report)
        report["recommended_draft"]["primary_source_verified"] = False
        with self.assertRaisesRegex(ReportRejected, "verified primary source"):
            validate_report(report, 0, now=self.now)

    def test_non_https_source_is_rejected(self):
        report = copy.deepcopy(self.report)
        draft = report["recommended_draft"]
        draft["url"] = "http://example.com/changelog/store-location-tools"
        draft["primary_source_final_url"] = draft["url"]
        draft["post_text"] = draft["post_text"].replace(SOURCE_URL, draft["url"])
        draft["character_count"] = len(draft["post_text"])
        with self.assertRaisesRegex(ReportRejected, "invalid source URL"):
            validate_report(report, 0, now=self.now)

    def test_extra_or_wrong_url_is_rejected(self):
        report = copy.deepcopy(self.report)
        draft = report["recommended_draft"]
        draft["post_text"] = draft["post_text"].replace(
            SOURCE_URL, "https://example.org/unrelated"
        )
        draft["character_count"] = len(draft["post_text"])
        with self.assertRaisesRegex(ReportRejected, "exactly its own verified"):
            validate_report(report, 0, now=self.now)

    def test_overlength_post_is_rejected(self):
        report = copy.deepcopy(self.report)
        draft = report["recommended_draft"]
        draft["post_text"] = "x" * 281
        draft["character_count"] = 281
        with self.assertRaisesRegex(ReportRejected, "too long"):
            validate_report(report, 0, now=self.now)

    def test_independent_editor_must_pass_and_meet_score_threshold(self):
        report = copy.deepcopy(self.report)
        report["recommended_draft"]["editorial_review"]["passed"] = False
        with self.assertRaisesRegex(ReportRejected, "did not pass"):
            validate_report(report, 0, now=self.now)
        report = copy.deepcopy(self.report)
        report["recommended_draft"]["editorial_review"]["originality_score"] = 6
        with self.assertRaisesRegex(ReportRejected, "below 7"):
            validate_report(report, 0, now=self.now)

    def test_today_plan_is_invalidated_after_rejection(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "daily-plan.json"
            path.write_text('{"date_ist":"2026-10-23","posts":[{"text":"old copy"}]}')
            invalidate_current_plan(path, self.now)
            self.assertFalse(path.exists())

    def test_plan_for_another_date_is_not_removed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "daily-plan.json"
            path.write_text('{"date_ist":"2026-10-22","posts":[{"text":"prior-day copy"}]}')
            invalidate_current_plan(path, self.now)
            self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
