# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-28T17:51:36+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 181
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
| Hacker News · hn-analytics-growth | 10 | ok |
| Hacker News · hn-automation-api | 1 | ok |
| Hacker News · hn-creator-business | 0 | ok |
| Hacker News · hn-digital-downloads-templates | 0 | ok |
| Hacker News · hn-digital-products | 2 | ok |
| Hacker News · hn-ecommerce-payments | 0 | ok |
| Hacker News · hn-indie-business-revenue | 0 | ok |
| Hacker News · hn-marketing-distribution | 0 | ok |
| Hacker News · hn-security-selfhost | 0 | ok |
| Hacker News · hn-seller-operations | 0 | ok |
| Hacker News · hn-shopify | 6 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Ahrefs Blog | 6 | ok |
| Console.dev | 12 | ok |
| Indie Hackers (unofficial third-party feed) | 5 | ok |
| Product Hunt | 39 | ok |
| Shopify Community | 30 | ok |
| Shopify Developer Changelog | 18 | ok |
| Stripe Blog | 3 | ok |
| WooCommerce Blog | 3 | ok |
| WordPress Plugin Directory · wp-digital-downloads | 10 | ok |
| WordPress Plugin Directory · wp-ecommerce | 10 | ok |
| WordPress Plugin Directory · wp-inventory-management | 10 | ok |
| WordPress Plugin Directory · wp-marketing-analytics | 10 | ok |
| WordPress Plugin Directory · wp-membership-creators | 10 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 106
- Previously tracked repositories refreshed outside search results: 94
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 18
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| Show HN: Multi-platform remote-control for any harness | no | — | Primary page title/content does not sufficiently match the candidate headline. |
| chattermate/chattermate.chat | yes | 200 | https://github.com/chattermate/chattermate.chat |
| spree/spree | yes | 200 | https://github.com/spree/spree |

## Selected draft candidates

### Draft option 1: chattermate/chattermate.chat

- Category: commerce_and_digital_products
- Source: GitHub Search
- Format: tool_discovery
- Editorial score: 8.4/10
- Model scores: timeliness 10/10, usefulness 8/10, novelty 6/10, evidence 9/10, insight 8/10
- Independent editor scores: {"clarity_score": 8, "technical_coherence_score": 8, "takeaway_value_score": 8, "source_faithfulness_score": 8, "originality_score": 8, "reason": "Clear, technically coherent, source‑faithful, and adds a useful test suggestion.", "passed": true}
- Live primary page: https://github.com/chattermate/chattermate.chat (HTTP 200)
- Exact source evidence: “GitHub - chattermate/chattermate.chat: Open-source AI customer support platform — AI chatbot with human handoff, Shopify & Slack integrations, visual workflow builder.”
- Why this angle: The repository description explicitly lists human handoff and Shopify integration, and a practical test ensures the escalation path works.
- Editorial takeaway: Test handoff flow by simulating a ticket that escalates to a human agent.
- Source: https://github.com/chattermate/chattermate.chat

**Claim-by-claim source quotes:**

- chattermate.chat offers AI chatbot with human handoff and Shopify integration. ← “GitHub - chattermate/chattermate.chat: Open-source AI customer support platform — AI chatbot with human handoff, Shopify & Slack integrations, visual workflow builder.”

Proposed post (not published):

> chattermate.chat offers AI chatbot with human handoff and Shopify integration. Test handoff flow by simulating a ticket that escalates to a human agent. https://github.com/chattermate/chattermate.chat

- Length: 200/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- Show HN: Multi-platform remote-control for any harness: Primary page title/content does not sufficiently match the candidate headline.
- spree/spree: A supporting quote does not share enough wording with its stated claim; Supporting quotes cover only 20% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: spree provides a self‑hosted DTC and B2B commerce platform with a Next.js storefront. Run the Next.js demo locally before deploying to production. https://github.com/spree/spree
  - Model evidence quote: “production-ready Next.js storefront”
  - Claim support: The source says capability X ← “production-ready Next.js storefront”

## Top discovery candidates considered

- Show HN: Multi-platform remote-control for any harness | Hacker News | product_and_workflow_tools | raw 64, adjusted 66 | https://github.com/tinybig-ai/jep
- chattermate/chattermate.chat | GitHub Search | commerce_and_digital_products | raw 70, adjusted 64 | current stars 147 | GitHub star trend: building baseline | https://github.com/chattermate/chattermate.chat
- spree/spree | GitHub Search | commerce_and_digital_products | raw 70, adjusted 64 | current stars 15786 | GitHub star trend: building baseline | https://github.com/spree/spree

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
