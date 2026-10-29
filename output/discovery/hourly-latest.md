# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-29T08:00:46+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 205
- Independent editorial review: 2 draft(s) passed / 0 rejected
- Drafts passing local checks: 2
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
| Hacker News · hn-analytics-growth | 10 | ok |
| Hacker News · hn-automation-api | 2 | ok |
| Hacker News · hn-creator-business | 0 | ok |
| Hacker News · hn-digital-downloads-templates | 0 | ok |
| Hacker News · hn-digital-products | 2 | ok |
| Hacker News · hn-ecommerce-payments | 0 | ok |
| Hacker News · hn-indie-business-revenue | 0 | ok |
| Hacker News · hn-marketing-distribution | 0 | ok |
| Hacker News · hn-security-selfhost | 0 | ok |
| Hacker News · hn-seller-operations | 0 | ok |
| Hacker News · hn-shopify | 10 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Ahrefs Blog | 6 | ok |
| Console.dev | 12 | ok |
| Indie Hackers (unofficial third-party feed) | 5 | ok |
| Product Hunt | 38 | ok |
| Shopify Community | 30 | ok |
| Shopify Developer Changelog | 31 | ok |
| Stripe Blog | 2 | ok |
| WooCommerce Blog | 3 | ok |
| WordPress Plugin Directory · wp-digital-downloads | 10 | ok |
| WordPress Plugin Directory · wp-ecommerce | 10 | ok |
| WordPress Plugin Directory · wp-inventory-management | 10 | ok |
| WordPress Plugin Directory · wp-marketing-analytics | 10 | ok |
| WordPress Plugin Directory · wp-membership-creators | 10 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 110
- Previously tracked repositories refreshed outside search results: 90
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 17
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| n8n-io/n8n | yes | 200 | https://github.com/n8n-io/n8n |
| Show HN: Simple DeepSeek web search CLI written in TypeScript (fast/cheap) | no | — | Primary source returned HTTP 403. |
| Shopify Flow: manage automations through AI Toolkit | yes | 200 | https://shopify.dev/changelog/posts/shopify-flow-manage-automations-through-admin-api |

## Selected draft candidates

### Draft option 1: Shopify Flow: manage automations through AI Toolkit

- Category: commerce_and_digital_products
- Source: Shopify Developer Changelog
- Format: practical_workflow
- Editorial score: 9.1/10
- Model scores: timeliness 10/10, usefulness 9/10, novelty 8/10, evidence 10/10, insight 9/10
- Independent editor scores: {"clarity_score": 9, "technical_coherence_score": 9, "takeaway_value_score": 8, "source_faithfulness_score": 9, "originality_score": 8, "reason": "Clear, technically accurate, and adds a useful permission check.", "passed": true}
- Live primary page: https://shopify.dev/changelog/posts/shopify-flow-manage-automations-through-admin-api (HTTP 200)
- Exact source evidence: “You can now use an external agent to manage your Shopify Flow workflows through AI Toolkit.”
- Why this angle: The changelog confirms the new agent‑based management feature, and the takeaway advises a security‑focused validation step.
- Editorial takeaway: Check agent permissions are limited to your store before enabling automation.
- Source: https://shopify.dev/changelog/posts/shopify-flow-manage-automations-through-admin-api

**Claim-by-claim source quotes:**

- Shopify Flow now lets external agents manage workflows via the AI Toolkit. ← “You can now use an external agent to manage your Shopify Flow workflows through AI Toolkit.”

Proposed post (not published):

> Shopify Flow now lets external agents manage workflows via the AI Toolkit. Check agent permissions are limited to your store before enabling automation. https://shopify.dev/changelog/posts/shopify-flow-manage-automations-through-admin-api

- Length: 238/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

### Draft option 2: n8n-io/n8n

- Category: ai_and_automation
- Source: GitHub Search
- Format: tool_discovery
- Editorial score: 8.65/10
- Model scores: timeliness 10/10, usefulness 8/10, novelty 7/10, evidence 10/10, insight 8/10
- Independent editor scores: {"clarity_score": 9, "technical_coherence_score": 9, "takeaway_value_score": 8, "source_faithfulness_score": 9, "originality_score": 8, "reason": "Clear, accurate, and provides a practical next step.", "passed": true}
- Live primary page: https://github.com/n8n-io/n8n (HTTP 200)
- Exact source evidence: “Fair-code workflow automation platform with native AI capabilities.”
- Why this angle: The primary source explicitly states the platform’s AI feature and fair‑code model, enabling a concrete test of AI node integration.
- Editorial takeaway: Run a sample AI node flow to confirm integration before production.
- Source: https://github.com/n8n-io/n8n

**Claim-by-claim source quotes:**

- n8n is a fair‑code workflow automation platform with native AI capabilities. ← “Fair-code workflow automation platform with native AI capabilities.”

Proposed post (not published):

> n8n is a fair‑code workflow automation platform with native AI capabilities. Run a sample AI node flow to confirm integration before production. https://github.com/n8n-io/n8n

- Length: 174/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- Show HN: Simple DeepSeek web search CLI written in TypeScript (fast/cheap): Primary source returned HTTP 403.

## Top discovery candidates considered

- n8n-io/n8n | GitHub Search | ai_and_automation | raw 69, adjusted 88 | current stars 208923 | GitHub stars +99 over about 21.1h | https://github.com/n8n-io/n8n
- Show HN: Simple DeepSeek web search CLI written in TypeScript (fast/cheap) | Hacker News | product_and_workflow_tools | raw 77, adjusted 79 | https://www.npmjs.com/package/deepseek-search-cli
- Shopify Flow: manage automations through AI Toolkit | Shopify Developer Changelog | commerce_and_digital_products | raw 78, adjusted 78 | https://shopify.dev/changelog/posts/shopify-flow-manage-automations-through-admin-api

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
