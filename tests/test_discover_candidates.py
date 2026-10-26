import sys
import collections
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import discover_candidates as discovery


class DiscoveryHelpersTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = discovery.load_config()
        cls.now = datetime(2026, 10, 21, 12, 0, tzinfo=timezone.utc)

    def test_clean_text_decodes_html_and_collapses_spaces(self):
        self.assertEqual(discovery.clean_text("<p>Build&nbsp; tools</p> &amp; ship"), "Build tools & ship")

    def test_canonicalize_url_removes_tracking_parameters(self):
        self.assertEqual(
            discovery.canonicalize_url("https://Example.com/project/?utm_source=x&ref=mail&mode=dark"),
            "https://example.com/project?mode=dark",
        )

    def test_parse_datetime_accepts_iso_and_rss_dates(self):
        iso_value = discovery.parse_datetime("2026-10-20T12:00:00Z")
        rss_value = discovery.parse_datetime("Tue, 20 Oct 2026 12:00:00 +0000")
        self.assertEqual(iso_value, rss_value)
        self.assertEqual(iso_value.tzinfo, timezone.utc)

    def test_shopify_digital_product_is_routed_to_commerce(self):
        categories = discovery.category_matches(
            "Shopify app for digital product checkout and subscriptions with a storefront API",
            self.config,
        )
        self.assertIn("commerce_and_digital_products", categories)

    def test_developer_cli_is_routed_to_developer_tools(self):
        categories = discovery.category_matches(
            "Open source CLI SDK for API testing, database migrations and deployment",
            self.config,
        )
        self.assertEqual(categories[0], "developer_tools")

    def test_digital_product_and_seller_operations_have_distinct_lanes(self):
        categories = discovery.category_matches(
            "A Notion template and spreadsheet for Etsy digital download sellers to track inventory, fees and profit margin",
            self.config,
        )
        self.assertIn("digital_product_business", categories)
        self.assertIn("online_seller_operations", categories)

    def test_expanded_registry_includes_creator_commerce_and_business_sources(self):
        feed_names = {feed["name"] for feed in self.config["feeds"]}
        self.assertIn("Shopify Community", feed_names)
        self.assertIn("Stripe Blog", feed_names)
        self.assertIn("Ahrefs Blog", feed_names)
        self.assertIn("Indie Hackers (unofficial third-party feed)", feed_names)
        self.assertGreaterEqual(len(self.config["wordpress_searches"]), 4)

    def test_new_editorial_feeds_have_competitive_source_weights(self):
        weights = self.config["source_weights"]
        # The expanded feeds must be capable of surfacing in discovery; they should
        # not be structurally buried beneath activity-driven GitHub/ HN candidates.
        editorial_sources = (
            "Console.dev",
            "Product Hunt",
            "Shopify Developer Changelog",
            "Stripe Blog",
            "Ahrefs Blog",
            "Indie Hackers",
            "WooCommerce Blog",
        )
        self.assertTrue(all(weights[name] >= 16 for name in editorial_sources))
        self.assertGreaterEqual(weights["Shopify Community"], 12)
        self.assertLessEqual(weights["GitHub Search"], 12)

    def test_wordpress_datetime_parses_official_api_timestamp(self):
        parsed = discovery.parse_wordpress_datetime("2026-10-20 4:15pm GMT")
        self.assertEqual(parsed, "2026-10-20T16:15:00+00:00")

    def test_wordpress_plugin_response_records_adoption_and_feedback_signals(self):
        payload = {
            "plugins": [{
                "name": "Easy Digital Downloads",
                "slug": "easy-digital-downloads",
                "url": "https://wordpress.org/plugins/easy-digital-downloads/",
                "homepage": "https://easydigitaldownloads.com/",
                "short_description": "Sell digital downloads, ebooks, templates and software from WordPress.",
                "last_updated": "2026-10-20 4:15pm GMT",
                "active_installs": 40000,
                "rating": 94,
                "num_ratings": 587,
                "downloaded": 1234567,
                "tags": {"digital-downloads": "Digital Downloads"},
            }]
        }
        search = {
            "id": "wp-digital-downloads",
            "query": "digital downloads",
            "category": "digital_product_business",
        }
        candidates = discovery.parse_wordpress_plugin_response(
            payload, search, self.config, self.now
        )
        self.assertEqual(len(candidates), 1)
        candidate = candidates[0]
        self.assertEqual(candidate["source"], "WordPress Plugin Directory")
        self.assertEqual(candidate["source_kind"], "wordpress_plugin")
        self.assertEqual(candidate["url"], "https://wordpress.org/plugins/easy-digital-downloads/")
        self.assertIn("digital_product_business", candidate["categories"])
        self.assertEqual(candidate["signals"]["active_installs"], 40000)
        self.assertEqual(candidate["signals"]["num_ratings"], 587)
        self.assertEqual(candidate["signals"]["rating_percent"], 94.0)
        self.assertIn("not paid-revenue evidence", candidate["signals"]["signal_interpretation"])

    def test_preview_selection_prioritizes_one_candidate_per_source(self):
        sources = [
            "GitHub Search", "Hacker News", "Shopify Community",
            "Shopify Developer Changelog", "WordPress Plugin Directory",
            "Indie Hackers (unofficial third-party feed)", "Product Hunt",
            "Console.dev", "Ahrefs Blog", "Stripe Blog", "WooCommerce Blog",
        ]
        candidates = []
        for index, source in enumerate(sources):
            candidates.append({
                "id": f"source-{index}",
                "url": f"https://example.com/source-{index}",
                "source": source,
                "primary_category": (
                    "commerce_and_digital_products"
                    if index in (0, 2, 3, 10)
                    else f"category-{index}"
                ),
                "priority_score": 100 - index,
            })
        # Extra high-ranked GitHub items must not crowd the other sources out.
        for index in range(20):
            candidates.insert(0, {
                "id": f"github-extra-{index}",
                "url": f"https://example.com/github-extra-{index}",
                "source": "GitHub Search",
                "primary_category": "commerce_and_digital_products",
                "priority_score": 200 - index,
            })

        selected = discovery.select_preview_candidates(candidates, 11)
        selected_sources = {
            "GitHub Search" if row["source"].startswith("GitHub Search")
            else "Hacker News" if row["source"].startswith("Hacker News")
            else row["source"]
            for row in selected
        }
        self.assertEqual(len(selected), 11)
        self.assertTrue(set(sources).issubset(selected_sources))

    def test_preview_selection_limits_source_and_category_concentration(self):
        candidates = []
        sources = (
            "GitHub Search",
            "Hacker News · hn-show-hn",
            "Shopify Community",
            "Ahrefs Blog",
            "Stripe Blog",
            "WooCommerce Blog",
        )
        categories = ("ai_and_automation", "commerce_and_digital_products")
        for index in range(30):
            candidates.append({
                "id": f"candidate-{index}",
                "url": f"https://example.com/{index}",
                "source": sources[index % len(sources)],
                "primary_category": categories[index % len(categories)],
                "priority_score": 100 - index,
            })

        selected = discovery.select_preview_candidates(candidates, 12)
        source_groups = collections.Counter(
            "GitHub Search" if row["source"].startswith("GitHub Search")
            else "Hacker News" if row["source"].startswith("Hacker News")
            else row["source"]
            for row in selected
        )
        category_counts = collections.Counter(row["primary_category"] for row in selected)
        self.assertEqual(len(selected), 12)
        self.assertLessEqual(max(source_groups.values()), 3)
        self.assertLessEqual(max(category_counts.values()), 8)
        self.assertGreaterEqual(len(source_groups), 4)
        scores = [row["priority_score"] for row in selected]
        self.assertEqual(scores, sorted(scores, reverse=True))

    def test_rss_parser_preserves_primary_link_and_source_date(self):
        xml = """<?xml version="1.0"?>
        <rss version="2.0"><channel><item>
          <title>Shopify checkout API update</title>
          <link>https://example.com/changelog/checkout</link>
          <description><![CDATA[<p>New checkout API for digital products</p>]]></description>
          <pubDate>Tue, 20 Oct 2026 12:00:00 +0000</pubDate>
          <category>Commerce</category>
        </item></channel></rss>"""
        feed = {
            "id": "shopify-dev-changelog",
            "name": "Shopify Developer Changelog",
            "url": "https://example.com/feed.xml",
            "category_hint": "commerce_and_digital_products",
        }
        result = discovery.parse_feed_xml(xml, feed, self.config, self.now)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["url"], "https://example.com/changelog/checkout")
        self.assertEqual(result[0]["source_kind"], "official_changelog")
        self.assertIn("commerce_and_digital_products", result[0]["categories"])
        self.assertIn("digital products", result[0]["summary"].lower())

    def test_atom_parser_handles_namespaced_entry(self):
        xml = """<?xml version="1.0"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <title>Console tool launch</title>
            <link href="https://example.com/tool"/>
            <updated>2026-10-20T12:00:00Z</updated>
            <summary>A developer tool to automate workflows</summary>
          </entry>
        </feed>"""
        feed = {
            "id": "console-dev",
            "name": "Console.dev",
            "url": "https://example.com/feed.xml",
            "category_hint": "developer_tools",
        }
        result = discovery.parse_feed_xml(xml, feed, self.config, self.now)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["url"], "https://example.com/tool")
        self.assertEqual(result[0]["published_at"], "2026-10-20T12:00:00+00:00")

    def test_recent_candidate_ranks_above_stale_candidate(self):
        common = {
            "source": "GitHub Search",
            "source_kind": "github_repository",
            "title": "Digital Product Checkout API",
            "url": "https://example.com/project",
            "summary": "A useful API integration for checkout automation",
            "category_hint": "commerce_and_digital_products",
            "signals": {"stars": 100},
            "config": self.config,
        }
        recent = discovery.normalize_candidate(
            **common, published_at=self.now - timedelta(days=1), now=self.now
        )
        stale = discovery.normalize_candidate(
            **common, published_at=self.now - timedelta(days=25), now=self.now
        )
        self.assertGreater(recent["priority_score"], stale["priority_score"])

    def test_merge_duplicates_keeps_both_sources_and_evidence(self):
        first = discovery.normalize_candidate(
            source="Product Hunt",
            source_kind="rss",
            title="Tool",
            url="https://example.com/tool?utm_source=ph",
            summary="A tool",
            published_at=self.now,
            evidence_urls=["https://example.com/tool"],
            config=self.config,
            now=self.now,
        )
        second = discovery.normalize_candidate(
            source="Hacker News",
            source_kind="hacker_news",
            title="Tool discussion",
            url="https://example.com/tool",
            summary="Useful discussion",
            published_at=self.now,
            evidence_urls=["https://news.ycombinator.com/item?id=123"],
            config=self.config,
            now=self.now,
        )
        merged = discovery.merge_duplicates([first, second])
        self.assertEqual(len(merged), 1)
        self.assertIn("Product Hunt", merged[0]["discovered_via"])
        self.assertIn("Hacker News", merged[0]["discovered_via"])
        self.assertIn("https://news.ycombinator.com/item?id=123", merged[0]["evidence_urls"])

    def test_report_is_research_only_and_creates_json_and_markdown(self):
        candidate = discovery.normalize_candidate(
            source="Product Hunt",
            source_kind="rss",
            title="Digital product helper",
            url="https://example.com/digital-product-helper",
            summary="A technical helper for selling downloadable products",
            published_at=self.now,
            category_hint="commerce_and_digital_products",
            config=self.config,
            now=self.now,
        )
        with tempfile.TemporaryDirectory() as temporary:
            md, js = discovery.write_report(
                [candidate],
                [{"source": "Test", "items_kept": 1, "status": "ok", "kind": "rss"}],
                self.config,
                14,
                10,
                Path(temporary),
            )
            self.assertTrue(md.exists())
            self.assertTrue(js.exists())
            report_text = md.read_text(encoding="utf-8")
            self.assertIn("nothing was posted to X", report_text)
            self.assertIn("Human editorial gate", report_text)


if __name__ == "__main__":
    unittest.main()
