# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-29T10:56:11+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 206
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
| Hacker News · hn-automation-api | 2 | ok |
| Hacker News · hn-creator-business | 0 | ok |
| Hacker News · hn-digital-downloads-templates | 0 | ok |
| Hacker News · hn-digital-products | 2 | ok |
| Hacker News · hn-ecommerce-payments | 0 | ok |
| Hacker News · hn-indie-business-revenue | 0 | ok |
| Hacker News · hn-marketing-distribution | 0 | ok |
| Hacker News · hn-security-selfhost | 0 | ok |
| Hacker News · hn-seller-operations | 0 | ok |
| Hacker News · hn-shopify | 9 | ok |
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
- Repositories seen in this discovery run: 112
- Previously tracked repositories refreshed outside search results: 88
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 17
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| obsei/obsei | yes | 200 | https://github.com/obsei/obsei |
| ChronoAIProject/NyxID | yes | 200 | https://github.com/ChronoAIProject/NyxID |
| Show HN: Interview your analysts instead of auto-generating a semantic layer | yes | 200 | https://github.com/nodal-data/nodal-context |

## Selected draft candidates

### Draft option 1: obsei/obsei

- Category: ai_and_automation
- Source: GitHub Search
- Format: tool_discovery
- Editorial score: 8.25/10
- Model scores: timeliness 9/10, usefulness 8/10, novelty 7/10, evidence 9/10, insight 8/10
- Independent editor scores: {"clarity_score": 9, "technical_coherence_score": 9, "takeaway_value_score": 8, "source_faithfulness_score": 9, "originality_score": 8, "reason": "Clear, technically accurate, and adds a useful verification step.", "passed": true}
- Live primary page: https://github.com/obsei/obsei (HTTP 200)
- Exact source evidence: “strips PII from feedback before any LLM sees it”
- Why this angle: Shows privacy‑first design and a concrete test for redaction.
- Editorial takeaway: Verify redaction by inspecting sample logs before training.
- Source: https://github.com/obsei/obsei

**Claim-by-claim source quotes:**

- obsei strips PII from feedback before any LLM sees it ← “strips PII from feedback before any LLM sees it”

Proposed post (not published):

> obsei strips PII from feedback before any LLM sees it. Verify redaction by inspecting sample logs before training. https://github.com/obsei/obsei

- Length: 145/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- ChronoAIProject/NyxID: Takeaway implies an interaction/causal relationship between source-listed features that the primary page does not establish. Reframe it as an explicit conditional test of the reader's own integration.; A supporting quote does not share enough wording with its stated claim; Supporting quotes cover only 43% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: NyxID injects credentials automatically into proxied API requests. Test that no raw keys appear in request headers during agent calls. https://github.com/ChronoAIProject/NyxID
  - Model evidence quote: “injects credentials automatically”
  - Claim support: NyxID injects credentials automatically into proxied API requests ← “injects credentials automatically”
- Show HN: Interview your analysts instead of auto-generating a semantic layer: Editorial takeaway needs a concrete test, trade-off, risk, comparison, or next step.
  - Rejected text: nodal-context provides open‑source business context for data analytics. Ensure context tables match your semantic layer before use. https://github.com/nodal-data/nodal-context
  - Model evidence quote: “Open source business context for your data analytics”
  - Claim support: nodal-context provides open‑source business context for data analytics ← “Open source business context for your data analytics”

## Top discovery candidates considered

- obsei/obsei | GitHub Search | ai_and_automation | raw 69, adjusted 73 | current stars 1441 | GitHub star trend: building baseline | https://github.com/obsei/obsei
- ChronoAIProject/NyxID | GitHub Search | ai_and_automation | raw 68, adjusted 72 | current stars 40 | GitHub star trend: building baseline | https://github.com/ChronoAIProject/NyxID
- Show HN: Interview your analysts instead of auto-generating a semantic layer | Hacker News | product_and_workflow_tools | raw 69, adjusted 71 | https://github.com/nodal-data/nodal-context

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
