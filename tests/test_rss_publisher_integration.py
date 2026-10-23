from __future__ import annotations

import sys
import unittest
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from publish_next import RSS_GROQ_PLAN_SOURCE, select_post_for_slot
from plan_sources import MULTIDOMAIN_PLAN_SOURCE
from randomized_slot import IST, choose_target, window_bounds


class PublisherPlanSelectionTests(unittest.TestCase):
    def test_selects_single_rss_post_only_for_its_matching_slot(self) -> None:
        plan = {
            "research_source": RSS_GROQ_PLAN_SOURCE,
            "posts": [{"slot": 1, "text": "Grounded source-led post"}],
        }
        self.assertEqual(
            select_post_for_slot(plan, 1)["text"],
            "Grounded source-led post",
        )

    def test_rss_post_cannot_be_published_in_a_different_slot(self) -> None:
        plan = {
            "research_source": RSS_GROQ_PLAN_SOURCE,
            "posts": [{"slot": 1, "text": "Grounded source-led post"}],
        }
        with self.assertRaisesRegex(ValueError, "slot does not match"):
            select_post_for_slot(plan, 2)

    def test_rss_plan_must_have_exactly_one_post(self) -> None:
        plan = {
            "research_source": RSS_GROQ_PLAN_SOURCE,
            "posts": [
                {"slot": 0, "text": "Post one"},
                {"slot": 0, "text": "Post two"},
            ],
        }
        with self.assertRaisesRegex(ValueError, "exactly one"):
            select_post_for_slot(plan, 0)

    def test_selects_single_multidomain_post_only_for_its_matching_slot(self) -> None:
        plan = {
            "research_source": MULTIDOMAIN_PLAN_SOURCE,
            "posts": [{"slot": 2, "text": "Verified multidomain post with source link"}],
        }
        self.assertEqual(
            select_post_for_slot(plan, 2)["text"],
            "Verified multidomain post with source link",
        )

    def test_multidomain_post_cannot_be_published_in_a_different_slot(self) -> None:
        plan = {
            "research_source": MULTIDOMAIN_PLAN_SOURCE,
            "posts": [{"slot": 1, "text": "Verified multidomain post"}],
        }
        with self.assertRaisesRegex(ValueError, "slot does not match"):
            select_post_for_slot(plan, 2)

    def test_multidomain_plan_must_have_exactly_one_post(self) -> None:
        plan = {
            "research_source": MULTIDOMAIN_PLAN_SOURCE,
            "posts": [
                {"slot": 0, "text": "Post one"},
                {"slot": 0, "text": "Post two"},
            ],
        }
        with self.assertRaisesRegex(ValueError, "exactly one"):
            select_post_for_slot(plan, 0)

    def test_legacy_curated_three_post_plan_still_works(self) -> None:
        plan = {"research_source": "Hacker News Algolia Search API",
                "posts": [{"text": "morning"}, {"text": "lunch"}, {"text": "evening"}]}
        self.assertEqual(select_post_for_slot(plan, 2)["text"], "evening")

    def test_empty_or_malformed_rss_post_is_rejected(self) -> None:
        plan = {
            "research_source": RSS_GROQ_PLAN_SOURCE,
            "posts": [{"slot": 0, "text": "  "}],
        }
        with self.assertRaisesRegex(ValueError, "empty post"):
            select_post_for_slot(plan, 0)


class RandomizedWindowTests(unittest.TestCase):
    def test_each_slot_has_a_one_hour_ist_window(self) -> None:
        now = datetime(2026, 10, 18, 8, 30, tzinfo=IST)
        expected_hours = {0: (9, 10), 1: (13, 14), 2: (19, 20)}
        for slot, (start_hour, end_hour) in expected_hours.items():
            start, end = window_bounds(now, slot)
            self.assertEqual((start.hour, end.hour), (start_hour, end_hour))
            self.assertEqual(end - start, timedelta(hours=1))

    def test_fixed_random_offset_targets_expected_minute(self) -> None:
        now = datetime(2026, 10, 18, 8, 45, tzinfo=IST)
        target = choose_target(now, 0, target_offset_seconds=20 * 60)
        self.assertEqual(target, datetime(2026, 10, 18, 9, 20, tzinfo=IST))

    def test_target_is_not_before_now_when_workflow_starts_late(self) -> None:
        now = datetime(2026, 10, 18, 9, 20, tzinfo=IST)
        target = choose_target(now, 0, target_offset_seconds=5 * 60)
        self.assertEqual(target, now)

    def test_expired_window_returns_no_target(self) -> None:
        now = datetime(2026, 10, 18, 10, 0, tzinfo=IST)
        self.assertIsNone(choose_target(now, 0))

    def test_random_target_stays_before_latest_target(self) -> None:
        now = datetime(2026, 10, 18, 13, 5, tzinfo=IST)
        start, end = window_bounds(now, 1)
        target = choose_target(now, 1)
        self.assertIsNotNone(target)
        self.assertGreaterEqual(target, now)
        self.assertLessEqual(target, start + timedelta(minutes=45))
        self.assertLess(target, end)

    def test_hourly_window_supports_last_slot_through_midnight(self) -> None:
        now = datetime(2026, 10, 18, 22, 30, tzinfo=IST)
        start, end = window_bounds(now, 0, hour=23)
        self.assertEqual(start, datetime(2026, 10, 18, 23, 0, tzinfo=IST))
        self.assertEqual(end, datetime(2026, 10, 19, 0, 0, tzinfo=IST))
        self.assertEqual(end - start, timedelta(hours=1))

    def test_hourly_target_uses_requested_ist_window(self) -> None:
        now = datetime(2026, 10, 18, 16, 5, tzinfo=IST)
        target = choose_target(now, 2, target_offset_seconds=10 * 60, hour=16)
        self.assertEqual(target, datetime(2026, 10, 18, 16, 10, tzinfo=IST))

    def test_hourly_window_rejects_hours_outside_production_schedule(self) -> None:
        now = datetime(2026, 10, 18, 8, 30, tzinfo=IST)
        with self.assertRaisesRegex(ValueError, "between 8 and 23"):
            window_bounds(now, 0, hour=7)


if __name__ == "__main__":
    unittest.main()
