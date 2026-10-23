# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-23T20:49:53+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 103
- Independent editorial review: 0 draft(s) passed / 1 rejected
- Drafts passing local checks: 0
- Outcome: **skip**
- Decision reason: No draft cleared the complete automatic quality gate; independent editorial review failed closed. Independent editorial review failed closed: Groq returned HTTP 429: Rate limit reached for model `openai/gpt-oss-20b` in organization `org_01m57z755zetrv5mytrbsx754p` service tier `on_demand` on tokens per minute (TPM): Limi

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
| Hacker News · hn-automation-api | 2 | ok |
| Hacker News · hn-creator-business | 0 | ok |
| Hacker News · hn-digital-products | 1 | ok |
| Hacker News · hn-ecommerce-payments | 0 | ok |
| Hacker News · hn-security-selfhost | 0 | ok |
| Hacker News · hn-shopify | 8 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Console.dev | 12 | ok |
| Product Hunt | 42 | ok |
| Shopify Developer Changelog | 12 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 83
- Previously tracked repositories refreshed outside search results: 116
- Refresh failures: 1
- Star snapshots recorded this run: 199
- Repositories with a 20–36 hour comparison baseline: 15
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| ollaya-dev/ollaya | yes | 200 | https://github.com/ollaya-dev/ollaya |
| vstorm-co/agenticos | yes | 200 | https://github.com/vstorm-co/agenticos |
| Show HN: ParaGraFX – An iOS app for reading and illustrating ePub books | yes | 200 | https://apps.apple.com/us/app/paragrafx-illustrate-books/id6795768929 |

## Selected draft candidates

No draft cleared the complete local and independent-editor gate. See the decision reason and rejected-draft section for locally valid drafts that were rejected, not reviewed, or blocked by a review error.

## Automatic repair attempt

- Attempted: yes
- Repaired drafts submitted: 2
- Repaired drafts that passed local validation: 1
- Repaired drafts rejected: 1
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- ollaya-dev/ollaya: Editorial takeaway is too long; keep the analysis concrete and concise.
  - Rejected text: ollaya provides a Jev-compatible API server that pulls and serves 24 model families. Run a /v1/systemone health check to confirm local model availability before production use. https://github.com/ollaya-dev/ollaya
  - Model evidence quote: “Jev-compatible API server for open decision models. Ollama for decision models: pull and serve 24 model families”
  - Claim support: ollaya provides a Jev-compatible API server that pulls and serves 24 model families ← “Jev-compatible API server for open decision models. Ollama for decision models: pull and serve 24 model families”
- vstorm-co/agenticos: Editorial takeaway is too long; keep the analysis concrete and concise.; Supporting quotes cover only 62% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: agenticos offers a self-hosted agent layer with an API for governing AI agents. Check that agent budgets are enforced by sending a high‑cost request and verifying the response is throttled. https://github.com/vstorm-co/agenticos
  - Model evidence quote: “Open-source AI teammates for your company. The self-hosted agent layer: build, run and govern AI agents on your own servers, models and rules. RAG, skills, a real browser, 4,700+ MCP servers and an API”
  - Claim support: agenticos offers a self-hosted agent layer with an API for governing AI agents ← “Open-source AI teammates for your company. The self-hosted agent layer: build, run and govern AI agents on your own servers, models and rules. RAG, skills, a real browser, 4,700+ MCP servers and an API”
- Show HN: ParaGraFX – An iOS app for reading and illustrating ePub books: Editorial takeaway is too long; keep the analysis concrete and concise.; A supporting quote does not share enough wording with its stated claim; Supporting quotes cover only 43% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: ParaGraFX is an iOS app that generates illustrations for ePub books. Verify queued chapter generation completes before app closure by monitoring background task status. https://apps.apple.com/us/app/paragrafx-illustrate-books/id6795768929
  - Model evidence quote: “ParaGraFX: Illustrate Books App - App Store”
  - Claim support: ParaGraFX is an iOS app that generates illustrations for ePub books ← “ParaGraFX: Illustrate Books App - App Store”
- vstorm-co/agenticos: Editorial takeaway is too long; keep the analysis concrete and concise.; No claim-by-claim supporting evidence was provided
  - Rejected text: agenticos is a self‑hosted AI agent platform with an API. Verify budget enforcement by sending a high‑cost request and checking the response is throttled. https://github.com/vstorm-co/agenticos
  - Model evidence quote: “Open‑source AI teammates for your company. The self‑hosted agent layer: build, run and govern AI agents on your own servers, models and rules. RAG, skills, a real browser, 4,700+ MCP servers and an API”
- ollaya-dev/ollaya: Independent editorial review failed closed: Groq returned HTTP 429: Rate limit reached for model `openai/gpt-oss-20b` in organization `org_01m57z755zetrv5mytrbsx754p` service tier `on_demand` on tokens per minute (TPM): Limi
  - Rejected text: ollaya is a Jev‑compatible API server for decision models. Run /v1/systemone health check to confirm local model availability before production use. https://github.com/ollaya-dev/ollaya

## Top discovery candidates considered

- ollaya-dev/ollaya | GitHub Search | ai_and_automation | raw 74, adjusted 68 | current stars 1384 | GitHub star trend: building baseline | https://github.com/ollaya-dev/ollaya
- vstorm-co/agenticos | GitHub Search | ai_and_automation | raw 74, adjusted 68 | current stars 116 | GitHub star trend: building baseline | https://github.com/vstorm-co/agenticos
- Show HN: ParaGraFX – An iOS app for reading and illustrating ePub books | Hacker News | product_and_workflow_tools | raw 66, adjusted 68 | https://apps.apple.com/us/app/paragrafx-illustrate-books/id6795768929

## Safety and interpretation

- This run did not produce a publishable draft; no post was published to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
