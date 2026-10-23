# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-23T16:24:24+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 96
- Independent editorial review: 0 draft(s) passed / 2 rejected
- Drafts passing local checks: 0
- Outcome: **skip**
- Decision reason: Every draft submitted for independent editorial review was rejected; The hour was skipped.

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
| Hacker News · hn-shopify | 8 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Console.dev | 12 | ok |
| Product Hunt | 41 | ok |
| Shopify Developer Changelog | 11 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 78
- Previously tracked repositories refreshed outside search results: 122
- Refresh failures: 0
- Star snapshots recorded this run: 21
- Repositories with a 20–36 hour comparison baseline: 16
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| n8n-io/n8n | yes | 200 | https://github.com/n8n-io/n8n |
| shogo-labs/shogo-ai | yes | 200 | https://github.com/shogo-labs/shogo-ai |
| Show HN: Airlock, which sandboxes AI agents, is available on the Mac App Store | yes | 200 | https://airlock.sorrel.systems |

## Selected draft candidates

No draft cleared the complete local and independent-editor gate. See the decision reason and rejected-draft section for locally valid drafts that were rejected, not reviewed, or blocked by a review error.

## Automatic repair attempt

- Attempted: yes
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- Show HN: Airlock, which sandboxes AI agents, is available on the Mac App Store: Supporting quotes cover only 57% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: Airlock runs Claude or Codex in a VM on macOS and logs all changes. After running, inspect the diff to ensure only intended files were modified. https://airlock.sorrel.systems
  - Model evidence quote: “Airlock runs Claude Code or Codex in a virtual machine on your Mac.”
  - Claim support: Airlock runs Claude or Codex in a VM on macOS and logs all changes. ← “Airlock runs Claude Code or Codex in a virtual machine on your Mac.”
- n8n-io/n8n: Takeaway assumes schedule trigger behavior not explicitly documented; no concrete test guidance.
  - Rejected text: n8n is a fair‑code workflow automation platform with native AI capabilities. Run a simple AI node and verify it triggers on schedule. https://github.com/n8n-io/n8n
- shogo-labs/shogo-ai: Takeaway presumes SDK can connect to an LLM endpoint, not mentioned in source; lacks concrete verification steps.
  - Rejected text: shogo-ai is an open‑source platform for building and running AI agents. Check that the SDK can instantiate an agent and connect to an LLM endpoint. https://github.com/shogo-labs/shogo-ai

## Top discovery candidates considered

- n8n-io/n8n | GitHub Search | ai_and_automation | raw 71, adjusted 75 | current stars 208374 | GitHub star trend: building baseline | https://github.com/n8n-io/n8n
- shogo-labs/shogo-ai | GitHub Search | ai_and_automation | raw 70, adjusted 74 | current stars 17 | GitHub star trend: building baseline | https://github.com/shogo-labs/shogo-ai
- Show HN: Airlock, which sandboxes AI agents, is available on the Mac App Store | Hacker News | data_and_growth | raw 64, adjusted 66 | https://airlock.sorrel.systems

## Safety and interpretation

- This run did not produce a publishable draft; no post was published to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
