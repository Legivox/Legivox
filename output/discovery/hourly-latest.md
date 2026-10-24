# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-24T18:49:58+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 86
- Independent editorial review: 1 draft(s) passed / 1 rejected
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
| Hacker News · hn-shopify | 7 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Console.dev | 12 | ok |
| Product Hunt | 44 | ok |
| Shopify Developer Changelog | 11 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 86
- Previously tracked repositories refreshed outside search results: 114
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 8
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| betterlytics/betterlytics | yes | 200 | https://github.com/betterlytics/betterlytics |
| reloop-labs/reloop | yes | 200 | https://github.com/reloop-labs/reloop |
| Beta: durable-harness | yes | 200 | https://vercel.com/blog/making-every-harness-durable?ref=console.dev |

## Selected draft candidates

### Draft option 1: Beta: durable-harness

- Category: developer_tools
- Source: Console.dev
- Format: short
- Editorial score: 8.8/10
- Model scores: timeliness 8/10, usefulness 9/10, novelty 7/10, evidence 10/10, insight 9/10
- Independent editor scores: {"clarity_score": 9, "technical_coherence_score": 9, "takeaway_value_score": 8, "source_faithfulness_score": 9, "originality_score": 7, "reason": "Clear claim, supported by source, and practical test for session persistence.", "passed": true}
- Live primary page: https://vercel.com/blog/making-every-harness-durable?ref=console.dev (HTTP 200)
- Exact source evidence: “durable-harness makes Pi, OpenCode, Claude Code, and Codex durable on Vercel, Postgres, or your laptop, so agent sessions survive crashes and timeouts.”
- Why this angle: Isolated a single capability and suggested a concrete durability test.
- Editorial takeaway: Restart an agent after a simulated crash to verify session persistence.
- Source: https://vercel.com/blog/making-every-harness-durable?ref=console.dev

**Claim-by-claim source quotes:**

- durable-harness ensures agent sessions survive crashes on Vercel. ← “durable-harness makes Pi, OpenCode, Claude Code, and Codex durable on Vercel, Postgres, or your laptop, so agent sessions survive crashes and timeouts.”

Proposed post (not published):

> durable-harness ensures agent sessions survive crashes on Vercel. Restart an agent after a simulated crash to verify session persistence. https://vercel.com/blog/making-every-harness-durable?ref=console.dev

- Length: 206/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: yes
- Repaired drafts submitted: 3
- Repaired drafts that passed local validation: 2
- Repaired drafts rejected: 1
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- betterlytics/betterlytics: The factual opening bundles multiple features; narrow it to one capability.
  - Rejected text: betterlytics offers session replay, error tracking, Core Web Vitals and uptime monitoring in one tool. Verify session replay after GDPR compliance to ensure privacy‑friendly analytics. https://github.com/betterlytics/betterlytics
  - Model evidence quote: “Open‑source web analytics with session replay, error tracking, Core Web Vitals and uptime monitoring in one tool. Cookieless, EU‑hosted cloud or self‑hosted.”
  - Claim support: betterlytics offers session replay, error tracking, Core Web Vitals and uptime monitoring in one tool. ← “Open‑source web analytics with session replay, error tracking, Core Web Vitals and uptime monitoring in one tool. Cookieless, EU‑hosted cloud or self‑hosted.”
- reloop-labs/reloop: The factual opening bundles multiple features; narrow it to one capability.; Editorial takeaway is not specific enough to this candidate's technical/product details.
  - Rejected text: reloop provides an open‑source transactional email API with SMTP, inbound mail, webhooks and campaigns. Run deliverability tests against major spam filters before scaling production traffic. https://github.com/reloop-labs/reloop
  - Model evidence quote: “Open‑source transactional email API and self‑hostable Resend alternative. SMTP, inbound mail, webhooks, and campaigns for developers.”
  - Claim support: reloop provides an open‑source transactional email API with SMTP, inbound mail, webhooks and campaigns. ← “Open‑source transactional email API and self‑hostable Resend alternative. SMTP, inbound mail, webhooks, and campaigns for developers.”
- Beta: durable-harness: The factual opening bundles multiple features; narrow it to one capability.
  - Rejected text: durable-harness makes Pi, OpenCode, Claude Code and Codex durable on Vercel, Postgres or laptop. Test session persistence after a crash to confirm durability across environments. https://vercel.com/blog/making-every-harness-durable?ref=console.dev
  - Model evidence quote: “durable-harness makes Pi, OpenCode, Claude Code, and Codex durable on Vercel, Postgres, or your laptop, so agent sessions survive crashes and timeouts.”
  - Claim support: durable-harness makes Pi, OpenCode, Claude Code and Codex durable on Vercel, Postgres or laptop. ← “durable-harness makes Pi, OpenCode, Claude Code, and Codex durable on Vercel, Postgres, or your laptop, so agent sessions survive crashes and timeouts.”
- reloop-labs/reloop: No claim-by-claim supporting evidence was provided; Supporting quotes cover only 17% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: reloop offers an SMTP interface for transactional email. Test SMTP delivery against a test mailbox to confirm authentication. https://github.com/reloop-labs/reloop
  - Model evidence quote: “SMTP, inbound mail, webhooks, and campaigns for developers.”
- betterlytics/betterlytics: Takeaway assumes GDPR compliance affects session replay, but source does not link GDPR to replay functionality.
  - Rejected text: betterlytics provides session replay for web analytics. Verify session replay captures user interactions after GDPR compliance. https://github.com/betterlytics/betterlytics

## Top discovery candidates considered

- betterlytics/betterlytics | GitHub Search | data_and_growth | raw 71, adjusted 55 | current stars 180 | GitHub star trend: building baseline | https://github.com/betterlytics/betterlytics
- reloop-labs/reloop | GitHub Search | developer_tools | raw 70, adjusted 54 | current stars 167 | GitHub star trend: building baseline | https://github.com/reloop-labs/reloop
- Beta: durable-harness | Console.dev | developer_tools | raw 52, adjusted 52 | https://vercel.com/blog/making-every-harness-durable?ref=console.dev

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
