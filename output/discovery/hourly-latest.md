# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-27T10:47:48+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 87
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
| Hacker News · hn-shopify | 6 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Console.dev | 12 | ok |
| Product Hunt | 40 | ok |
| Shopify Developer Changelog | 9 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 78
- Previously tracked repositories refreshed outside search results: 122
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 9
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| HKUDS/nanobot | yes | 200 | https://github.com/HKUDS/nanobot |
| IHUI-INF-AI/IHUI-AI | yes | 200 | https://github.com/IHUI-INF-AI/IHUI-AI |
| Ask HN: How do you handle time-series metrics at scale without a large bill? | yes | 200 | https://news.ycombinator.com/item?id=50253890 |

## Selected draft candidates

### Draft option 1: HKUDS/nanobot

- Category: ai_and_automation
- Source: GitHub Search
- Format: tool_discovery
- Editorial score: 8.65/10
- Model scores: timeliness 10/10, usefulness 8/10, novelty 7/10, evidence 10/10, insight 8/10
- Independent editor scores: {"clarity_score": 9, "technical_coherence_score": 9, "takeaway_value_score": 7, "source_faithfulness_score": 9, "originality_score": 7, "reason": "Clear, accurate claim with source support; takeaway adds a practical validation step.", "passed": true}
- Live primary page: https://github.com/HKUDS/nanobot (HTTP 200)
- Exact source evidence: “Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps”
- Why this angle: The primary source explicitly describes Nanobot’s lightweight, self‑hosted nature and WebUI support, enabling a focused implementation test of the UI rendering.
- Editorial takeaway: Validate that the WebUI correctly renders agent state before deploying to production.
- Source: https://github.com/HKUDS/nanobot

**Claim-by-claim source quotes:**

- Nanobot is an ultra‑lightweight Python framework for self‑hosted AI agents with a WebUI. ← “Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps”

Proposed post (not published):

> Nanobot is an ultra‑lightweight Python framework for self‑hosted AI agents with a WebUI. Validate that the WebUI correctly renders agent state before deploying to production. https://github.com/HKUDS/nanobot

- Length: 207/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- IHUI-INF-AI/IHUI-AI: The factual opening bundles multiple features; narrow it to one capability.
  - Rejected text: IHUI‑AI is an AI operating system that unifies 176 LLMs via LangGraph, MCP, and A2A. Test multi‑tenant RLS by attempting cross‑table access with a non‑owner role. https://github.com/IHUI-INF-AI/IHUI-AI
  - Model evidence quote: “Eight-platform full-stack AI operating system - unifies 176 LLMs via LangGraph + MCP + A2A. Multi-tenant RLS over 340 tables, RAG knowledge base, agent marketplace.”
  - Claim support: IHUI‑AI is an AI operating system that unifies 176 LLMs via LangGraph, MCP, and A2A. ← “Eight-platform full-stack AI operating system - unifies 176 LLMs via LangGraph + MCP + A2A. Multi-tenant RLS over 340 tables, RAG knowledge base, agent marketplace.”
- Ask HN: How do you handle time-series metrics at scale without a large bill?: Primary-source evidence quote is oversized or dominated by page navigation; use a concise source-backed excerpt.; Claim evidence quote is oversized or dominated by page navigation; use a concise source-backed excerpt.; Factual sentence includes terms absent from the source title/summary: asks, effective, pick, thread
  - Rejected text: Ask HN thread asks how to pick a cost‑effective time‑series database for analytics. Benchmark query latency on PostgreSQL vs ClickHouse for your typical write‑heavy workload. https://news.ycombinator.com/item?id=50253890
  - Model evidence quote: “I've considered just standard PostgreSQL, SQLite on the edge (Cloudflare D1 / Turso), purpose built columnar databases (Clickhouse, DuckDB) and the ones managed by big cloud like Google BigQuery, Amazon Timestream, and Cloudflare Analytics Engine.”
  - Claim support: Ask HN thread asks how to pick a cost‑effective time‑series database for analytics. ← “I've considered just standard PostgreSQL, SQLite on the edge (Cloudflare D1 / Turso), purpose built columnar databases (Clickhouse, DuckDB) and the ones managed by big cloud like Google BigQuery, Amazon Timestream, and Cloudflare Analytics Engine.”

## Top discovery candidates considered

- HKUDS/nanobot | GitHub Search | ai_and_automation | raw 71, adjusted 75 | current stars 49440 | GitHub star trend: building baseline | https://github.com/HKUDS/nanobot
- IHUI-INF-AI/IHUI-AI | GitHub Search | security_and_self_hosting | raw 71, adjusted 75 | current stars 31 | GitHub star trend: building baseline | https://github.com/IHUI-INF-AI/IHUI-AI
- Ask HN: How do you handle time-series metrics at scale without a large bill? | Hacker News | data_and_growth | raw 69, adjusted 69 | https://news.ycombinator.com/item?id=50253890

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
