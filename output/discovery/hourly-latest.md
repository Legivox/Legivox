# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-24T19:38:16+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 75
- Independent editorial review: 0 draft(s) passed / 0 rejected
- Drafts passing local checks: 0
- Outcome: **skip**
- Decision reason: All generated drafts failed the local evidence/editorial checks; the hour was skipped.

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
| Shopify Developer Changelog | 11 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 77
- Previously tracked repositories refreshed outside search results: 123
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 8
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| mixpeek/amux | yes | 200 | https://github.com/mixpeek/amux |
| Basedash Scheduled CSV Exports | no | — | Primary source returned HTTP 403. |
| PostHog/posthog | yes | 200 | https://github.com/PostHog/posthog |

## Selected draft candidates

No candidate produced a draft that passed every local check. Skipping is intentional.

## Automatic repair attempt

- Attempted: yes
- Repaired drafts submitted: 2
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 2
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- Basedash Scheduled CSV Exports: Primary source returned HTTP 403.
- mixpeek/amux: The factual opening bundles multiple features; narrow it to one capability.; Fact sentence is too long; narrow it to one source-backed capability.
  - Rejected text: amux is an open‑source Rust control plane that orchestrates Claude, Codex, and Gemini workers on a shared board. Validate that atomic tasks finish before the next loop to avoid stale state. https://github.com/mixpeek/amux
  - Model evidence quote: “Open‑source control plane for AI coding agents. Run an AI engineering team: parallel Claude Code, Codex, and Gemini workers with a shared board”
  - Claim support: amux orchestrates Claude, Codex, and Gemini workers on a shared board ← “Open‑source control plane for AI coding agents. Run an AI engineering team: parallel Claude Code, Codex, and Gemini workers with a shared board”
- PostHog/posthog: The factual opening bundles multiple features; narrow it to one capability.
  - Rejected text: PostHog aggregates AI observability, analytics, and session replay into a single platform. Run a replay test on a critical user flow to confirm flag changes propagate correctly. https://github.com/PostHog/posthog
  - Model evidence quote: “PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more”
  - Claim support: PostHog aggregates AI observability, analytics, and session replay into a single platform ← “PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more”
- mixpeek/amux: The factual opening bundles multiple features; narrow it to one capability.; No claim-by-claim supporting evidence was provided; Supporting quotes cover only 64% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: amux is an open‑source control plane that runs parallel Claude, Codex, and Gemini workers on a shared board. Validate that atomic tasks finish before the next loop to avoid stale state. https://github.com/mixpeek/amux
  - Model evidence quote: “parallel Claude Code, Codex, and Gemini workers with a shared board”
- PostHog/posthog: No claim-by-claim supporting evidence was provided; Supporting quotes cover only 33% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: PostHog provides AI observability and analytics for self‑driving products. Run a replay test on a critical user flow to confirm flag changes propagate correctly. https://github.com/PostHog/posthog
  - Model evidence quote: “AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more”

## Top discovery candidates considered

- mixpeek/amux | GitHub Search | security_and_self_hosting | raw 68, adjusted 52 | current stars 544 | GitHub star trend: building baseline | https://github.com/mixpeek/amux
- Basedash Scheduled CSV Exports | Product Hunt | product_and_workflow_tools | raw 51, adjusted 51 | https://www.producthunt.com/products/basedash
- PostHog/posthog | GitHub Search | data_and_growth | raw 66, adjusted 50 | current stars 40405 | GitHub star trend: building baseline | https://github.com/PostHog/posthog

## Safety and interpretation

- This run did not produce a publishable draft; no post was published to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
