# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-25T11:41:22+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 88
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
| Product Hunt | 40 | ok |
| Shopify Developer Changelog | 10 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 79
- Previously tracked repositories refreshed outside search results: 121
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 12
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| Show HN: Independent Vet – Find locally owned vets (and corporate ones) near you | yes | 200 | https://independentvet.com/ |
| Show HN: Music player for visually exploring music collection | yes | 200 | https://github.com/Cliff-Lee/melodex |
| codelibs/fess | yes | 200 | https://github.com/codelibs/fess |

## Selected draft candidates

### Draft option 1: codelibs/fess

- Category: security_and_self_hosting
- Source: GitHub Search
- Format: tool_discovery
- Editorial score: 8.25/10
- Model scores: timeliness 9/10, usefulness 8/10, novelty 7/10, evidence 9/10, insight 8/10
- Independent editor scores: {"clarity_score": 8, "technical_coherence_score": 8, "takeaway_value_score": 8, "source_faithfulness_score": 8, "originality_score": 8, "reason": "Clear, accurate, and adds a practical benchmark suggestion.", "passed": true}
- Live primary page: https://github.com/codelibs/fess (HTTP 200)
- Exact source evidence: “Open‑source, self‑hosted enterprise & site search server built on OpenSearch. Crawls web / file / DB / cloud sources, 20+ languages, REST API, and AI/RAG & semantic search.”
- Why this angle: Highlights core capability and a practical performance check.
- Editorial takeaway: Run a benchmark on a subset of data to gauge latency before full deployment.
- Source: https://github.com/codelibs/fess

**Claim-by-claim source quotes:**

- Fess is a self‑hosted enterprise search server built on OpenSearch that supports AI‑powered semantic search. ← “Open‑source, self‑hosted enterprise & site search server built on OpenSearch. Crawls web / file / DB / cloud sources, 20+ languages, REST API, and AI/RAG & semantic search.”

Proposed post (not published):

> Fess is a self‑hosted enterprise search server built on OpenSearch that supports AI‑powered semantic search. Run a benchmark on a subset of data to gauge latency before full deployment. https://github.com/codelibs/fess

- Length: 218/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- Show HN: Independent Vet – Find locally owned vets (and corporate ones) near you: Supporting quotes cover only 60% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: Independent Vet lets users find locally owned veterinary practices and see ownership status. Verify ownership filters before booking to avoid PE‑owned surprises. https://independentvet.com/
  - Model evidence quote: “Find locally owned veterinary practices near you and see which clinics are verified independent or corporately owned.”
  - Claim support: Independent Vet lets users find locally owned veterinary practices and see ownership status. ← “Find locally owned veterinary practices near you and see which clinics are verified independent or corporately owned.”
- Show HN: Music player for visually exploring music collection: Editorial takeaway mostly repeats source wording; add an independent test, trade-off or interpretation.
  - Rejected text: Melodex is a local‑first music player that builds a visual Music Map and Album Wall. Test map navigation on a small library before scaling to full collection. https://github.com/Cliff-Lee/melodex
  - Model evidence quote: “Open‑source, local‑first music player with a visual Music Map, Album Wall and listening journeys.”
  - Claim support: Melodex is a local‑first music player that builds a visual Music Map and Album Wall. ← “Open‑source, local‑first music player with a visual Music Map, Album Wall and listening journeys.”

## Top discovery candidates considered

- Show HN: Independent Vet – Find locally owned vets (and corporate ones) near you | Hacker News | product_and_workflow_tools | raw 66, adjusted 68 | https://independentvet.com/
- Show HN: Music player for visually exploring music collection | Hacker News | product_and_workflow_tools | raw 65, adjusted 67 | https://github.com/Cliff-Lee/melodex
- codelibs/fess | GitHub Search | security_and_self_hosting | raw 72, adjusted 66 | current stars 1142 | GitHub star trend: building baseline | https://github.com/codelibs/fess

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
