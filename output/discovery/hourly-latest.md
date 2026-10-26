# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-26T14:55:00+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 95
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
- Repositories seen in this discovery run: 81
- Previously tracked repositories refreshed outside search results: 119
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 7
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| spatiumnorth/spatiumddi | yes | 200 | https://github.com/spatiumnorth/spatiumddi |
| open-edge-platform/dlstreamer | yes | 200 | https://github.com/open-edge-platform/dlstreamer |
| Show HN: ShellSprint – A typing game-ish for Linux and Kubernetes commands | yes | 200 | https://shellsprint-dev.pages.dev |

## Selected draft candidates

### Draft option 1: open-edge-platform/dlstreamer

- Category: data_and_growth
- Source: GitHub Search
- Format: tool_discovery
- Editorial score: 8.35/10
- Model scores: timeliness 8/10, usefulness 9/10, novelty 7/10, evidence 9/10, insight 8/10
- Independent editor scores: {"clarity_score": 8, "technical_coherence_score": 7, "takeaway_value_score": 7, "source_faithfulness_score": 8, "originality_score": 7, "reason": "Clear description, source backs claim, added practical latency check is a useful, original tip.", "passed": true}
- Live primary page: https://github.com/open-edge-platform/dlstreamer (HTTP 200)
- Exact source evidence: “GitHub - open-edge-platform/dlstreamer: Deep Learning Streamer (DL Streamer) Pipeline Framework is an open-source streaming media analytics framework, based on GStreamer* multimedia framework, for creating complex media analytics pipelines”
- Why this angle: Highlights GStreamer integration
- Editorial takeaway: Validate pipeline latency by measuring end‑to‑end frame timestamps.
- Source: https://github.com/open-edge-platform/dlstreamer

**Claim-by-claim source quotes:**

- dlstreamer builds media analytics pipelines on GStreamer. ← “GitHub - open-edge-platform/dlstreamer: Deep Learning Streamer (DL Streamer) Pipeline Framework is an open-source streaming media analytics framework, based on GStreamer* multimedia framework, for creating complex media analytics pipelines”

Proposed post (not published):

> dlstreamer builds media analytics pipelines on GStreamer. Validate pipeline latency by measuring end‑to‑end frame timestamps. https://github.com/open-edge-platform/dlstreamer

- Length: 174/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- spatiumnorth/spatiumddi: The factual opening bundles multiple features; narrow it to one capability.
  - Rejected text: spatiumddi runs its own BIND9, PowerDNS, and Kea containers. Test DNS consistency by querying each container after deployment. https://github.com/spatiumnorth/spatiumddi
  - Model evidence quote: “Runs its own BIND9 / PowerDNS / Kea service containers”
  - Claim support: spatiumddi runs its own BIND9, PowerDNS, and Kea containers ← “Runs its own BIND9 / PowerDNS / Kea service containers”
- Show HN: ShellSprint – A typing game-ish for Linux and Kubernetes commands: The factual opening bundles multiple features; narrow it to one capability.; Editorial takeaway needs a concrete test, trade-off, risk, comparison, or next step.; Supporting quotes cover only 56% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: ShellSprint offers typing lessons for Linux, Rancher, Podman, Ansible, and Kubernetes. Track accuracy over time to spot command recall gaps. https://shellsprint-dev.pages.dev
  - Model evidence quote: “Practice Linux, Rancher RKE2, Podman, Ansible and Kubernetes commands”
  - Claim support: ShellSprint offers typing lessons for Linux, Rancher, Podman, Ansible, and Kubernetes ← “Practice Linux, Rancher RKE2, Podman, Ansible and Kubernetes commands”

## Top discovery candidates considered

- spatiumnorth/spatiumddi | GitHub Search | security_and_self_hosting | raw 71, adjusted 65 | current stars 71 | GitHub star trend: building baseline | https://github.com/spatiumnorth/spatiumddi
- open-edge-platform/dlstreamer | GitHub Search | data_and_growth | raw 67, adjusted 61 | current stars 643 | GitHub star trend: building baseline | https://github.com/open-edge-platform/dlstreamer
- Show HN: ShellSprint – A typing game-ish for Linux and Kubernetes commands | Hacker News | product_and_workflow_tools | raw 56, adjusted 58 | https://shellsprint-dev.pages.dev

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
