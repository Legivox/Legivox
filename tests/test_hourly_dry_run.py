import json
import os
import urllib.error
from unittest.mock import patch
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
            "primary_source_verified": True,
            "primary_source_http_status": 200,
            "primary_source_title": "Hookdeck webhook integration skills for coding agents",
            "primary_source_evidence": "Webhook integration skills for AI coding agents. Step-by-step guidance for setting up webhook receivers, signature verification, and event handling for Stripe, Shopify, GitHub, and more.",
            "evidence_urls": ["https://github.com/hookdeck/webhook-skills"],
            "signals": {"license_spdx": "MIT", "stars": 92},
        }

    def test_editorial_review_queue_reviews_top_three_and_defers_only_lower_ranked(self):
        drafts = [
            {"candidate_id": "low", "editorial_score": 7.2, "hourly_adjusted_score": 95},
            {"candidate_id": "top", "editorial_score": 9.0, "hourly_adjusted_score": 60},
            {"candidate_id": "tie-low", "editorial_score": 8.0, "hourly_adjusted_score": 75},
            {"candidate_id": "tie-high", "editorial_score": 8.0, "hourly_adjusted_score": 80},
            {"candidate_id": "mid", "editorial_score": 7.7, "hourly_adjusted_score": 70},
        ]
        review_queue, deferred = hourly.split_editorial_review_queue(drafts, limit=3)
        self.assertEqual(
            [row["candidate_id"] for row in review_queue],
            ["top", "tie-high", "tie-low"],
        )
        self.assertEqual(
            [row["candidate_id"] for row in deferred],
            ["mid", "low"],
        )
        self.assertEqual(
            sorted(row["candidate_id"] for row in review_queue + deferred),
            ["low", "mid", "tie-high", "tie-low", "top"],
        )

        no_review, all_deferred = hourly.split_editorial_review_queue(drafts, limit=0)
        self.assertEqual(no_review, [])
        self.assertEqual(len(all_deferred), len(drafts))

    def test_conflicting_primary_source_counts_reject_numeric_metric_claim(self):
        candidate = dict(self.candidate)
        candidate.update({
            "title": "n8n-io/n8n",
            "source": "GitHub Search",
            "source_kind": "github_repository",
            "url": "https://github.com/n8n-io/n8n",
            "canonical_url": "https://github.com/n8n-io/n8n",
            "primary_source_verified": True,
            "primary_source_title": "GitHub - n8n-io/n8n: Fair-code workflow automation platform with 400+ integrations",
            "primary_source_description": (
                "Fair-code workflow automation platform with native AI capabilities. "
                "With 400+ integrations, teams can build powerful automations."
            ),
            "primary_source_text": (
                "The current README headline says the platform connects to 1500+ integrations. "
                "The About section still says 400+ integrations."
            ),
            "primary_source_evidence": (
                "Fair-code workflow automation platform with native AI capabilities. "
                "With 400+ integrations, teams can build powerful automations. "
                "The current README headline says the platform connects to 1500+ integrations. "
                "The About section still says 400+ integrations."
            ),
            "primary_source_final_url": "https://github.com/n8n-io/n8n",
            "evidence_urls": ["https://github.com/n8n-io/n8n"],
        })
        fact = "n8n is a fair-code workflow platform with 400+ integrations and native AI."
        takeaway = "Run a representative workflow to measure latency against your own SLA."
        quote = "Fair-code workflow automation platform with native AI capabilities. With 400+ integrations"
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": fact,
            "post_text": fact + " " + takeaway + " " + candidate["url"],
            "editorial_takeaway": takeaway,
            "evidence_quote": quote,
            "claim_evidence": [{"claim": fact, "quote": quote}],
            "scores": {"timeliness": 8, "usefulness": 8, "novelty": 7, "evidence": 8, "insight": 8},
        }
        _accepted, reasons = hourly.validate_draft(draft, {"candidate-1": candidate})
        self.assertTrue(any(
            "conflicting counts for integration" in reason for reason in reasons
        ))

        stable_evidence = "n8n's current README consistently says 1500+ integrations and native AI."
        self.assertEqual(
            hourly.conflicting_source_metric_counts(
                "n8n connects workflows with 1500+ integrations.",
                stable_evidence,
            ),
            [],
        )

    def test_valid_draft_passes_and_is_marked_dry_run_only(self):
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": "Hookdeck's webhook skills give step-by-step guidance for receivers, signature verification and event handling.",
            "post_text": (
                "Hookdeck's webhook skills give step-by-step guidance for receivers, signature verification and event "
                "handling. For webhook receivers, test signatures and duplicate events before shipping. "
                "https://github.com/hookdeck/webhook-skills"
            ),
            "format": "tool_discovery",
            "audience": "developers building integrations",
            "angle": "safer webhook setup",
            "editorial_takeaway": "For webhook receivers, test signatures and duplicate events before shipping.",
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
        self.assertEqual(accepted["status"], "dry_run_passed_not_published")

        # The writer's own novelty score is diagnostic only. The separate editor
        # makes the independent originality decision later in the pipeline.
        low_self_score = dict(draft)
        low_self_score["scores"] = dict(draft["scores"])
        low_self_score["scores"]["novelty"] = 1
        accepted_low, reasons_low = hourly.validate_draft(low_self_score, {"candidate-1": self.candidate})
        self.assertEqual(reasons_low, [])
        self.assertIsNotNone(accepted_low)

    def test_composer_assembles_separate_fact_takeaway_and_primary_url(self):
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": (
                "Hookdeck's webhook integration skills: step-by-step guidance for receivers, "
                "signature verification and event handling for coding agents."
            ),
            "editorial_takeaway": (
                "For webhook receivers, test signatures and duplicate events before shipping."
            ),
        }
        composed = hourly.compose_post_from_fields(draft, self.candidate)
        self.assertEqual(composed["post_text"].split(" https://", 1)[0],
                         draft["fact_sentence"] + " " + draft["editorial_takeaway"])
        self.assertTrue(composed["post_text"].endswith(self.candidate["url"]))
        self.assertEqual(composed["post_text"].count(self.candidate["url"]), 1)
        self.assertEqual(
            composed["copy_character_budget"],
            hourly.MAX_POST_CHARS - len(self.candidate["url"]) - 2,
        )
        self.assertLessEqual(
            len(draft["fact_sentence"]) + len(draft["editorial_takeaway"]),
            composed["copy_character_budget"],
        )
        self.assertNotIn("generation_format_error", composed)

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
            "fact_sentence": "Hookdeck's webhook integration skills guide coding agents through receiver setup, signature verification and event handling.",
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
            "fact_sentence": "Hookdeck's webhook integration skills support receiver setup and signature verification.",
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

    def test_concrete_scan_remediation_is_recognized_as_actionable(self):
        candidate = dict(self.candidate)
        candidate.update({
            "title": "Securing your app, together",
            "source": "Shopify Developer Changelog",
            "source_kind": "official_changelog",
            "url": "https://shopify.dev/changelog/securing-your-app-together",
            "canonical_url": "https://shopify.dev/changelog/securing-your-app-together",
            "summary": (
                "AI Toolkit checks for Shopify-specific vulnerabilities, such as unauthenticated routes, "
                "cross-shop data access and unverified webhooks. Move to expiring access tokens."
            ),
            "evidence_urls": ["https://shopify.dev/changelog/securing-your-app-together"],
        })
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": "AI Toolkit checks for Shopify-specific vulnerabilities.",
            "post_text": (
                "AI Toolkit checks for Shopify-specific vulnerabilities. "
                "Run the scan before release and fix any flagged routes. "
                "https://shopify.dev/changelog/securing-your-app-together"
            ),
            "editorial_takeaway": "Run the scan before release and fix any flagged routes.",
            "evidence_quote": "AI Toolkit checks for Shopify-specific vulnerabilities",
            "claim_evidence": [
                {
                    "claim": "AI Toolkit checks for Shopify-specific vulnerabilities",
                    "quote": "AI Toolkit checks for Shopify-specific vulnerabilities",
                }
            ],
            "scores": {"timeliness": 9, "usefulness": 8, "novelty": 7, "evidence": 9, "insight": 8},
        }
        _accepted, reasons = hourly.validate_draft(draft, {"candidate-1": candidate})
        self.assertFalse(any("needs a concrete test" in reason for reason in reasons))

    def test_takeaway_that_repeats_source_details_is_rejected(self):
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": "Webhook skills guide coding agents through receiver setup.",
            "post_text": (
                "Webhook skills guide coding agents through receiver setup. "
                "Check webhook receivers, signature verification and event handling. "
                "https://github.com/hookdeck/webhook-skills"
            ),
            "editorial_takeaway": "Check webhook receivers, signature verification and event handling.",
            "evidence_quote": "webhook receivers, signature verification, and event handling",
            "claim_evidence": [
                {
                    "claim": "The source describes webhook guidance for coding agents",
                    "quote": "Webhook integration skills for AI coding agents. Step-by-step guidance for setting up webhook receivers",
                }
            ],
            "scores": {"timeliness": 8, "usefulness": 8, "novelty": 8, "evidence": 8, "insight": 8},
        }
        accepted, reasons = hourly.validate_draft(draft, {"candidate-1": self.candidate})
        self.assertIsNone(accepted)
        self.assertTrue(any("mostly repeats source wording" in reason for reason in reasons))

    def test_headline_rewrite_is_rejected_even_when_it_has_a_generic_second_sentence(self):
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": "Hookdeck webhook integration skills for coding agents.",
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

    def test_feed_summary_cannot_support_a_claim_absent_from_live_primary_page(self):
        candidate = dict(self.candidate)
        candidate["primary_source_title"] = "Hookdeck webhook integration skills for coding agents"
        candidate["primary_source_description"] = "Webhook integration skills for AI coding agents."
        candidate["primary_source_text"] = "Webhook integration skills for AI coding agents."
        candidate["primary_source_evidence"] = "Webhook integration skills for AI coding agents."
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": "The skills provide signature verification and event handling for Stripe and Shopify.",
            "post_text": (
                "The skills provide signature verification and event handling for Stripe and Shopify. "
                "For webhook receivers, test signature failures before shipping. "
                "https://github.com/hookdeck/webhook-skills"
            ),
            "editorial_takeaway": "For webhook receivers, test signature failures before shipping.",
            "evidence_quote": "signature verification, and event handling",
            "claim_evidence": [
                {
                    "claim": "The skills provide signature verification and event handling for Stripe and Shopify",
                    "quote": "webhook receivers, signature verification, and event handling for Stripe, Shopify, GitHub",
                }
            ],
            "scores": {"timeliness": 8, "usefulness": 8, "novelty": 8, "evidence": 8, "insight": 8},
        }
        accepted, reasons = hourly.validate_draft(draft, {"candidate-1": candidate})
        self.assertIsNone(accepted)
        self.assertTrue(any("Primary-source evidence quote is missing" in reason for reason in reasons))
        self.assertTrue(any("factual claim lacks a quote present in the live primary-source page" in reason for reason in reasons))

    def test_primary_quote_attachment_uses_only_verbatim_page_text_and_meets_coverage(self):
        candidate = dict(self.candidate)
        candidate["primary_source_title"] = "Hookdeck webhook integration skills for coding agents"
        candidate["primary_source_description"] = "Webhook integration skills for AI coding agents."
        candidate["primary_source_text"] = (
            "Step-by-step guidance for setting up webhook receivers, signature verification, "
            "and event handling for Stripe, Shopify, GitHub, and more."
        )
        candidate["primary_source_evidence"] = candidate["primary_source_text"]
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": "Hookdeck webhook integration skills guide coding agents through receiver setup.",
            "post_text": (
                "Hookdeck webhook integration skills guide coding agents through receiver setup. "
                "Test signature failures and duplicate event delivery before shipping. "
                + candidate["url"]
            ),
            "editorial_takeaway": "Test signature failures and duplicate event delivery before shipping.",
            "evidence_quote": "webhook integration",
            "claim_evidence": [],
        }
        grounded = hourly.attach_primary_claim_evidence(draft, candidate)
        self.assertTrue(grounded.get("evidence_quote_repaired_from_primary_page"))
        quote = grounded["claim_evidence"][0]["quote"]
        self.assertIn(hourly.normalize_for_match(quote), hourly.normalize_for_match(hourly.primary_evidence_text(candidate)))
        fact_tokens = hourly.tokens(draft["fact_sentence"]) - {
            "allow", "also", "and", "are", "can", "could", "does", "for", "from", "get",
            "has", "have", "into", "its", "may", "more", "not", "now", "only", "our",
            "provides", "support", "supports", "the", "their", "this", "through", "use",
            "using", "with", "within", "your",
        }
        quote_coverage = len(fact_tokens & hourly.tokens(quote)) / max(1, len(fact_tokens))
        self.assertGreaterEqual(quote_coverage, 0.65)
        self.assertEqual(grounded["claim_evidence"][0]["claim"], draft["fact_sentence"])

    def test_primary_quote_attachment_refuses_weak_lexical_overlap(self):
        candidate = dict(self.candidate)
        candidate["primary_source_title"] = "A cooking recipe collection"
        candidate["primary_source_description"] = "Seasonal recipes for home cooks."
        candidate["primary_source_text"] = "Learn to cook simple meals with seasonal vegetables."
        candidate["primary_source_evidence"] = candidate["primary_source_text"]
        quote = hourly.best_primary_quote_for_claim(
            "Hookdeck webhook integration skills guide coding agents through receiver setup.",
            candidate,
        )
        self.assertIsNone(quote)

    def test_automatic_repair_uses_rejection_reasons_and_keeps_exact_primary_url(self):
        candidate = dict(self.candidate)
        candidate["primary_source_text"] = (
            "Webhook integration skills for AI coding agents. Step-by-step guidance for setting up webhook receivers, "
            "signature verification, and event handling for Stripe, Shopify, GitHub, and more."
        )
        candidate["primary_source_description"] = "Webhook integration skills for AI coding agents."
        candidate["primary_source_evidence"] = candidate["primary_source_text"]
        rejected = [{
            "candidate_id": "candidate-1",
            "title": candidate["title"],
            "proposed_text": "An overly long feature list that failed validation.",
            "evidence_quote": "",
            "claim_evidence": [],
            "reasons": [
                "Fact sentence is too long; narrow it to one source-backed capability.",
                "Editorial takeaway is too long; keep the analysis concrete and concise.",
            ],
        }]
        repaired_response = {
            "drafts": [{
                "candidate_id": "candidate-1",
                "fact_sentence": "Hookdeck's webhook skills guide coding agents through receiver setup.",
                "editorial_takeaway": "Test invalid signatures and duplicate deliveries before shipping.",
                "evidence_quote": "Step-by-step guidance for setting up webhook receivers",
                "claim_evidence": [{
                    "claim": "Hookdeck's webhook skills guide coding agents through receiver setup",
                    "quote": "Step-by-step guidance for setting up webhook receivers",
                }],
                "format": "tool_discovery",
                "audience": "developers",
                "angle": "webhook testing",
                "rationale": "Narrowed the claim and shortened the test advice after specific validator failures.",
                "scores": {"timeliness": 8, "usefulness": 8, "novelty": 7, "evidence": 9, "insight": 8},
            }]
        }
        response = {"choices": [{"message": {"content": json.dumps(repaired_response)}}]}
        with patch.object(hourly, "request_groq", return_value=response):
            drafts, error = hourly.repair_rejected_drafts(rejected, {"candidate-1": candidate})
        self.assertIsNone(error)
        self.assertEqual(len(drafts), 1)
        self.assertTrue(drafts[0]["automatic_repair_attempt"])
        self.assertTrue(drafts[0]["post_text"].endswith(candidate["url"]))
        self.assertIn("Fact sentence is too long", drafts[0]["repaired_after_reasons"][0])

    def test_repair_selection_prioritizes_savings_measurement_failure_over_earlier_drafts(self):
        candidates = {}
        rejected = []
        fixtures = [
            ("taskuary", 77, ["The factual opening bundles multiple features; narrow it to one capability."]),
            ("chattermate", 76, ["Takeaway implies an interaction/causal relationship between source-listed features."]),
            ("shopify-consent", 75, ["Supporting quotes cover only 50% of factual wording."]),
            ("caudra", 73, [
                "Efficiency/savings takeaway lacks a baseline or direct metric; repeating the same prompt twice does not isolate savings."
            ]),
        ]
        for name, score, reasons in fixtures:
            candidate = dict(self.candidate)
            candidate.update({
                "id": name,
                "title": name,
                "url": f"https://github.com/example/{name}",
                "canonical_url": f"https://github.com/example/{name}",
                "primary_source_title": f"{name} primary page",
                "primary_source_description": f"Primary description for {name}.",
                "primary_source_text": f"Primary evidence for {name}, with enough text to support a useful verified summary.",
                "primary_source_evidence": f"{name} primary page. Primary evidence for {name}, with enough text to support a useful verified summary.",
                "primary_source_verified": True,
                "primary_source_http_status": 200,
                "hourly_adjusted_score": score,
                "priority_score": score,
            })
            candidates[name] = candidate
            rejected.append({
                "candidate_id": name,
                "title": name,
                "proposed_text": f"{name} first-pass text failed validation. {candidate['url']}",
                "reasons": reasons,
                "claim_evidence": [],
            })
        response = {"choices": [{"message": {"content": json.dumps({"drafts": []})}}]}
        with patch.object(hourly, "request_groq", return_value=response) as mocked:
            repaired, error = hourly.repair_rejected_drafts(rejected, candidates, limit=1)
        self.assertEqual(repaired, [])
        self.assertIsNone(error)
        payload = json.loads(mocked.call_args.args[0][1]["content"])
        self.assertEqual(
            [item["candidate_id"] for item in payload["rejected_candidates"]],
            ["caudra"],
        )

    def test_automatic_repair_does_not_guess_candidate_for_unknown_id(self):
        rejected = [{
            "candidate_id": "candidate-unknown",
            "title": "Unknown",
            "proposed_text": "Some text",
            "reasons": ["Missing source evidence"],
        }]
        drafts, error = hourly.repair_rejected_drafts(rejected, {"candidate-1": self.candidate})
        self.assertEqual(drafts, [])
        self.assertIsNone(error)

    def test_groq_413_retries_with_smaller_candidate_pool(self):
        candidates = []
        for index in range(3):
            item = dict(self.candidate)
            item["id"] = f"candidate-{index}"
            item["title"] = f"Distinct project {index}"
            item["url"] = f"https://github.com/example/project-{index}"
            item["canonical_url"] = item["url"]
            item["primary_source_title"] = item["title"]
            item["primary_source_description"] = "Source description for the project."
            item["primary_source_evidence"] = (
                item["title"] + " provides a useful workflow for developers."
            )
            candidates.append(item)

        empty_drafts = {"choices": [{"message": {"content": json.dumps({"drafts": []})}}]}
        with patch.dict(os.environ, {"GROQ_API_KEY": "test-key"}):
            with patch.object(hourly, "request_groq", side_effect=[RuntimeError("Groq returned HTTP 413"), empty_drafts]) as mocked:
                drafts, error = hourly.draft_candidates(candidates)
        self.assertEqual(drafts, [])
        self.assertIsNone(error)
        self.assertEqual(mocked.call_count, 2)
        retried_payload = json.loads(mocked.call_args_list[1].args[0][1]["content"])
        self.assertEqual(len(retried_payload["candidates"]), 1)

    def test_missing_evidence_quote_is_derived_only_from_a_quote_found_on_the_live_page(self):
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": "Webhook skills guide AI coding agents through signature verification.",
            "editorial_takeaway": "Test invalid signatures and duplicate deliveries before shipping.",
            "claim_evidence": [
                {
                    "claim": "The source says capability X",
                    "quote": "Webhook integration skills for AI coding agents. Step-by-step guidance for setting up webhook receivers, signature verification, and event handling",
                }
            ],
        }
        composed = hourly.compose_post_from_fields(draft, self.candidate)
        self.assertEqual(composed.get("evidence_quote"), draft["claim_evidence"][0]["quote"])
        self.assertTrue(composed["post_text"].endswith(self.candidate["url"]))

    def test_markdown_code_wrappers_do_not_break_a_live_page_quote(self):
        page_text = "Checkout MCP and Cart MCP responses include a buyer.consent object."
        quoted_text = "Checkout MCP and Cart MCP responses include a " + chr(96) + "buyer.consent" + chr(96) + " object."
        self.assertIn(
            hourly.normalize_for_match(quoted_text),
            hourly.normalize_for_match(page_text),
        )

    def test_multi_feature_fact_sentence_is_rejected(self):
        candidate = dict(self.candidate)
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": (
                "The tool supports webhook receiver setup, signature verification, and event handling for Shopify."
            ),
            "post_text": (
                "The tool supports webhook receiver setup, signature verification, and event handling for Shopify. "
                "Test failed signature handling before shipping. https://github.com/hookdeck/webhook-skills"
            ),
            "editorial_takeaway": "Test failed signature handling before shipping.",
            "evidence_quote": "webhook receivers, signature verification, and event handling for Stripe, Shopify, GitHub, and more.",
            "claim_evidence": [
                {
                    "claim": "The source describes setup, verification and event handling",
                    "quote": "webhook receivers, signature verification, and event handling for Stripe, Shopify, GitHub, and more.",
                }
            ],
            "scores": {"timeliness": 8, "usefulness": 8, "novelty": 8, "evidence": 8, "insight": 8},
        }
        accepted, reasons = hourly.validate_draft(draft, {"candidate-1": candidate})
        self.assertIsNone(accepted)
        self.assertTrue(any("bundles multiple features" in reason for reason in reasons))

    def test_numeric_unit_spacing_is_normalized_without_hiding_different_values(self):
        source_numbers = {
            hourly.re.sub(r"\s+", "", value).casefold()
            for value in hourly.NUMBER_RE.findall("The page adds one 3.2KB script.")
        }
        post_numbers = {
            hourly.re.sub(r"\s+", "", value).casefold()
            for value in hourly.NUMBER_RE.findall("The page adds one 3.2 KB script.")
        }
        self.assertEqual(source_numbers, post_numbers)
        self.assertNotEqual(
            {hourly.re.sub(r"\s+", "", value).casefold() for value in hourly.NUMBER_RE.findall("PageSpeed score 99")},
            {hourly.re.sub(r"\s+", "", value).casefold() for value in hourly.NUMBER_RE.findall("PageSpeed score 100")},
        )

        version_numbers = hourly.NUMBER_RE.findall("GraphQL Admin API 2027-01 lets you read and configure a flag.")
        self.assertEqual(version_numbers, ["2027", "01"])
        self.assertNotIn("01lets", {value.casefold() for value in version_numbers})

    def test_missing_candidate_id_is_recovered_only_from_exact_verified_source_url(self):
        candidates = {
            "candidate-1": {"url": "https://github.com/hookdeck/webhook-skills"},
            "candidate-2": {"url": "https://github.com/example/other-tool"},
        }
        recovered, note = hourly.resolve_candidate_id({
            "candidate_id": "",
            "post_text": "Hookdeck guides webhook setup. https://github.com/hookdeck/webhook-skills",
        }, candidates)
        self.assertEqual(recovered, "candidate-1")
        self.assertIn("exact verified source URL", note)

        missing, reason = hourly.resolve_candidate_id({
            "candidate_id": "",
            "post_text": "A generic paragraph without an original source link.",
        }, candidates)
        self.assertIsNone(missing)
        self.assertIn("no exact verified source URL matched", reason)

    def test_github_feature_word_cannot_substitute_for_named_repository_identity(self):
        candidate = dict(self.candidate)
        page_text = (
            "ChatterMate provides human handoff and Shopify support for customer-service chats. "
            "Webhooks are outbound ticket webhooks to drive your own automations."
        )
        candidate.update({
            "title": "chattermate/chattermate.chat",
            "source": "GitHub Search",
            "source_kind": "github_repository",
            "url": "https://github.com/chattermate/chattermate.chat",
            "canonical_url": "https://github.com/chattermate/chattermate.chat",
            "primary_source_title": "ChatterMate - Open Source AI Customer Support Chatbot Platform",
            "primary_source_description": "AI chatbot with Shopify and e-commerce support.",
            "primary_source_text": page_text,
            "primary_source_evidence": (
                "ChatterMate - Open Source AI Customer Support Chatbot Platform. "
                "AI chatbot with Shopify and e-commerce support. " + page_text
            ),
            "primary_source_verified": True,
            "primary_source_http_status": 200,
            "primary_source_final_url": "https://github.com/chattermate/chattermate.chat",
            "evidence_urls": ["https://github.com/chattermate/chattermate.chat"],
        })
        fact = "Supports Shopify integration for AI chat."
        takeaway = "Test whether your own workflow triggers a ticket webhook after handoff."
        quote = "AI chatbot with Shopify and e-commerce support."
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": fact,
            "post_text": fact + " " + takeaway + " " + candidate["url"],
            "editorial_takeaway": takeaway,
            "evidence_quote": quote,
            "claim_evidence": [{"claim": fact, "quote": quote}],
            "scores": {"timeliness": 8, "usefulness": 8, "novelty": 7, "evidence": 8, "insight": 8},
        }
        _accepted, reasons = hourly.validate_draft(draft, {"candidate-1": candidate})
        self.assertTrue(any(
            "named product/repository/feature subject" in reason for reason in reasons
        ))

        named_fact = "ChatterMate supports Shopify integration for AI chat."
        draft["fact_sentence"] = named_fact
        draft["post_text"] = named_fact + " " + takeaway + " " + candidate["url"]
        draft["claim_evidence"] = [{"claim": named_fact, "quote": quote}]
        _accepted_named, named_reasons = hourly.validate_draft(draft, {"candidate-1": candidate})
        self.assertFalse(any(
            "named product/repository/feature subject" in reason for reason in named_reasons
        ))

    def test_opening_must_name_the_product_not_start_with_an_orphaned_verb(self):
        candidate = dict(self.candidate)
        candidate.update({
            "title": "Show HN: Bloffy, a blog you write freely and own completely",
            "source": "Hacker News",
            "source_kind": "hacker_news",
            "url": "https://bloffy.co/en",
            "canonical_url": "https://bloffy.co/en",
            "primary_source_title": "A blog you write freely and own completely | Bloffy",
            "primary_source_description": "All Bloffy adds to a reader's page is one small 3.2KB script.",
            "primary_source_text": "All Bloffy adds to a reader's page is one small 3.2KB script.",
            "primary_source_evidence": "A blog you write freely and own completely. All Bloffy adds to a reader's page is one small 3.2KB script.",
            "evidence_urls": ["https://bloffy.co/en"],
        })
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": "Adds only a 3.2KB script to pages.",
            "post_text": (
                "Adds only a 3.2KB script to pages. "
                "Measure page load to confirm script size stays under 4KB. "
                "https://bloffy.co/en"
            ),
            "editorial_takeaway": "Measure page load to confirm script size stays under 4KB.",
            "evidence_quote": "All Bloffy adds to a reader's page is one small 3.2KB script.",
            "claim_evidence": [
                {
                    "claim": "Bloffy adds a small script to a reader's page",
                    "quote": "All Bloffy adds to a reader's page is one small 3.2KB script",
                }
            ],
            "scores": {"timeliness": 8, "usefulness": 8, "novelty": 8, "evidence": 8, "insight": 8},
        }
        accepted, reasons = hourly.validate_draft(draft, {"candidate-1": candidate})
        self.assertIsNone(accepted)
        self.assertTrue(any("omits the named product/repository/feature subject" in reason for reason in reasons))

    def test_unsupported_skill_sync_capability_is_rejected_locally(self):
        candidate = dict(self.candidate)
        candidate["primary_source_text"] = (
            "Hookdeck webhook integration skills for coding agents. "
            "Step-by-step guidance for receivers, signature verification and event handling."
        )
        candidate["primary_source_description"] = "Webhook integration skills for AI coding agents."
        candidate["primary_source_evidence"] = candidate["primary_source_text"]
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": "Hookdeck provides webhook integration skills for coding agents.",
            "post_text": (
                "Hookdeck provides webhook integration skills for coding agents. "
                "Test that agent skill syncs before launching parallel workflows. "
                "https://github.com/hookdeck/webhook-skills"
            ),
            "editorial_takeaway": "Test that agent skill syncs before launching parallel workflows.",
            "evidence_quote": "Hookdeck webhook integration skills for coding agents",
            "claim_evidence": [
                {
                    "claim": "Hookdeck provides webhook integration skills for coding agents",
                    "quote": "Hookdeck webhook integration skills for coding agents",
                }
            ],
            "scores": {"timeliness": 8, "usefulness": 8, "novelty": 8, "evidence": 8, "insight": 8},
        }
        accepted, reasons = hourly.validate_draft(draft, {"candidate-1": candidate})
        self.assertIsNone(accepted)
        self.assertTrue(any("undocumented product capability" in reason for reason in reasons))

    def test_token_savings_advice_needs_a_baseline_or_direct_usage_metric(self):
        candidate = dict(self.candidate)
        page_text = (
            "Command-aware filters shrink shell output before the model reads it. "
            "You can switch between filtered and raw views. "
            "/usage shows what the session spent and scores the cache hit rate."
        )
        candidate.update({
            "title": "Show HN: Caudra - An open-source terminal coding agent in one native binary",
            "source": "Hacker News",
            "source_kind": "hacker_news",
            "url": "https://github.com/caudra/caudra",
            "canonical_url": "https://github.com/caudra/caudra",
            "primary_source_title": "GitHub - caudra/caudra: The complete coding agent for your terminal",
            "primary_source_description": (
                "Caudra arrives complete. Steerable subagents, built-in token savings, a workbench, "
                "and a history you can revert were designed together."
            ),
            "primary_source_text": page_text,
            "primary_source_evidence": (
                "GitHub - caudra/caudra: The complete coding agent for your terminal. "
                "Caudra arrives complete. Steerable subagents, built-in token savings, a workbench, "
                "and a history you can revert were designed together. " + page_text
            ),
            "primary_source_verified": True,
            "primary_source_http_status": 200,
            "primary_source_final_url": "https://github.com/caudra/caudra",
            "evidence_urls": ["https://github.com/caudra/caudra"],
        })
        fact = "Caudra filters shell output before the model reads it."
        quote = "Command-aware filters shrink shell output before the model reads it."
        scores = {"timeliness": 8, "usefulness": 8, "novelty": 7, "evidence": 8, "insight": 8}
        bad_takeaway = "Run the same prompt twice to confirm token savings; test history revert."
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": fact,
            "post_text": fact + " " + bad_takeaway + " " + candidate["url"],
            "editorial_takeaway": bad_takeaway,
            "evidence_quote": quote,
            "claim_evidence": [{"claim": fact, "quote": quote}],
            "scores": scores,
        }
        _accepted, reasons = hourly.validate_draft(draft, {"candidate-1": candidate})
        self.assertTrue(any(
            "lacks a baseline or direct metric" in reason for reason in reasons
        ))

        good_takeaway = "Compare filtered vs raw shell output to verify token savings in /usage."
        draft["editorial_takeaway"] = good_takeaway
        draft["post_text"] = fact + " " + good_takeaway + " " + candidate["url"]
        _accepted_good, good_reasons = hourly.validate_draft(draft, {"candidate-1": candidate})
        self.assertFalse(any(
            "lacks a baseline or direct metric" in reason for reason in good_reasons
        ))

    def test_unverified_relationship_between_shopify_webhooks_and_handoff_is_rejected(self):
        candidate = dict(self.candidate)
        page_text = (
            "ChatterMate provides human handoff and Shopify support for customer-service chats. "
            "Webhooks are outbound ticket webhooks to drive your own automations."
        )
        candidate.update({
            "title": "chattermate/chattermate.chat",
            "source": "GitHub Search",
            "source_kind": "github_repository",
            "url": "https://github.com/chattermate/chattermate.chat",
            "canonical_url": "https://github.com/chattermate/chattermate.chat",
            "primary_source_title": "ChatterMate - Open Source AI Customer Support Chatbot Platform",
            "primary_source_description": (
                "Open-source AI customer support platform with human handoff. "
                "AI chatbot with Shopify and e-commerce support."
            ),
            "primary_source_text": page_text,
            "primary_source_evidence": (
                "ChatterMate - Open Source AI Customer Support Chatbot Platform. "
                "Open-source AI customer support platform with human handoff. "
                "AI chatbot with Shopify and e-commerce support. " + page_text
            ),
            "evidence_urls": ["https://github.com/chattermate/chattermate.chat"],
        })
        fact = "ChatterMate offers Shopify support in its AI customer-service chatbot."
        quote = "AI chatbot with Shopify and e-commerce support."
        bad_takeaway = "Verify Shopify webhook triggers after handoff."
        draft = {
            "candidate_id": "candidate-1",
            "fact_sentence": fact,
            "post_text": fact + " " + bad_takeaway + " " + candidate["url"],
            "editorial_takeaway": bad_takeaway,
            "evidence_quote": quote,
            "claim_evidence": [{"claim": fact, "quote": quote}],
            "scores": {"timeliness": 8, "usefulness": 8, "novelty": 7, "evidence": 8, "insight": 8},
        }
        _accepted, reasons = hourly.validate_draft(draft, {"candidate-1": candidate})
        self.assertTrue(any(
            "interaction/causal relationship between source-listed features" in reason
            for reason in reasons
        ))

        # Conditional advice about the reader's own integration is allowed; it does
        # not claim ChatterMate ships a Shopify-specific webhook trigger.
        conditional = "Test whether your own workflow triggers a ticket webhook after handoff."
        draft["editorial_takeaway"] = conditional
        draft["post_text"] = fact + " " + conditional + " " + candidate["url"]
        _accepted_conditional, conditional_reasons = hourly.validate_draft(draft, {"candidate-1": candidate})
        self.assertFalse(any(
            "interaction/causal relationship between source-listed features" in reason
            for reason in conditional_reasons
        ))

    def test_independent_editor_rejects_metric_mismatch(self):
        draft = {
            "candidate_id": "candidate-1",
            "title": "Bloffy",
            "post_text": (
                "Bloffy adds a 3.2KB script to reader pages. "
                "Measure page load to confirm script size stays under 4KB. https://bloffy.co/en"
            ),
            "fact_sentence": "Bloffy adds a 3.2KB script to reader pages.",
            "editorial_takeaway": "Measure page load to confirm script size stays under 4KB.",
            "url": "https://bloffy.co/en",
            "claim_evidence": [],
        }
        review_payload = {
            "reviews": [{
                "candidate_id": "candidate-1",
                "pass": False,
                "clarity_score": 8,
                "technical_coherence_score": 3,
                "takeaway_value_score": 5,
                "source_faithfulness_score": 7,
                "originality_score": 7,
                "reason": "Page-load timing does not measure script byte size; inspect the transferred resource size instead.",
            }]
        }
        response = {"choices": [{"message": {"content": json.dumps(review_payload)}}]}
        with patch.object(hourly, "request_groq", return_value=response):
            approved, rejected, error = hourly.editorial_review_drafts([draft], {"candidate-1": self.candidate})
        self.assertIsNone(error)
        self.assertEqual(approved, [])
        self.assertEqual(len(rejected), 1)
        self.assertIn("does not measure script byte size", rejected[0]["reasons"][0])
        self.assertEqual(rejected[0]["editorial_review"]["technical_coherence_score"], 3)

    def test_independent_editor_rejects_low_originality_even_if_other_scores_pass(self):
        draft = {
            "candidate_id": "candidate-1",
            "title": "Hookdeck webhook skills",
            "post_text": "Hookdeck provides webhook integration guidance. Test duplicate delivery before shipping.",
            "fact_sentence": "Hookdeck provides webhook integration guidance.",
            "editorial_takeaway": "Test duplicate delivery before shipping.",
            "url": "https://github.com/hookdeck/webhook-skills",
            "claim_evidence": [],
        }
        review_payload = {
            "reviews": [{
                "candidate_id": "candidate-1",
                "pass": False,
                "clarity_score": 8,
                "technical_coherence_score": 8,
                "takeaway_value_score": 8,
                "source_faithfulness_score": 8,
                "originality_score": 4,
                "reason": "The opening mostly paraphrases the project description and adds little perspective.",
            }]
        }
        response = {"choices": [{"message": {"content": json.dumps(review_payload)}}]}
        with patch.object(hourly, "request_groq", return_value=response):
            approved, rejected, error = hourly.editorial_review_drafts([draft], {"candidate-1": self.candidate})
        self.assertIsNone(error)
        self.assertEqual(approved, [])
        self.assertEqual(len(rejected), 1)
        self.assertEqual(rejected[0]["editorial_review"]["originality_score"], 4)
        self.assertIn("paraphrases", rejected[0]["reasons"][0])

    def test_independent_editor_pass_is_required_even_after_local_validation(self):
        draft = {
            "candidate_id": "candidate-1",
            "title": "Hookdeck webhook skills",
            "post_text": "Hookdeck provides webhook integration guidance. Test duplicate delivery before shipping.",
            "fact_sentence": "Hookdeck provides webhook integration guidance.",
            "editorial_takeaway": "Test duplicate delivery before shipping.",
            "url": "https://github.com/hookdeck/webhook-skills",
            "claim_evidence": [],
        }
        review_payload = {
            "reviews": [{
                "candidate_id": "candidate-1",
                "pass": True,
                "clarity_score": 8,
                "technical_coherence_score": 8,
                "takeaway_value_score": 8,
                "source_faithfulness_score": 8,
                "originality_score": 8,
                "reason": "The subject is named and the test logically follows from the integration use case.",
            }]
        }
        response = {"choices": [{"message": {"content": json.dumps(review_payload)}}]}
        with patch.object(hourly, "request_groq", return_value=response):
            approved, rejected, error = hourly.editorial_review_drafts([draft], {"candidate-1": self.candidate})
        self.assertIsNone(error)
        self.assertEqual(rejected, [])
        self.assertEqual(len(approved), 1)
        self.assertTrue(approved[0]["editorial_review"]["passed"])
        self.assertEqual(approved[0]["editorial_review"]["technical_coherence_score"], 8)

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
        self.assertEqual(candidate["stars_delta_24h"], -2)
        self.assertEqual(candidate["stars_growth_percent_24h"], -2.0)

    def test_star_watchlist_refreshes_repositories_missing_from_current_discovery(self):
        state = hourly.empty_state()
        old_key = "123456"
        old_sample = self.now.isoformat()
        state["repo_star_watchlist"][old_key] = {
            "repo_id": old_key,
            "full_name": "prior-owner/prior-repo",
            "first_seen_at": old_sample,
            "last_seen_at": (self.now - timedelta(hours=2)).isoformat(),
            "consecutive_refresh_failures": 0,
        }
        state["repo_star_snapshots"][old_key] = [{"at": old_sample, "stars": 100}]
        current = dict(self.candidate)
        current["signals"] = {"stars": 50, "github_repo_id": "999999", "full_name": "current-owner/current-repo"}
        refreshed_metadata = {
            "repo_id": old_key,
            "full_name": "prior-owner/prior-repo",
            "stars": 140,
            "archived": False,
            "html_url": "https://github.com/prior-owner/prior-repo",
            "updated_at": "",
            "pushed_at": "",
        }
        with patch.dict(os.environ, {"GITHUB_TOKEN": "test-token"}):
            with patch.object(hourly, "fetch_github_repo_metadata", return_value=refreshed_metadata):
                metrics = hourly.update_github_star_velocity([current], state, self.now + timedelta(hours=24), refresh_missing=True)
        self.assertEqual(metrics["previously_tracked_repositories_refreshed"], 1)
        self.assertEqual(state["repo_star_snapshots"][old_key][-1]["stars"], 140)
        self.assertEqual(metrics["repositories_with_20_to_36_hour_baseline"], 1)
        self.assertEqual(state["repo_star_watchlist"][old_key]["full_name"], "prior-owner/prior-repo")

    def test_repository_numeric_id_keeps_star_history_across_renames(self):
        state = hourly.empty_state()
        candidate = dict(self.candidate)
        candidate["signals"] = {"stars": 100, "github_repo_id": "123456", "full_name": "owner/old-name"}
        hourly.update_github_star_velocity([candidate], state, self.now)
        renamed = dict(candidate)
        renamed["title"] = "owner/new-name"
        renamed["url"] = "https://github.com/owner/new-name"
        renamed["canonical_url"] = renamed["url"]
        renamed["id"] = "a-different-url-derived-id"
        renamed["signals"] = {"stars": 120, "github_repo_id": "123456", "full_name": "owner/new-name"}
        hourly.update_github_star_velocity([renamed], state, self.now + timedelta(hours=24))
        self.assertEqual(renamed["stars_delta_24h"], 20)
        self.assertIn("123456", state["repo_star_snapshots"])
        self.assertEqual(len(state["repo_star_snapshots"]), 1)
        self.assertEqual(state["repo_star_watchlist"]["123456"]["full_name"], "owner/new-name")

    def test_primary_source_verifier_rejects_http_404(self):
        error = urllib.error.HTTPError(
            self.candidate["url"], 404, "Not Found", {}, None
        )
        with patch.object(hourly.urllib.request, "urlopen", side_effect=error):
            verified, reason = hourly.verify_primary_source(self.candidate)
        self.assertIsNone(verified)
        self.assertIn("HTTP 404", reason)

    def test_primary_source_verifier_keeps_live_page_evidence_and_redirect_target(self):
        html = (
            "<html><head><title>Hookdeck webhook integration skills for coding agents</title>"
            '<meta name="description" content="Webhook integration skills for AI coding agents."></head>'
            "<body><article><p>Step-by-step guidance for setting up webhook receivers, signature verification, "
            "and event handling for Stripe, Shopify, and GitHub.</p></article></body></html>"
        ).encode("utf-8")

        class FakeResponse:
            status = 200
            headers = {"Content-Type": "text/html; charset=utf-8"}

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def geturl(self):
                return "https://github.com/hookdeck/webhook-skills"

            def read(self, _size=-1):
                return html

        with patch.object(hourly.urllib.request, "urlopen", return_value=FakeResponse()):
            verified, reason = hourly.verify_primary_source(self.candidate)
        self.assertIsNone(reason)
        self.assertTrue(verified["primary_source_verified"])
        self.assertEqual(verified["primary_source_http_status"], 200)
        self.assertIn("signature verification", verified["primary_source_evidence"])
        self.assertEqual(verified["url"], "https://github.com/hookdeck/webhook-skills")

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
