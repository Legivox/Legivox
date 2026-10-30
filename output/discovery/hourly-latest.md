# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-30T15:03:58+05:30
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
| Hacker News · hn-automation-api | 1 | ok |
| Hacker News · hn-creator-business | 0 | ok |
| Hacker News · hn-digital-downloads-templates | 0 | ok |
| Hacker News · hn-digital-products | 1 | ok |
| Hacker News · hn-ecommerce-payments | 0 | ok |
| Hacker News · hn-indie-business-revenue | 0 | ok |
| Hacker News · hn-marketing-distribution | 0 | ok |
| Hacker News · hn-security-selfhost | 0 | ok |
| Hacker News · hn-seller-operations | 0 | ok |
| Hacker News · hn-shopify | 10 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Ahrefs Blog | 7 | ok |
| Console.dev | 11 | ok |
| Indie Hackers (unofficial third-party feed) | 5 | ok |
| Product Hunt | 43 | ok |
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
- Repositories with a 20–36 hour comparison baseline: 20
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| gotempsh/temps | yes | 200 | https://github.com/gotempsh/temps |
| kagura-ai/memory-cloud | yes | 200 | https://github.com/kagura-ai/memory-cloud |
| How Stable Are AI Citations? 10 Things We Learned Tracking 37,500 Citations | yes | 200 | https://ahrefs.com/blog/how-stable-are-ai-citations/ |

## Selected draft candidates

### Draft option 1: How Stable Are AI Citations? 10 Things We Learned Tracking 37,500 Citations

- Category: data_and_growth
- Source: Ahrefs Blog
- Format: practical_workflow
- Editorial score: 8.1/10
- Model scores: timeliness 8/10, usefulness 8/10, novelty 7/10, evidence 9/10, insight 8/10
- Independent editor scores: {"clarity_score": 9, "technical_coherence_score": 9, "takeaway_value_score": 8, "source_faithfulness_score": 9, "originality_score": 8, "reason": "Clear, coherent, faithful to source, and offers a concrete monitoring recommendation.", "passed": true}
- Live primary page: https://ahrefs.com/blog/how-stable-are-ai-citations/ (HTTP 200)
- Exact source evidence: “Half of AI citations disappear the next day, and most come back.”
- Why this angle: The article quantifies citation volatility, guiding a monitoring strategy.
- Editorial takeaway: Set a daily monitor; if a citation drops >50%, refresh the content.
- Source: https://ahrefs.com/blog/how-stable-are-ai-citations/

**Claim-by-claim source quotes:**

- Half of AI citations disappear the next day, and most return. ← “Half of AI citations disappear the next day, and most come back.”

Proposed post (not published):

> Half of AI citations disappear the next day, and most return. Set a daily monitor; if a citation drops >50%, refresh the content. https://ahrefs.com/blog/how-stable-are-ai-citations/

- Length: 182/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- gotempsh/temps: The factual opening bundles multiple features; narrow it to one capability.
  - Rejected text: temps offers 440+ CLI operations covering deployments, analytics, and error tracking. Run a deployment test and verify error logs appear to confirm end‑to‑end coverage. https://github.com/gotempsh/temps
  - Model evidence quote: “440+ CLI operations with drop-in skills for Claude Code, Codex & OpenCode — deployments, analytics, session replay, error tracking, OpenTelemetry, email, sandboxes & AI gateway in one self-hosted Rust binary.”
  - Claim support: temps offers 440+ CLI operations covering deployments, analytics, and error tracking. ← “440+ CLI operations with drop-in skills for Claude Code, Codex & OpenCode — deployments, analytics, session replay, error tracking, OpenTelemetry, email, sandboxes & AI gateway in one self-hosted Rust binary.”
- kagura-ai/memory-cloud: Fact sentence is too long; narrow it to one source-backed capability.; Editorial takeaway is not specific enough to this candidate's technical/product details.
  - Rejected text: memory‑cloud is a self‑hosted MCP server that learns from searches using hybrid search and a neural memory graph. Run the same query twice and compare result diversity to confirm learning. https://github.com/kagura-ai/memory-cloud
  - Model evidence quote: “Self-hosted MCP server that gets smarter every time you search: hybrid search + a neural memory graph that learns.”
  - Claim support: memory‑cloud is a self‑hosted MCP server that learns from searches using hybrid search and a neural memory graph. ← “Self-hosted MCP server that gets smarter every time you search: hybrid search + a neural memory graph that learns.”

## Top discovery candidates considered

- gotempsh/temps | GitHub Search | data_and_growth | raw 72, adjusted 66 | current stars 880 | GitHub star trend: building baseline | https://github.com/gotempsh/temps
- kagura-ai/memory-cloud | GitHub Search | security_and_self_hosting | raw 66, adjusted 60 | current stars 13 | GitHub star trend: building baseline | https://github.com/kagura-ai/memory-cloud
- How Stable Are AI Citations? 10 Things We Learned Tracking 37,500 Citations | Ahrefs Blog | data_and_growth | raw 60, adjusted 60 | https://ahrefs.com/blog/how-stable-are-ai-citations/

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
