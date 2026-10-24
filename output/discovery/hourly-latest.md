# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-24T21:39:43+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 79
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
| Product Hunt | 42 | ok |
| Shopify Developer Changelog | 10 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 76
- Previously tracked repositories refreshed outside search results: 124
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 7
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| Show HN: A set of test-cases for CP/M emulators | yes | 200 | https://github.com/skx/cpm-test |
| metadist/synaplan | yes | 200 | https://github.com/metadist/synaplan |
| productdevbook/yuva | yes | 200 | https://github.com/productdevbook/yuva |

## Selected draft candidates

### Draft option 1: metadist/synaplan

- Category: security_and_self_hosting
- Source: GitHub Search
- Format: practical_workflow
- Editorial score: 8.25/10
- Model scores: timeliness 9/10, usefulness 8/10, novelty 7/10, evidence 9/10, insight 8/10
- Independent editor scores: {"clarity_score": 8, "technical_coherence_score": 8, "takeaway_value_score": 8, "source_faithfulness_score": 8, "originality_score": 8, "reason": "Clear, accurate, and adds a useful deployment tip.", "passed": true}
- Live primary page: https://github.com/metadist/synaplan (HTTP 200)
- Exact source evidence: “Open-source, self-hosted AI platform (PHP/Symfony): chat with any model, RAG over your docs”
- Why this angle: Illustrates deployment and integration steps
- Editorial takeaway: Deploy synaplan in Docker and expose the widget to embed in your help center.
- Source: https://github.com/metadist/synaplan

**Claim-by-claim source quotes:**

- synaplan is a self‑hosted AI platform that lets you chat with any model and run RAG over your docs ← “Open-source, self-hosted AI platform (PHP/Symfony): chat with any model, RAG over your docs”

Proposed post (not published):

> synaplan is a self‑hosted AI platform that lets you chat with any model and run RAG over your docs. Deploy synaplan in Docker and expose the widget to embed in your help center. https://github.com/metadist/synaplan

- Length: 214/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- Show HN: A set of test-cases for CP/M emulators: Supporting quotes cover only 57% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: cpm-test provides test cases that run against CP/M emulators. Run these tests on your emulator to catch missing BDOS calls before shipping. https://github.com/skx/cpm-test
  - Model evidence quote: “Testing code for running against CP/M emulators”
  - Claim support: cpm-test provides test cases that run against CP/M emulators ← “Testing code for running against CP/M emulators”
- productdevbook/yuva: The factual opening bundles multiple features; narrow it to one capability.; Supporting quotes cover only 56% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: yuva unifies email, live chat, and in‑app messaging into a single inbox for teams. Add a status page widget to yuva to surface uptime to customers. https://github.com/productdevbook/yuva
  - Model evidence quote: “Open-source customer messaging for teams with many products: e‑mail, live chat and in‑app conversations in one inbox”
  - Claim support: yuva unifies email, live chat, and in‑app messaging into a single inbox for teams ← “Open-source customer messaging for teams with many products: e‑mail, live chat and in‑app conversations in one inbox”

## Top discovery candidates considered

- Show HN: A set of test-cases for CP/M emulators | Hacker News | product_and_workflow_tools | raw 62, adjusted 64 | https://github.com/skx/cpm-test
- metadist/synaplan | GitHub Search | security_and_self_hosting | raw 68, adjusted 52 | current stars 221 | GitHub star trend: building baseline | https://github.com/metadist/synaplan
- productdevbook/yuva | GitHub Search | data_and_growth | raw 68, adjusted 52 | current stars 25 | GitHub star trend: building baseline | https://github.com/productdevbook/yuva

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
