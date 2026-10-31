# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-31T14:53:14+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 194
- Independent editorial review: 1 draft(s) passed / 0 rejected
- Drafts passing local checks: 1
- Outcome: **dry_run_passed**
- Decision reason: At least one draft passed live primary-source, evidence, originality, novelty, URL and length checks. The top-ranked draft would be eligible for the future automated post flow; dry-run mode did not publish it.

## Source health

| Source | Items kept | Result |
|---|---:|---|
| GitHub Search · github-ai-agent-tools | 10 | ok |
| GitHub Search · github-analytics-seo | 10 | ok |
| GitHub Search · github-creator-infrastructure | 10 | ok |
| GitHub Search · github-developer-tools | 10 | ok |
| GitHub Search · github-digital-product-tools | 10 | ok |
| GitHub Search · github-ecommerce-digital-products | 10 | ok |
| GitHub Search · github-marketing-distribution | 10 | ok |
| GitHub Search · github-mcp-servers | 10 | ok |
| GitHub Search · github-self-hosted | 10 | ok |
| GitHub Search · github-seller-operations | 10 | ok |
| GitHub Search · github-shopify-commerce | 10 | ok |
| GitHub Search · github-workflow-automation | 10 | ok |
| Hacker News · hn-analytics-growth | 9 | ok |
| Hacker News · hn-automation-api | 1 | ok |
| Hacker News · hn-creator-business | 0 | ok |
| Hacker News · hn-digital-downloads-templates | 0 | ok |
| Hacker News · hn-digital-products | 1 | ok |
| Hacker News · hn-ecommerce-payments | 0 | ok |
| Hacker News · hn-indie-business-revenue | 0 | ok |
| Hacker News · hn-marketing-distribution | 0 | ok |
| Hacker News · hn-security-selfhost | 0 | ok |
| Hacker News · hn-seller-operations | 0 | ok |
| Hacker News · hn-shopify | 8 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Ahrefs Blog | 8 | ok |
| Console.dev | 11 | ok |
| Indie Hackers (unofficial third-party feed) | 5 | ok |
| Product Hunt | 42 | ok |
| Shopify Community | 30 | ok |
| Shopify Developer Changelog | 30 | ok |
| Stripe Blog | 3 | ok |
| WooCommerce Blog | 3 | ok |
| WordPress Plugin Directory · wp-digital-downloads | 10 | ok |
| WordPress Plugin Directory · wp-ecommerce | 10 | ok |
| WordPress Plugin Directory · wp-inventory-management | 10 | ok |
| WordPress Plugin Directory · wp-marketing-analytics | 10 | ok |
| WordPress Plugin Directory · wp-membership-creators | 10 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 107
- Previously tracked repositories refreshed outside search results: 93
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 18
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| leepokai/Codync | yes | 200 | https://github.com/leepokai/Codync |
| Show HN: KuralHub 1.0, Speech emotion datasets for 70 languages in one place | yes | 200 | https://aaivu.github.io/KuralHub/datasets.html |
| Show HN: Readeck sync for Kobo's stock reader | yes | 200 | https://github.com/fkaduk/kobodeck |

## Selected draft candidates

### Draft option 1: leepokai/Codync

- Category: security_and_self_hosting
- Source: GitHub Search
- Format: tool_discovery
- Editorial score: 8.4/10
- Model scores: timeliness 10/10, usefulness 8/10, novelty 7/10, evidence 9/10, insight 8/10
- Independent editor scores: {"clarity_score": 9, "technical_coherence_score": 9, "takeaway_value_score": 8, "source_faithfulness_score": 9, "originality_score": 8, "reason": "Clear, accurate claim with source support; actionable takeaway is relevant and not merely restating the headline.", "passed": true}
- Live primary page: https://github.com/leepokai/Codync (HTTP 200)
- Exact source evidence: “Open source Grok Bot alternative, Bring your own agent and subscription: message Claude Code, Codex, Gemini CLI, Cursor, Copilot and 40+ AI agents as bots”
- Why this angle: The primary source explicitly lists 40+ AI agents, confirming Codync’s broad agent support. A practical test ensures the CLI routing works for each provider.
- Editorial takeaway: Run a quick agent switch test to confirm the CLI can route to each AI provider.
- Source: https://github.com/leepokai/Codync

**Claim-by-claim source quotes:**

- Codync is an open source Grok Bot alternative that supports 40+ AI agents. ← “Open source Grok Bot alternative, Bring your own agent and subscription: message Claude Code, Codex, Gemini CLI, Cursor, Copilot and 40+ AI agents as bots”

Proposed post (not published):

> Codync is an open source Grok Bot alternative that supports 40+ AI agents. Run a quick agent switch test to confirm the CLI can route to each AI provider. https://github.com/leepokai/Codync

- Length: 189/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- Show HN: KuralHub 1.0, Speech emotion datasets for 70 languages in one place: Editorial takeaway is not specific enough to this candidate's technical/product details.; A supporting quote does not share enough wording with its stated claim; Unsupported numeric claim(s): 11; Supporting quotes cover only 33% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: KuralHub catalogs 90 speech emotion datasets across 70 languages with benchmark results for 11 models. Validate dataset license compliance before training to avoid downstream legal issues. https://aaivu.github.io/KuralHub/datasets.html
  - Model evidence quote: “90 SER datasets with emotion labels, size, licence and access links, organised by language.”
  - Claim support: KuralHub catalogs 90 speech emotion datasets across 70 languages with benchmark results for 11 models. ← “90 SER datasets with emotion labels, size, licence and access links, organised by language”
- Show HN: Readeck sync for Kobo's stock reader: Editorial takeaway is too long; keep the analysis concrete and concise.
  - Rejected text: Kobodeck is a minimalist Readeck article downloader for Kobo e-readers. Test download and sync on a test Kobo to ensure article formatting matches device expectations. https://github.com/fkaduk/kobodeck
  - Model evidence quote: “A minimalist Readeck article downloader for Kobo e-readers.”
  - Claim support: Kobodeck is a minimalist Readeck article downloader for Kobo e-readers. ← “A minimalist Readeck article downloader for Kobo e-readers”

## Top discovery candidates considered

- leepokai/Codync | GitHub Search | security_and_self_hosting | raw 72, adjusted 66 | current stars 1110 | GitHub star trend: building baseline | https://github.com/leepokai/Codync
- Show HN: KuralHub 1.0, Speech emotion datasets for 70 languages in one place | Hacker News | product_and_workflow_tools | raw 63, adjusted 65 | https://aaivu.github.io/KuralHub/datasets.html
- Show HN: Readeck sync for Kobo's stock reader | Hacker News | product_and_workflow_tools | raw 63, adjusted 65 | https://github.com/fkaduk/kobodeck

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
