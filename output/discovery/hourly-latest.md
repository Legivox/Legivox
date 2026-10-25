# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-25T13:39:28+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 85
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
| Product Hunt | 43 | ok |
| Shopify Developer Changelog | 10 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 76
- Previously tracked repositories refreshed outside search results: 124
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 11
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| Show HN: Tributary – Discover who influenced your favorite musicians | yes | 200 | https://tributary.music/ |
| Show HN: Dadgpt Open Source Halloween Costume | yes | 200 | https://dadgptcostume.vercel.app/ |
| Metaobject analytics queryable capability available in the Admin API | yes | 200 | https://shopify.dev/changelog/posts/metaobject-analytics-queryable-capability-available-in-the-admin-api |

## Selected draft candidates

### Draft option 1: Metaobject analytics queryable capability available in the Admin API

- Category: data_and_growth
- Source: Shopify Developer Changelog
- Format: engineering_lesson
- Editorial score: 8.1/10
- Model scores: timeliness 8/10, usefulness 8/10, novelty 7/10, evidence 9/10, insight 8/10
- Independent editor scores: {"clarity_score": 8, "technical_coherence_score": 8, "takeaway_value_score": 8, "source_faithfulness_score": 8, "originality_score": 8, "reason": "Clear, technically accurate, and adds a useful guard recommendation not directly stated in the source.", "passed": true}
- Live primary page: https://shopify.dev/changelog/posts/metaobject-analytics-queryable-capability-available-in-the-admin-api (HTTP 200)
- Exact source evidence: “graphql) Starting with GraphQL Admin API version `2027-01`, you can read and configure the `analyticsQueryable` capability on metaobject definitions.”
- Why this angle: The changelog explicitly lists the new input field for setting analyticsQueryable. The takeaway advises checking the error code CAPABILITY_NOT_ELIGIBLE, a documented guard that developers should handle.
- Editorial takeaway: Add a guard to check CAPABILITY_NOT_ELIGIBLE when enabling analytics.
- Source: https://shopify.dev/changelog/posts/metaobject-analytics-queryable-capability-available-in-the-admin-api

**Claim-by-claim source quotes:**

- Metaobject analyticsQueryable can now be set via GraphQL Admin API. ← “graphql) Starting with GraphQL Admin API version `2027-01`, you can read and configure the `analyticsQueryable` capability on metaobject definitions.”

Proposed post (not published):

> Metaobject analyticsQueryable can now be set via GraphQL Admin API. Add a guard to check CAPABILITY_NOT_ELIGIBLE when enabling analytics. https://shopify.dev/changelog/posts/metaobject-analytics-queryable-capability-available-in-the-admin-api

- Length: 242/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- Show HN: Tributary – Discover who influenced your favorite musicians: A supporting quote does not share enough wording with its stated claim; Factual sentence includes terms absent from the source title/summary: influence, pair, similarity, track
  - Rejected text: Tributary pairs an artist’s track with an influence’s track to show similarities. Test the pairings by listening side‑by‑side to spot genre shifts. https://tributary.music/
  - Model evidence quote: “Hear the songs and read the stories behind the connections.”
  - Claim support: Tributary pairs an artist’s track with an influence’s track to show similarities. ← “Hear the songs and read the stories behind the connections.”
- Show HN: Dadgpt Open Source Halloween Costume: A supporting quote does not share enough wording with its stated claim; Supporting quotes cover only 38% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: DadGPT Costume lets a phone in a hat answer dad jokes aloud. Verify microphone permissions before deploying to avoid silent failures. https://dadgptcostume.vercel.app/
  - Model evidence quote: “Tap the mic, ask Dad anything, and he answers out loud with a dad joke.”
  - Claim support: DadGPT Costume lets a phone in a hat answer dad jokes aloud. ← “Tap the mic, ask Dad anything, and he answers out loud with a dad joke.”

## Top discovery candidates considered

- Show HN: Tributary – Discover who influenced your favorite musicians | Hacker News | product_and_workflow_tools | raw 63, adjusted 65 | https://tributary.music/
- Show HN: Dadgpt Open Source Halloween Costume | Hacker News | product_and_workflow_tools | raw 58, adjusted 60 | https://dadgptcostume.vercel.app/
- Metaobject analytics queryable capability available in the Admin API | Shopify Developer Changelog | data_and_growth | raw 66, adjusted 56 | https://shopify.dev/changelog/posts/metaobject-analytics-queryable-capability-available-in-the-admin-api

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
