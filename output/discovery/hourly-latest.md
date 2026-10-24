# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-24T11:40:49+05:30
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
| Hacker News · hn-automation-api | 2 | ok |
| Hacker News · hn-creator-business | 0 | ok |
| Hacker News · hn-digital-products | 1 | ok |
| Hacker News · hn-ecommerce-payments | 0 | ok |
| Hacker News · hn-security-selfhost | 0 | ok |
| Hacker News · hn-shopify | 8 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Console.dev | 12 | ok |
| Product Hunt | 40 | ok |
| Shopify Developer Changelog | 11 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 77
- Previously tracked repositories refreshed outside search results: 123
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 9
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| Tell HN: Don't use Fathom Analytics (founder is blocking criticism) | no | — | Primary source returned HTTP 429. |
| lemma-work/lemma-platform | yes | 200 | https://github.com/lemma-work/lemma-platform |
| pipeshub-ai/pipeshub-ai | yes | 200 | https://github.com/pipeshub-ai/pipeshub-ai |

## Selected draft candidates

### Draft option 1: pipeshub-ai/pipeshub-ai

- Category: ai_and_automation
- Source: GitHub Search
- Format: tweet
- Editorial score: 8.8/10
- Model scores: timeliness 8/10, usefulness 9/10, novelty 7/10, evidence 10/10, insight 9/10
- Independent editor scores: {"clarity_score": 8, "technical_coherence_score": 8, "takeaway_value_score": 8, "source_faithfulness_score": 8, "originality_score": 8, "reason": "Clear, accurate, and adds a concrete test idea.", "passed": true}
- Live primary page: https://github.com/pipeshub-ai/pipeshub-ai (HTTP 200)
- Exact source evidence: “PipesHub turns your company&#39;s knowledge (Slack, Drive, Jira, GitHub, Microsoft 365 and 40+ connectors) into a permission-aware workspace that agents...”
- Why this angle: Focused on a single documented feature and added a concrete permission‑testing step.
- Editorial takeaway: Test permission handling by querying a protected Jira issue and checking access logs.
- Source: https://github.com/pipeshub-ai/pipeshub-ai

**Claim-by-claim source quotes:**

- pipeshub‑ai turns Jira knowledge into a permission‑aware workspace for agents. ← “PipesHub turns your company&#39;s knowledge (Slack, Drive, Jira, GitHub, Microsoft 365 and 40+ connectors) into a permission-aware workspace that agents...”

Proposed post (not published):

> pipeshub‑ai turns Jira knowledge into a permission‑aware workspace for agents. Test permission handling by querying a protected Jira issue and checking access logs. https://github.com/pipeshub-ai/pipeshub-ai

- Length: 207/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: yes
- Repaired drafts submitted: 2
- Repaired drafts that passed local validation: 1
- Repaired drafts rejected: 1
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- Tell HN: Don't use Fathom Analytics (founder is blocking criticism): Primary source returned HTTP 429.
- lemma-work/lemma-platform: The factual opening bundles multiple features; narrow it to one capability.; Fact sentence is too long; narrow it to one source-backed capability.
  - Rejected text: lemma-platform is a multiplayer harness for sharing agents, apps and workflows across Slack, Telegram, WhatsApp, Teams, Email. Verify a workflow runs identically when triggered from Slack and Teams. https://github.com/lemma-work/lemma-platform
  - Model evidence quote: “Multiplayer harness that shapes around your work. Agents, apps and workflows your team shares, used from Slack, Telegram, WhatsApp, Teams, Email, Web or your own AI agent.”
  - Claim support: lemma-platform is a multiplayer harness for sharing agents, apps and workflows across Slack, Telegram, WhatsApp, Teams, Email. ← “Multiplayer harness that shapes around your work. Agents, apps and workflows your team shares, used from Slack, Telegram, WhatsApp, Teams, Email, Web or your own AI agent.”
- Unmapped model draft: Model omitted a valid candidate ID and no exact verified source URL matched.
- pipeshub-ai/pipeshub-ai: The factual opening bundles multiple features; narrow it to one capability.; Fact sentence is too long; narrow it to one source-backed capability.; Editorial takeaway is too long; keep the analysis concrete and concise.; Fact plus takeaway exceeds the per-link character budget.; Draft is 357 raw characters; limit is 280
  - Rejected text: pipeshub-ai is an open‑source context layer that turns company knowledge from Slack, Drive, Jira, GitHub, Microsoft 365 and 40+ connectors into a permission‑aware workspace for agents to search, grep, navigate and cite. Run a permission test by querying a protected Jira issue and ensuring the agent respects ACLs. https://github.com/pipeshub-ai/pipeshub-ai
  - Model evidence quote: “PipesHub turns your company's knowledge (Slack, Drive, Jira, GitHub, Microsoft 365 and 40+ connectors) into a permission‑aware workspace that agents can search, grep, navigate and cite.”
  - Claim support: pipeshub-ai is an open‑source context layer that turns company knowledge from Slack, Drive, Jira, GitHub, Microsoft 365 and 40+ connectors into a permission‑aware workspace for agents to search, grep, navigate and cite. ← “PipesHub turns your company's knowledge (Slack, Drive, Jira, GitHub, Microsoft 365 and 40+ connectors) into a permission‑aware workspace that agents can search, grep, navigate and cite.”
- lemma-work/lemma-platform: Editorial takeaway is not specific enough to this candidate's technical/product details.; No claim-by-claim supporting evidence was provided; Factual sentence includes terms absent from the source title/summary: run, same
  - Rejected text: lemma‑platform lets you run the same workflow from Slack and Teams. Verify identical execution by triggering the workflow in both channels and comparing logs. https://github.com/lemma-work/lemma-platform
  - Model evidence quote: “Agents, apps and workflows your team shares, used from Slack, Telegram, WhatsApp, Teams, Email, Web or your own AI agent.”

## Top discovery candidates considered

- Tell HN: Don't use Fathom Analytics (founder is blocking criticism) | Hacker News | data_and_growth | raw 69, adjusted 69 | https://news.ycombinator.com/item?id=50210534
- lemma-work/lemma-platform | GitHub Search | ai_and_automation | raw 71, adjusted 65 | current stars 633 | GitHub star trend: building baseline | https://github.com/lemma-work/lemma-platform
- pipeshub-ai/pipeshub-ai | GitHub Search | ai_and_automation | raw 71, adjusted 65 | current stars 3845 | GitHub star trend: building baseline | https://github.com/pipeshub-ai/pipeshub-ai

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
