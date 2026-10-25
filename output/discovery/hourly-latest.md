# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-25T21:40:08+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 85
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
| GitHub Search · github-ecommerce-digital-products | 10 | ok |
| GitHub Search · github-mcp-servers | 10 | ok |
| GitHub Search · github-self-hosted | 10 | ok |
| GitHub Search · github-shopify-commerce | 10 | ok |
| GitHub Search · github-workflow-automation | 10 | ok |
| Hacker News · hn-analytics-growth | 10 | ok |
| Hacker News · hn-automation-api | 1 | ok |
| Hacker News · hn-creator-business | 0 | ok |
| Hacker News · hn-digital-products | 1 | ok |
| Hacker News · hn-ecommerce-payments | 0 | ok |
| Hacker News · hn-security-selfhost | 0 | ok |
| Hacker News · hn-shopify | 10 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Console.dev | 12 | ok |
| Product Hunt | 42 | ok |
| Shopify Developer Changelog | 10 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 83
- Previously tracked repositories refreshed outside search results: 117
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 13
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| Show HN: Swingback, get feedback from your user for free | yes | 200 | https://swingback.dev |
| MikkoParkkola/mcp-gateway | yes | 200 | https://github.com/MikkoParkkola/mcp-gateway |
| AgentGrid.io | no | — | Primary source returned HTTP 403. |

## Selected draft candidates

### Draft option 1: Show HN: Swingback, get feedback from your user for free

- Category: product_and_workflow_tools
- Source: Hacker News
- Format: short
- Editorial score: 8.8/10
- Model scores: timeliness 8/10, usefulness 9/10, novelty 6/10, evidence 10/10, insight 9/10
- Independent editor scores: {"clarity_score": 8, "technical_coherence_score": 8, "takeaway_value_score": 8, "source_faithfulness_score": 9, "originality_score": 7, "reason": "Clear, accurate claim with direct source support and a concrete testable takeaway.", "passed": true}
- Live primary page: https://swingback.dev (HTTP 200)
- Exact source evidence: “Swingback: user feedback tool with voting, roadmap and changelog Collect user feedback in a portal and an in-app widget, sync feature requests with GitHub and Linear, and tell every voter when you ship.”
- Why this angle: The primary page explicitly states sync with GitHub and Linear; the takeaway focuses on verifying that relationship.
- Editorial takeaway: Test that a new vote creates a GitHub issue to confirm sync.
- Source: https://swingback.dev

**Claim-by-claim source quotes:**

- Swingback syncs feature requests to GitHub and Linear. ← “Swingback: user feedback tool with voting, roadmap and changelog Collect user feedback in a portal and an in-app widget, sync feature requests with GitHub and Linear, and tell every voter when you ship.”

Proposed post (not published):

> Swingback syncs feature requests to GitHub and Linear. Test that a new vote creates a GitHub issue to confirm sync. https://swingback.dev

- Length: 137/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

### Draft option 2: MikkoParkkola/mcp-gateway

- Category: ai_and_automation
- Source: GitHub Search
- Format: short
- Editorial score: 8.8/10
- Model scores: timeliness 8/10, usefulness 9/10, novelty 6/10, evidence 10/10, insight 9/10
- Independent editor scores: {"clarity_score": 8, "technical_coherence_score": 8, "takeaway_value_score": 8, "source_faithfulness_score": 9, "originality_score": 7, "reason": "Accurate description of Rust binary and actionable verification step, fully supported by source.", "passed": true}
- Live primary page: https://github.com/MikkoParkkola/mcp-gateway (HTTP 200)
- Exact source evidence: “Self-hosted MCP gateway and proxy in one Rust binary, 100+ API integrations built in, one-command import of existing servers.”
- Why this angle: The source confirms a one‑command import; the takeaway tests that import.
- Editorial takeaway: Verify that a one‑command import registers existing servers before deployment.
- Source: https://github.com/MikkoParkkola/mcp-gateway

**Claim-by-claim source quotes:**

- mcp‑gateway is a Rust binary that proxies MCP servers. ← “Self-hosted MCP gateway and proxy in one Rust binary, 100+ API integrations built in, one-command import of existing servers.”

Proposed post (not published):

> mcp‑gateway is a Rust binary that proxies MCP servers. Verify that a one‑command import registers existing servers before deployment. https://github.com/MikkoParkkola/mcp-gateway

- Length: 178/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: yes
- Repaired drafts submitted: 2
- Repaired drafts that passed local validation: 2
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- AgentGrid.io: Primary source returned HTTP 403.
- Show HN: Swingback, get feedback from your user for free: Takeaway implies an interaction/causal relationship between source-listed features that the primary page does not establish. Reframe it as an explicit conditional test of the reader's own integration.; Fact sentence is too long; narrow it to one source-backed capability.
  - Rejected text: Swingback lets you collect user feedback via a portal and in‑app widget, syncing requests with GitHub and Linear. Run a test that a new vote triggers a GitHub issue creation to confirm sync works. https://swingback.dev
  - Model evidence quote: “Collect user feedback in a portal and an in‑app widget, sync feature requests with GitHub and Linear”
  - Claim support: Swingback lets you collect user feedback via a portal and in‑app widget, syncing requests with GitHub and Linear ← “Collect user feedback in a portal and an in‑app widget, sync feature requests with GitHub and Linear”
- MikkoParkkola/mcp-gateway: Fact sentence is too long; narrow it to one source-backed capability.; Editorial takeaway is too long; keep the analysis concrete and concise.
  - Rejected text: mcp‑gateway is a Rust binary that proxies MCP servers, offering a fixed context cost and 100+ built‑in API integrations. Verify that a one‑command import correctly registers existing servers before deploying to production. https://github.com/MikkoParkkola/mcp-gateway
  - Model evidence quote: “Self‑hosted MCP gateway and proxy in one Rust binary, 100+ API integrations built in, one‑command import of existing servers”
  - Claim support: mcp‑gateway is a Rust binary that proxies MCP servers, offering a fixed context cost and 100+ built‑in API integrations ← “Self‑hosted MCP gateway and proxy in one Rust binary, 100+ API integrations built in, one‑command import of existing servers”

## Top discovery candidates considered

- Show HN: Swingback, get feedback from your user for free | Hacker News | product_and_workflow_tools | raw 66, adjusted 68 | https://swingback.dev
- MikkoParkkola/mcp-gateway | GitHub Search | ai_and_automation | raw 75, adjusted 51 | current stars 85 | GitHub star trend: building baseline | https://github.com/MikkoParkkola/mcp-gateway
- AgentGrid.io | Product Hunt | product_and_workflow_tools | raw 51, adjusted 51 | https://www.producthunt.com/products/agentgrid-io

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
