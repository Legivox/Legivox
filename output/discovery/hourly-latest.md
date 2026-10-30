# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-30T19:13:46+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 195
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
| Hacker News · hn-analytics-growth | 6 | ok |
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
- Repositories seen in this discovery run: 108
- Previously tracked repositories refreshed outside search results: 92
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 19
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| Show HN: Ocel – Deploy apps to your AWS,GCP or VPS with infra from code | yes | 200 | https://github.com/ocelhq/ocel |
| Show HN: SpecDeck – Bring coding agent decisions back into the spec | yes | 200 | https://specdeck.ai/ |
| snapotter-hq/SnapOtter | yes | 200 | https://github.com/snapotter-hq/SnapOtter |

## Selected draft candidates

### Draft option 1: Show HN: Ocel – Deploy apps to your AWS,GCP or VPS with infra from code

- Category: product_and_workflow_tools
- Source: Hacker News
- Format: tool_discovery
- Editorial score: 8.65/10
- Model scores: timeliness 10/10, usefulness 8/10, novelty 7/10, evidence 10/10, insight 8/10
- Independent editor scores: {"clarity_score": 8, "technical_coherence_score": 8, "takeaway_value_score": 8, "source_faithfulness_score": 8, "originality_score": 8, "reason": "Clear, technically coherent, source-backed, and adds a useful pre‑deploy test tip.", "passed": true}
- Live primary page: https://github.com/ocelhq/ocel (HTTP 200)
- Exact source evidence: “Ocel is a CLI for deploying apps to your AWS, GCP or VPS without writing infra code.”
- Why this angle: The GitHub description confirms Ocel’s core purpose of deploying apps anywhere, and the summary notes no separate IaC files are required. The takeaway advises a practical pre‑deploy compile check to surface infra issues early.
- Editorial takeaway: Run a pre‑deploy test that compiles infra code to catch missing dependencies.
- Source: https://github.com/ocelhq/ocel

**Claim-by-claim source quotes:**

- Ocel’s CLI deploys apps to AWS, GCP or VPS without separate IaC files. ← “Ocel is a CLI for deploying apps to your AWS, GCP or VPS without writing infra code.”

Proposed post (not published):

> Ocel’s CLI deploys apps to AWS, GCP or VPS without separate IaC files. Run a pre‑deploy test that compiles infra code to catch missing dependencies. https://github.com/ocelhq/ocel

- Length: 179/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- Show HN: SpecDeck – Bring coding agent decisions back into the spec: The factual opening bundles multiple features; narrow it to one capability.
  - Rejected text: SpecDeck keeps context, requirements, acceptance criteria together for AI agents. Run a spec review cycle to verify AI outputs match spec before merging. https://specdeck.ai/
  - Model evidence quote: “Keep project context, requirements, and acceptance criteria together.”
  - Claim support: SpecDeck keeps context, requirements, acceptance criteria together for AI agents. ← “Keep project context, requirements, and acceptance criteria together.”
- snapotter-hq/SnapOtter: The factual opening bundles multiple features; narrow it to one capability.; Editorial takeaway is too long; keep the analysis concrete and concise.; Supporting quotes cover only 62% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: SnapOtter is a self‑hosted tool that runs OCR, transcribe, and local AI on‑premise. Add a pipeline test that uploads a sample PDF and verifies OCR output matches expected text. https://github.com/snapotter-hq/SnapOtter
  - Model evidence quote: “Open‑source, self‑hosted file‑processing tool. Convert, compress, OCR, transcribe & run local AI across image, video, audio, PDF & documents, via UI, REST API & pipelines. Your files never leave your network.”
  - Claim support: SnapOtter is a self‑hosted tool that runs OCR, transcribe, and local AI on‑premise. ← “Open‑source, self‑hosted file‑processing tool. Convert, compress, OCR, transcribe & run local AI across image, video, audio, PDF & documents, via UI, REST API & pipelines. Your files never leave your network.”

## Top discovery candidates considered

- Show HN: Ocel – Deploy apps to your AWS,GCP or VPS with infra from code | Hacker News | product_and_workflow_tools | raw 71, adjusted 55 | https://github.com/ocelhq/ocel
- Show HN: SpecDeck – Bring coding agent decisions back into the spec | Hacker News | product_and_workflow_tools | raw 69, adjusted 53 | https://specdeck.ai/
- snapotter-hq/SnapOtter | GitHub Search | security_and_self_hosting | raw 67, adjusted 51 | current stars 2904 | GitHub star trend: building baseline | https://github.com/snapotter-hq/SnapOtter

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
