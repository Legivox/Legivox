# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-26T16:53:30+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 94
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
| Hacker News · hn-analytics-growth | 4 | ok |
| Hacker News · hn-automation-api | 1 | ok |
| Hacker News · hn-creator-business | 0 | ok |
| Hacker News · hn-digital-products | 1 | ok |
| Hacker News · hn-ecommerce-payments | 0 | ok |
| Hacker News · hn-security-selfhost | 0 | ok |
| Hacker News · hn-shopify | 6 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Console.dev | 12 | ok |
| Product Hunt | 40 | ok |
| Shopify Developer Changelog | 10 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 80
- Previously tracked repositories refreshed outside search results: 120
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 6
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| Show HN: Ultimidi – learn piano through games | yes | 200 | https://game.ultimidi.com/ |
| Show HN: Nord Theme for Cursor | yes | 200 | https://github.com/willio/nord-theme-for-cursor |
| Sponsor: Falconer | yes | 200 | https://falconer.com/about/knowledge-health?utm_source=console.dev&utm_medium=newsletter&utm_content=knowledge-health |

## Selected draft candidates

### Draft option 1: Show HN: Nord Theme for Cursor

- Category: product_and_workflow_tools
- Source: Hacker News
- Format: tool_discovery
- Editorial score: 8.1/10
- Model scores: timeliness 8/10, usefulness 8/10, novelty 7/10, evidence 9/10, insight 8/10
- Independent editor scores: {"clarity_score": 8, "technical_coherence_score": 8, "takeaway_value_score": 8, "source_faithfulness_score": 8, "originality_score": 8, "reason": "Clear, technically coherent, source‑faithful, and adds a useful verification step.", "passed": true}
- Live primary page: https://github.com/willio/nord-theme-for-cursor (HTTP 200)
- Exact source evidence: “Nord (Polar Night) glass theme for Cursor — custom theme written to Cursor's theme store, with tested apply/restore/verify scripts”
- Why this angle: The source confirms the theme’s tested scripts; persistence testing is a practical validation step.
- Editorial takeaway: Verify theme persistence after Cursor restarts to catch state bugs.
- Source: https://github.com/willio/nord-theme-for-cursor

**Claim-by-claim source quotes:**

- Nord theme for Cursor offers a low‑contrast glass palette with tested apply/restore scripts. ← “Nord (Polar Night) glass theme for Cursor — custom theme written to Cursor's theme store, with tested apply/restore/verify scripts”

Proposed post (not published):

> Nord theme for Cursor offers a low‑contrast glass palette with tested apply/restore scripts. Verify theme persistence after Cursor restarts to catch state bugs. https://github.com/willio/nord-theme-for-cursor

- Length: 208/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- Show HN: Ultimidi – learn piano through games: Supporting quotes cover only 62% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: Ultimidi: Piano Journey lets users learn piano via short lessons and songs. Test lesson progression to ensure difficulty scales linearly. https://game.ultimidi.com/
  - Model evidence quote: “Learn piano through short lessons, familiar songs, and a colorful musical adventure.”
  - Claim support: Ultimidi: Piano Journey lets users learn piano via short lessons and songs. ← “Learn piano through short lessons, familiar songs, and a colorful musical adventure.”
- Sponsor: Falconer: The factual opening bundles multiple features; narrow it to one capability.; Fact plus takeaway exceeds the per-link character budget.; Draft is 285 raw characters; limit is 280
  - Rejected text: Falconer grades docs on coherence, coverage, freshness, density, and completeness. Run a quarterly audit to catch emerging contradictions before agents use stale data. https://falconer.com/about/knowledge-health?utm_source=console.dev&utm_medium=newsletter&utm_content=knowledge-health
  - Model evidence quote: “Falconer grades your docs on coherence, coverage, freshness, density, and completeness, surfacing outdated content, gaps, and contradictions before agents act.”
  - Claim support: Falconer grades docs on coherence, coverage, freshness, density, and completeness. ← “Falconer grades your docs on coherence, coverage, freshness, density, and completeness, surfacing outdated content, gaps, and contradictions before agents act.”

## Top discovery candidates considered

- Show HN: Ultimidi – learn piano through games | Hacker News | product_and_workflow_tools | raw 63, adjusted 65 | https://game.ultimidi.com/
- Show HN: Nord Theme for Cursor | Hacker News | product_and_workflow_tools | raw 56, adjusted 58 | https://github.com/willio/nord-theme-for-cursor
- Sponsor: Falconer | Console.dev | developer_tools | raw 49, adjusted 49 | https://falconer.com/about/knowledge-health?utm_source=console.dev&utm_medium=newsletter&utm_content=knowledge-health

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
