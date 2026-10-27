# Content Discovery Source Expansion

## Scope

This document describes the sources Legivox uses to discover useful public content for its X publishing pipeline. It is not the internal market-research system for deciding which digital product we should build. No product-market validation, private marketplace research, or preorder tracking is implemented here.

A source can surface a story; it does not automatically make that story accurate, useful, timely, or publishable. Candidates must pass the existing primary-source and editorial quality gates before they reach the post plan.

## Automated RSS and Atom sources

| Source | Editorial use | Limitations |
|---|---|---|
| Console.dev | Curated developer tools and workflows | Feed selection is editorially curated; still verify the tool's own page |
| Product Hunt | New product launches and product/workflow ideas | Launch ranking and votes do not establish product quality |
| Shopify Developer Changelog | Shopify APIs, platform changes and developer implications | One lane only; it is not representative of all Shopify merchant issues |
| Shopify Community | Merchant questions, feature requests and practical workarounds | Public discussion is self-selected; a single post is not a universal problem |
| Stripe Blog | Payment infrastructure, APIs, checkout and commerce changes | Company-authored source; distinguish product announcements from independent analysis |
| Ahrefs Blog | SEO, search visibility and digital marketing lessons | Vendor-authored material; label claims and use primary evidence when available |
| WooCommerce Blog | Ecommerce tooling, store operations and platform changes | Vendor-authored source; distinguish general guidance from product announcements |
| Indie Hackers via RSS.app | Founder workflows, product launches and distribution lessons | Unofficial third-party feed; availability and summaries are best-effort, so verify the original story and disable the feed if it becomes unreliable |

The source registry is `data/discovery_sources.json`. RSS feed diagnostics include item counts, connection/parse failures and status. A feed returning zero eligible items is not necessarily broken; it may have no recent items matching the configured lookback. A fetch or parse error, however, should be reviewed before production rollout.

## Search and directory sources

| Source | Coverage | How Legivox should interpret it |
|---|---|---|
| GitHub repository search | Developer tools, AI/agents, automation, commerce, creator infrastructure, seller workflows, SEO/growth and self-hosting | Useful for finding projects and releases; lifetime stars are not proof that a project is new or excellent |
| Hacker News / Show HN | Discussions and demonstrations related to tools, commerce, automation, analytics, security and indie work | Upvotes/comments help rank discovery candidates, not verify their claims |
| WordPress.org Plugin Directory API | Plugins for digital downloads, ecommerce, inventory, memberships and marketing analytics | Active installs, downloads and ratings are public adoption/feedback context; they are not paid-revenue data |

The discovery report applies preview-only caps of three candidates per source group and eight per editorial category, so reviewers can inspect a broader sample instead of seeing only the highest-scoring source dominate. These caps do not affect the hourly publishing selector. Shopify Community RSS is currently kept as a discovery-only signal because live primary-page verification from GitHub Actions returned HTTP 403 in repeated checks on 2026-10-26. The unofficial Indie Hackers feed also remains discovery-only after repeated candidate headline/primary-page mismatches. Both sources are excluded from automated drafting until primary-page verification is reliable; do not bypass the primary-source gate to force them into posts. WordPress Plugin Directory last-updated timestamps remain usable for a maintenance freshness check, but do not receive breaking-news recency points, and install/rating/download counts are capped as weak ranking signals. The current registry contains 12 GitHub queries, 12 Hacker News queries, 5 WordPress Plugin Directory searches and 8 RSS/Atom feeds. Several niche Hacker News queries may return zero eligible items in a given window. This is acceptable when the search is quiet, but the review report should be monitored for persistent low-yield queries that consume quota without adding useful candidates. The first preview exposed a parse error from the earlier unofficial Indie Hackers endpoint. It was replaced with an RSS.app feed; the latest live preview successfully parsed it and returned 5 items, with all 37 source adapters/queries responding. Because it is third-party, recheck its health on later runs.

## Separate from content discovery

The following are not connected by this registry: logged-in Etsy Marketplace Insights, Etsy/Gumroad marketplace review mining, App Store review exports, Google Trends exports, private sales analytics, buyer interviews and preorder tracking. Those belong to a separate internal product-research process and must not be described as hourly automated sources.

YouTube creators and engineering/business publications may be editorial inspiration, but unless they are listed in the source registry or an adapter, they are not automated inputs.

## Dry-run and release gates

Before enabling source changes in production:

1. Run JSON validation and the full Python unit/integration suite.
2. Run the read-only discovery preview on the branch and inspect the source-health table. Do not accept a feed merely because the workflow itself exited successfully.
3. Confirm every new source either returns plausible recent items or is explicitly documented as unavailable/low-yield and removed or corrected. Check the actual candidate titles, not only the source-health status.
4. Inspect the diverse preview candidates for relevance, duplicate noise, weakly supported claims, source concentration and obvious personal/support-ticket details that should not be amplified.
5. Keep PR validation read-only. Do not dispatch the state-writing hourly dry-run against this feature branch: it persists the latest report and star snapshots to `legivox-hourly-state`, which is also read by the production publisher. The PR preview tests the current source registry without changing that shared state; the normal scheduled quality-gated run should exercise the new registry after merge.
6. Review the draft PR and its final passing workflow run before merging. The discovery-preview workflow does not use X credentials or publish. Production source changes take effect only after merge.

The score ranks candidates for review; it is not a claim that the project is high quality, secure, commercially successful, or suitable for every audience.
