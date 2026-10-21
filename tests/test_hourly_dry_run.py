import json
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import discover_candidates as discovery
import hourly_dry_run as hourly


class HourlyDryRunTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 10, 21, 12, 0, tzinfo=timezone.utc)
        self.candidate = {
            "id": "candidate-1",
            "title": "Hookdeck webhook integration skills for coding agents",
            "source": "GitHub Search",
            "source_kind": "github_repository",
            "url": "https://github.com/hookdeck/webhook-skills",
            "canonical_url": "https://github.com/hookdeck/webhook-skills",
            "summary": (
                "Webhook integration skills for AI coding agents. Step-by-step guidance for setting up "
                "webhook receivers, signature verification, and event handling for Stripe, Shopify, GitHub, and more."
            ),
            "primary_category": "commerce_and_digital_products",
            "categories": ["commerce_and_digital_products"],
            "priority_score": 88,
            "days_old": 0.1,
            "published_at": "2026-10-21T11:00:00+00:00",
            "verification_status": "needs_primary_source_review",
            "evidence_urls": ["https://github.com/hookdeck/webhook-skills"],
            "signals": {"license_spdx": "MIT", "stars": 92},
        }

    def test_valid_draft_passes_and_is_marked_for_human_review(self):
        draft = {
            "candidate_id": "candidate-1",
            "post_text": (
                "Hookdeck's webhook integration skills: step-by-step guidance for receivers, signature "
                "verification and event handling for coding agents. For webhook receivers, add tests for invalid "
                "signatures and duplicate events before shipping. https://github.com/hookdeck/webhook-skills"
            ),
            "format": "tool_discovery",
            "audience": "developers building integrations",
            "angle": "safer webhook setup",
            "editorial_takeaway": "For webhook receivers, add tests for invalid signatures and duplicate events before shipping.",
            "evidence_quote": "signature verification, and event handling",
            "claim_evidence": [
                {
                    "claim": "The project has webhook integration skills for coding agents",
                    "quote": "Hookdeck webhook integration skills for coding agents",
                },
                {
                    "claim": "The skills provide step-by-step guidance for webhook receivers, signature verification and event handling",
                    "quote": "Step-by-step guidance for setting up webhook receivers, signature verification, and event handling",
                },
            ],
            "rationale": "The post turns the source into a concrete validation step rather than a product announcement.",
            "scores": {"timeliness": 7, "usefulness": 8, "novelty": 7, "evidence": 8, "insight": 8},
        }
        accepted, reasons = hourly.validate_draft(draft, {"candidate-1": self.candidate})
        self.assertEqual(reasons, [])
        self.assertIsNotNone(accepted)
        self.assertLessEqual(accepted["character_count"], 280)
        self.assertFalse(accepted["published_to_x"])
        self.assertEqual(accepted["status"], "draft_passed_needs_human_review")

    def test_helper_preserves_copy_and_only_moves_source_url_to_end(self):
        draft = {
            "candidate_id": "candidate-1",
            "post_text": (
                "Hookdeck's webhook skills guide receiver setup. "
                "For webhook receivers, add tests for invalid signatures before shipping. "
                "https://github.com/hookdeck/webhook-skills"
            ),
            "editorial_takeaway": "For webhook receivers, add tests for invalid signatures before shipping.",
        }
        updated = hourly.ensure_editorial_context(draft, self.candidate)
        self.assertTrue(updated["post_text"].endswith(self.candidate["url"]))
        self.assertIn(draft["editorial_takeaway"], updated["post_text"])
        self.assertEqual(updated["editorial_takeaway"], draft["editorial_takeaway"])

    def test_helper_does_not_invent_generic_audience_context(self):
        draft = {
            "candidate_id": "candidate-1",
            "post_text": (
                "Hookdeck's webhook skills guide receiver setup. "
                "For webhook receivers, add tests for invalid signatures before shipping. "
                "https://github.com/hookdeck/webhook-skills"
            ),
        }
        updated = hourly.ensure_editorial_context(draft, self.candidate)
        self.assertNotIn("Useful if you build for online merchants.", updated["post_text"])
        self.assertIn("add tests for invalid signatures", updated["post_text"])

    def test_feature_list_without_separate_use_case_is_rejected(self):
        draft = {
            "candidate_id": "candidate-1",
            "post_text": (
                "Hookdeck's webhook integration skills guide coding agents through receiver setup, signature verification "
                "and event handling. https://github.com/hookdeck/webhook-skills"
            ),
            "evidence_quote": "signature verification, and event handling",
            "claim_evidence": [
                {
                    "claim": "Hookdeck webhook integration skills guide coding agents",
                    "quote": "Hookdeck webhook integration skills for coding agents",
                },
                {
                    "claim": "Guidance covers webhook receivers, signature verification and event handling",
                    "quote": "webhook receivers, signature verification, and event handling",
                },
            ],
            "scores": {"timeliness": 7, "usefulness": 8, "novelty": 7, "evidence": 8},
        }
        accepted, reasons = hourly.validate_draft(draft, {"candidate-1": self.candidate})
        self.assertIsNone(accepted)
        self.assertTrue(any("headline" in reason or "editorial_takeaway" in reason for reason in reasons))

    def test_generic_audience_suffix_is_not_accepted_as_editorial_insight(self):
        draft = {
            "candidate_id": "candidate-1",
            "post_text": (
                "Hookdeck's webhook integration skills support receiver setup and signature verification. "
                "Useful if you're building apps. https://github.com/hookdeck/webhook-skills"
            ),
            "editorial_takeaway": "Useful if you're building apps.",
            "evidence_quote": "signature verification, and event handling",
            "claim_evidence": [
                {
                    "claim": "The project has webhook integration skills for coding agents",
                    "quote": "Hookdeck webhook integration skills for coding agents",
                }
            ],
            "scores": {"timeliness": 8, "usefulness": 8, "novelty": 8, "evidence": 8, "insight": 8},
        }
        accepted, reasons = hourly.validate_draft(draft, {"candidate-1": self.candidate})
        self.assertIsNone(accepted)
        self.assertTrue(any("Generic audience-only advice" in reason or "actionable" in reason or "too generic" in reason for reason in reasons))

    def test_headline_rewrite_is_rejected_even_when_it_has_a_generic_second_sentence(self):
        draft = {
            "candidate_id": "candidate-1",
            "post_text": (
                "Hookdeck webhook integration skills for coding agents. "
                "For webhook receivers, add tests for invalid signatures before shipping. "
                "https://github.com/hookdeck/webhook-skills"
            ),
            "editorial_takeaway": "For webhook receivers, add tests for invalid signatures before shipping.",
            "evidence_quote": "signature verification, and event handling",
            "claim_evidence": [
                {
                    "claim": "The project has webhook integration skills for coding agents",
                    "quote": "Hookdeck webhook integration skills for coding agents",
                }
            ],
            "scores": {"timeliness": 8, "usefulness": 8, "novelty": 8, "evidence": 8, "insight": 8},
        }
        accepted, reasons = hourly.validate_draft(draft, {"candidate-1": self.candidate})
        self.assertIsNone(accepted)
        self.assertTrue(any("source headline" in reason for reason in reasons))

    def test_draft_without_source_url_is_rejected(self):
        draft = {
            "candidate_id": "candidate-1",
            "post_text": "A useful workflow for webhook integration.",
            "evidence_quote": "signature verification, and event handling",
            "scores": {"timeliness": 7, "usefulness": 8, "novelty": 7, "evidence": 8},
        }
        accepted, reasons = hourly.validate_draft(draft, {"candidate-1": self.candidate})
        self.assertIsNone(accepted)
        self.assertTrue(any("primary candidate URL" in reason for reason in reasons))

    def test_unverifiable_marketing_superlative_is_rejected(self):
        draft = {
            "candidate_id": "candidate-1",
            "post_text": (
                "The tool everyone uses for webhook delivery. Useful if you're building provider integrations. "
                "https://github.com/hookdeck/webhook-skills"
            ),
            "evidence_quote": "signature verification, and event handling",
            "claim_evidence": [
                {
                    "claim": "Webhook integration skills provide signature verification and event handling",
                    "quote": "webhook receivers, signature verification, and event handling",
                }
            ],
            "scores": {"timeliness": 7, "usefulness": 8, "novelty": 7, "evidence": 8},
        }
        accepted, reasons = hourly.validate_draft(draft, {"candidate-1": self.candidate})
        self.assertIsNone(accepted)
        self.assertTrue(any("Unverifiable marketing language" in reason for reason in reasons))

    def test_draft_with_unsupported_numeric_claim_is_rejected(self):
        draft = {
            "candidate_id": "candidate-1",
            "post_text": (
                "This makes webhook integration 10x faster for every team. "
                "https://github.com/hookdeck/webhook-skills"
            ),
            "evidence_quote": "signature verification, and event handling",
            "scores": {"timeliness": 7, "usefulness": 8, "novelty": 7, "evidence": 8},
        }
        accepted, reasons = hourly.validate_draft(draft, {"candidate-1": self.candidate})
        self.assertIsNone(accepted)
        self.assertTrue(any("Unsupported numeric claim" in reason for reason in reasons))

    def test_draft_with_unsupported_feature_terms_is_rejected(self):
        draft = {
            "candidate_id": "candidate-1",
            "post_text": (
                "Hookdeck's webhook skills add a real-time custom analytics dashboard and guaranteed fraud prevention "
                "for Shopify and Stripe. Useful if you're auditing a store. "
                "https://github.com/hookdeck/webhook-skills"
            ),
            "evidence_quote": "signature verification, and event handling",
            "claim_evidence": [
                {
                    "claim": "The guidance covers signature verification",
                    "quote": "signature verification, and event handling",
                }
            ],
            "scores": {"timeliness": 7, "usefulness": 8, "novelty": 7, "evidence": 8},
        }
        accepted, reasons = hourly.validate_draft(draft, {"candidate-1": self.candidate})
        self.assertIsNone(accepted)
        self.assertTrue(any("Factual sentence includes terms absent" in reason for reason in reasons))

    def test_diversity_rank_excludes_recently_used_candidate(self):
        state = hourly.empty_state()
        state["used_candidates"]["candidate-1"] = self.now.isoformat()
        result = hourly.diversity_rank([self.candidate], state, self.now)
        self.assertEqual(result, [])

    def test_diversity_rank_respects_per_category_cap(self):
        state = hourly.empty_state()
        for index in range(hourly.MAX_PER_CATEGORY_PER_DAY):
            state["events"].append({
                "timestamp_utc": (self.now - timedelta(hours=index + 1)).isoformat(),
                "status": "draft_passed",
                "source_group": "Some other source",
                "category": "commerce_and_digital_products",
                "title": "Different previous title " + str(index),
            })
        result = hourly.diversity_rank([self.candidate], state, self.now)
        self.assertEqual(result, [])

    def test_diversified_shortlist_limits_single_source_and_category(self):
        candidates = []
        specs = [
            ("g1", "GitHub Search", "ai_and_automation"),
            ("g2", "GitHub Search", "ai_and_automation"),
            ("g3", "GitHub Search", "ai_and_automation"),
            ("g4", "GitHub Search", "commerce_and_digital_products"),
            ("hn1", "Hacker News", "commerce_and_digital_products"),
            ("ph1", "Product Hunt", "data_and_growth"),
            ("shop1", "Shopify Developer Changelog", "security_and_self_hosting"),
            ("console1", "Console.dev", "developer_tools"),
        ]
        for index, (cid, source, category) in enumerate(specs):
            candidates.append({
                "id": cid,
                "title": "Distinct useful technical project " + cid,
                "source": source,
                "primary_category": category,
                "priority_score": 100 - index,
                "hourly_adjusted_score": 100 - index,
            })
        selected = hourly.diversified_shortlist(candidates, 5)
        self.assertEqual(len(selected), 5)
        source_groups = [
            "GitHub Search" if item["source"].startswith("GitHub Search") else item["source"]
            for item in selected
        ]
        self.assertLessEqual(source_groups.count("GitHub Search"), 2)
        self.assertLessEqual(
            max(__import__("collections").Counter(item["primary_category"] for item in selected).values()),
            2,
        )
        self.assertGreaterEqual(len(set(item["primary_category"] for item in selected)), 3)

    def test_freshness_window_uses_source_specific_rules(self):
        current = dict(self.candidate, source="GitHub Search", days_old=2.5)
        stale_repo = dict(self.candidate, source="GitHub Search", days_old=4.0)
        weekly = dict(self.candidate, source="Console.dev", days_old=8.0)
        self.assertTrue(hourly.is_fresh(current, 3))
        self.assertFalse(hourly.is_fresh(stale_repo, 3))
        self.assertTrue(hourly.is_fresh(weekly, 14))
        self.assertTrue(hourly.is_fresh(weekly, 7))

    def test_github_star_velocity_requires_persisted_20_to_36_hour_baseline(self):
        state = hourly.empty_state()
        candidate = dict(self.candidate)
        candidate["source_kind"] = "github_repository"
        candidate["signals"] = {"stars": 100}
        hourly.update_github_star_velocity([candidate], state, self.now)
        self.assertIsNone(candidate.get("stars_delta_24h"))
        self.assertEqual(len(state["repo_star_snapshots"]["candidate-1"]), 1)

        candidate["signals"]["stars"] = 120
        later = self.now + timedelta(hours=24)
        hourly.update_github_star_velocity([candidate], state, later)
        self.assertEqual(candidate["stars_delta_24h"], 20)
        self.assertEqual(candidate["stars_delta_baseline_hours"], 24.0)
        self.assertEqual(candidate["stars_growth_percent_24h"], 20.0)
        self.assertEqual(len(state["repo_star_snapshots"]["candidate-1"]), 2)

    def test_star_velocity_uses_recent_baseline_and_does_not_claim_negative_growth(self):
        state = hourly.empty_state()
        candidate = dict(self.candidate)
        candidate["source_kind"] = "github_repository"
        candidate["signals"] = {"stars": 100}
        hourly.update_github_star_velocity([candidate], state, self.now)

        candidate["signals"]["stars"] = 98
        later = self.now + timedelta(hours=23)
        hourly.update_github_star_velocity([candidate], state, later)
        self.assertEqual(candidate["stars_delta_24h"], 0)
        self.assertEqual(candidate["stars_growth_percent_24h"], 0.0)

    def test_non_github_candidates_are_not_labelled_with_star_trend(self):
        candidate = dict(self.candidate)
        candidate["source"] = "Shopify Developer Changelog"
        candidate["source_kind"] = "official_changelog"
        candidate["url"] = "https://shopify.dev/changelog/sample"
        candidate["canonical_url"] = candidate["url"]
        candidate["signals"] = {}
        state = hourly.empty_state()
        ranked = hourly.diversity_rank([candidate], state, self.now, lookback_days=1)
        self.assertEqual(len(ranked), 1)
        self.assertEqual(ranked[0]["trend_signal"], "not_applicable")
        self.assertLessEqual(ranked[0]["hourly_adjusted_score"] - ranked[0]["priority_score"], 4)

    def test_daily_caps_use_india_calendar_day_not_rolling_24_hours(self):
        state = hourly.empty_state()
        state["events"] = [
            {
                "run_at_ist": "2026-10-20T23:55:00+05:30",
                "timestamp_utc": "2026-10-20T18:25:00+00:00",
                "status": "draft_passed",
            },
            {
                "run_at_ist": "2026-10-21T08:05:00+05:30",
                "timestamp_utc": "2026-10-21T02:35:00+00:00",
                "status": "draft_passed",
            },
        ]
        today = hourly.events_today(state, self.now)
        self.assertEqual(len(today), 1)
        self.assertEqual(today[0]["run_at_ist"], "2026-10-21T08:05:00+05:30")

    def test_state_loader_fails_closed_on_corrupt_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "hourly-state.json"
            path.write_text("{broken", encoding="utf-8")
            original = hourly.STATE_PATH
            hourly.STATE_PATH = path
            try:
                with self.assertRaises(RuntimeError):
                    hourly.load_state()
            finally:
                hourly.STATE_PATH = original

    def test_hourly_report_is_explicitly_dry_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = (hourly.OUT, hourly.LATEST_JSON_PATH, hourly.LATEST_MD_PATH)
            hourly.OUT = Path(tmp)
            hourly.LATEST_JSON_PATH = Path(tmp) / "hourly-latest.json"
            hourly.LATEST_MD_PATH = Path(tmp) / "hourly-latest.md"
            try:
                report = {
                    "run_at_ist": "2026-10-21T17:30:00+05:30",
                    "mode": "hourly_dry_run_only",
                    "eligible_candidate_count": 0,
                    "source_diagnostics": [],
                    "outcome": "skip",
                    "decision_reason": "No candidate passed.",
                    "passing_drafts": [],
                    "rejected_drafts": [],
                    "candidate_shortlist": [],
                }
                hourly.write_outputs(report)
                payload = json.loads(hourly.LATEST_JSON_PATH.read_text(encoding="utf-8"))
                md = hourly.LATEST_MD_PATH.read_text(encoding="utf-8")
                self.assertFalse(payload["posted_to_x"])
                self.assertIn("not performed", md)
                self.assertIn("skip", md)
            finally:
                hourly.OUT, hourly.LATEST_JSON_PATH, hourly.LATEST_MD_PATH = original


if __name__ == "__main__":
    unittest.main()
