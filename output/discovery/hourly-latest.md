# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-25T09:46:42+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 91
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
| Hacker News · hn-shopify | 8 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Console.dev | 12 | ok |
| Product Hunt | 42 | ok |
| Shopify Developer Changelog | 10 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 79
- Previously tracked repositories refreshed outside search results: 121
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 16
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| paperclipai/paperclip | yes | 200 | https://github.com/paperclipai/paperclip |
| agentrq/agentrq | yes | 200 | https://github.com/agentrq/agentrq |
| Show HN: Perch, a calm Mac app for juggling Claude Code sessions | yes | 200 | https://perchfocus.com/ |

## Selected draft candidates

### Draft option 1: agentrq/agentrq

- Category: ai_and_automation
- Source: GitHub Search
- Format: tool_discovery
- Editorial score: 8.4/10
- Model scores: timeliness 10/10, usefulness 8/10, novelty 7/10, evidence 9/10, insight 8/10
- Independent editor scores: {"clarity_score": 8, "technical_coherence_score": 8, "takeaway_value_score": 8, "source_faithfulness_score": 8, "originality_score": 8, "reason": "Clear, technically coherent, source‑faithful, and adds a useful deployment test.", "passed": true}
- Live primary page: https://github.com/agentrq/agentrq (HTTP 200)
- Exact source evidence: “AgentRQ: Human‑in‑loop realtime conversational task manager for AI Agents. Self‑hosted!”
- Why this angle: The repository title directly describes the product and its self‑hosted nature. The takeaway addresses a practical validation step for ACP integration.
- Editorial takeaway: Test a Claude harness to confirm ACP support before deployment.
- Source: https://github.com/agentrq/agentrq

**Claim-by-claim source quotes:**

- AgentRQ is a self‑hosted, real‑time conversational task manager for AI agents ← “AgentRQ: Human‑in‑loop realtime conversational task manager for AI Agents. Self‑hosted!”

Proposed post (not published):

> AgentRQ is a self‑hosted, real‑time conversational task manager for AI agents. Test a Claude harness to confirm ACP support before deployment. https://github.com/agentrq/agentrq

- Length: 177/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- paperclipai/paperclip: Takeaway implies an undocumented product capability: sync. Reframe as a check of documented behavior.; Takeaway implies an interaction/causal relationship between source-listed features that the primary page does not establish. Reframe it as an explicit conditional test of the reader's own integration.; Supporting quotes cover only 50% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: paperclip is an open‑source app for managing agents at work. Run a sample workflow to verify agent‑skill sync before scaling. https://github.com/paperclipai/paperclip
  - Model evidence quote: “The open‑source app everyone uses to manage agents at work”
  - Claim support: paperclip is an open‑source app for managing agents at work ← “The open‑source app everyone uses to manage agents at work”
- Show HN: Perch, a calm Mac app for juggling Claude Code sessions: The factual opening bundles multiple features; narrow it to one capability.; Editorial takeaway needs a concrete test, trade-off, risk, comparison, or next step.; Supporting quotes cover only 60% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: Perch is a calm Mac app that centralises Claude Code sessions, PRs, and links. Enable mute mode to focus while only seeing pending CI or reviewer actions. https://perchfocus.com/
  - Model evidence quote: “A calm Mac home for your Claude Code work, with every session, PR, and link in one place.”
  - Claim support: Perch is a calm Mac app that centralises Claude Code sessions, PRs, and links ← “A calm Mac home for your Claude Code work, with every session, PR, and link in one place.”

## Top discovery candidates considered

- paperclipai/paperclip | GitHub Search | ai_and_automation | raw 69, adjusted 88 | current stars 107022 | GitHub stars +328 over about 20.1h | https://github.com/paperclipai/paperclip
- agentrq/agentrq | GitHub Search | ai_and_automation | raw 73, adjusted 77 | current stars 1167 | GitHub star trend: building baseline | https://github.com/agentrq/agentrq
- Show HN: Perch, a calm Mac app for juggling Claude Code sessions | Hacker News | data_and_growth | raw 72, adjusted 74 | https://perchfocus.com/

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
