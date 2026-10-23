# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-23T17:40:58+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 100
- Independent editorial review: 1 draft(s) passed / 2 rejected
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
| Product Hunt | 41 | ok |
| Shopify Developer Changelog | 11 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 79
- Previously tracked repositories refreshed outside search results: 121
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 26
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| milind-soni/OpenMausBot | yes | 200 | https://github.com/milind-soni/OpenMausBot |
| corezoid/corezoid-ai-plugin | yes | 200 | https://github.com/corezoid/corezoid-ai-plugin |
| Show HN: MegaKey (standardization and extension of the Hyper and Meh keys) | yes | 200 | https://leftium.github.io/megakey/ |

## Selected draft candidates

### Draft option 1: milind-soni/OpenMausBot

- Category: security_and_self_hosting
- Source: GitHub Search
- Format: short
- Editorial score: 8.6/10
- Model scores: timeliness 8/10, usefulness 9/10, novelty 7/10, evidence 10/10, insight 8/10
- Independent editor scores: {"clarity_score": 8, "technical_coherence_score": 8, "takeaway_value_score": 8, "source_faithfulness_score": 8, "originality_score": 8, "reason": "Clear, accurate, and adds a useful deployment tip.", "passed": true}
- Live primary page: https://github.com/milind-soni/OpenMausBot (HTTP 200)
- Exact source evidence: “Open-source Grok Bot alternative with a virtual machine that bots can use - milind-soni/OpenMausBot”
- Why this angle: The primary source explicitly states the product runs bots inside a virtual machine, and the repository topics include docker, indicating Docker deployment is supported.
- Editorial takeaway: Deploy OpenMausBot with Docker to isolate bot execution.
- Source: https://github.com/milind-soni/OpenMausBot

**Claim-by-claim source quotes:**

- OpenMausBot is an open‑source Grok Bot alternative that runs bots inside a virtual machine. ← “Open-source Grok Bot alternative with a virtual machine that bots can use - milind-soni/OpenMausBot”

Proposed post (not published):

> OpenMausBot is an open‑source Grok Bot alternative that runs bots inside a virtual machine. Deploy OpenMausBot with Docker to isolate bot execution. https://github.com/milind-soni/OpenMausBot

- Length: 191/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: yes
- Repaired drafts submitted: 1
- Repaired drafts that passed local validation: 1
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- Show HN: MegaKey (standardization and extension of the Hyper and Meh keys): Takeaway implies an interaction/causal relationship between source-listed features that the primary page does not establish. Reframe it as an explicit conditional test of the reader's own integration.; Editorial takeaway needs a concrete test, trade-off, risk, comparison, or next step.; A supporting quote does not share enough wording with its stated claim; Supporting quotes cover only 25% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: MegaKey defines five pseudo‑modifier keys that map complex shortcuts to single‑key symbols. Create a Karabiner rule and confirm the new key triggers the intended shortcut. https://leftium.github.io/megakey/
  - Model evidence quote: “A system of 5 pseudo-modifier keys that works on standard keyboards”
  - Claim support: MegaKey defines five pseudo‑modifier keys that map complex shortcuts to single‑key symbols. ← “A system of 5 pseudo-modifier keys that works on standard keyboards”
- milind-soni/OpenMausBot: Technical coherence and source faithfulness below threshold due to unsupported sandbox claim.
  - Rejected text: OpenMausBot is an open‑source Grok Bot alternative that runs bots inside a virtual machine. Run a sandboxed script in the VM and verify it cannot escape the container. https://github.com/milind-soni/OpenMausBot
- corezoid/corezoid-ai-plugin: Takeaway suggests type checks not documented; source faithfulness insufficient.
  - Rejected text: corezoid-ai-plugin hosts a marketplace of AI plugins for Claude Code and Codex. Import a sample playbook and run type checks to confirm plugin schemas are valid. https://github.com/corezoid/corezoid-ai-plugin

## Top discovery candidates considered

- milind-soni/OpenMausBot | GitHub Search | security_and_self_hosting | raw 63, adjusted 82 | current stars 5475 | GitHub stars +55 over about 20.1h | https://github.com/milind-soni/OpenMausBot
- corezoid/corezoid-ai-plugin | GitHub Search | ai_and_automation | raw 72, adjusted 76 | current stars 74 | GitHub star trend: building baseline | https://github.com/corezoid/corezoid-ai-plugin
- Show HN: MegaKey (standardization and extension of the Hyper and Meh keys) | Hacker News | product_and_workflow_tools | raw 66, adjusted 68 | https://leftium.github.io/megakey/

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
