# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-21T23:16:38+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 66
- Drafts passing local checks: 1
- Outcome: **draft_ready_for_human_review**
- Decision reason: At least one draft passed evidence, novelty, claim, URL and length checks. The best eligible option is shown first; nothing was published.

## Source health

| Source | Items kept | Result |
|---|---:|---|
| GitHub Search · github-ai-agent-tools | 10 | ok |
| GitHub Search · github-analytics-seo | 0 | error (HTTPError) |
| GitHub Search · github-creator-infrastructure | 0 | error (HTTPError) |
| GitHub Search · github-developer-tools | 10 | ok |
| GitHub Search · github-ecommerce-digital-products | 0 | error (HTTPError) |
| GitHub Search · github-mcp-servers | 10 | ok |
| GitHub Search · github-self-hosted | 0 | error (HTTPError) |
| GitHub Search · github-shopify-commerce | 0 | error (HTTPError) |
| GitHub Search · github-workflow-automation | 0 | error (HTTPError) |
| Hacker News · hn-analytics-growth | 10 | ok |
| Hacker News · hn-automation-api | 3 | ok |
| Hacker News · hn-creator-business | 0 | ok |
| Hacker News · hn-digital-products | 1 | ok |
| Hacker News · hn-ecommerce-payments | 0 | ok |
| Hacker News · hn-security-selfhost | 0 | ok |
| Hacker News · hn-shopify | 8 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Console.dev | 0 | ok |
| Product Hunt | 31 | ok |
| Shopify Developer Changelog | 5 | ok |

## Selected draft candidates

### Draft option 1: callstack/agent-device

- Category: ai_and_automation
- Source: GitHub Search
- Format: engineering_lesson
- Editorial score: 8.6/10
- Model scores: timeliness 9/10, usefulness 9/10, novelty 7/10, evidence 9/10
- Exact source evidence: “CLI, MCP server, and typed Node.js API for iOS, Android, HarmonyOS, TV, web, macOS, and Linux”
- Why this angle: Shows breadth of supported platforms
- Source: https://github.com/callstack/agent-device

**Claim-by-claim source quotes:**

- Agent‑device offers CLI, MCP server, and Node.js API for multiple OS ← “CLI, MCP server, and typed Node.js API for iOS, Android, HarmonyOS, TV, web, macOS, and Linux”

Proposed post (not published):

> callstack/agent-device – CLI, MCP server, and typed Node.js API for automating iOS, Android, HarmonyOS, TV, web, macOS, and Linux. https://github.com/callstack/agent-device

- Length: 172/280 raw characters
- Required next step: human review of original source, licence/pricing where relevant, and all factual claims.

## Rejected draft options

- Show HN: Slap Alert: Claim quotes cover only 12% of substantive draft terms; cite more of the actual facts
  - Rejected text: Show HN: Slap Alert – a native Mac menu‑bar app that slaps a sticky note on your screen for every sale. Works with Stripe, Paddle, RevenueCat, Shopify, App Store, Polar, Dodo, win cards, and shows weekly sales wall. https://slapalert.com/
  - Model evidence quote: “It's a native Mac menu-bar app for macOS 14 and up”
  - Claim support: Slap Alert is a native Mac menu‑bar app ← “It's a native Mac menu-bar app for macOS 14 and up”
- Show HN: IDE for a general-purpose visual programming language "Pipe": Too many substantive terms are absent from the source title/summary: needed, stores, web
  - Rejected text: Show HN: Pipe IDE – a web‑based visual programming IDE that stores all data locally, no account needed. Try it on https://www.pipelang.com/
  - Model evidence quote: “Pipe IDE requires no account - all data is stored locally in your browser's database”
  - Claim support: Pipe IDE stores data locally ← “Pipe IDE requires no account - all data is stored locally in your browser's database”
- xerj-org/xerj: Claim quotes cover only 6% of substantive draft terms; cite more of the actual facts
  - Rejected text: xerj – a Rust binary that indexes code, docs, logs, JSONL/CSV, PDFs for BM25 full‑text, vector, hybrid search, code search without grep, and RAG. https://github.com/xerj-org/xerj
  - Model evidence quote: “Local-first search engine and MCP server for AI agents”
  - Claim support: xerj is a local‑first search engine for AI agents ← “Local-first search engine and MCP server for AI agents”
- hibi: novelty score is below the minimum 6/10
  - Rejected text: hibi – an open‑source Obsidian alternative. https://www.producthunt.com/products/hibi
  - Model evidence quote: “an open-source obsidian alternative”
  - Claim support: hibi is an open‑source Obsidian alternative ← “an open-source obsidian alternative”

## Top discovery candidates considered

- Show HN: Slap Alert | Hacker News | commerce_and_digital_products | raw 65, adjusted 67 | https://slapalert.com/
- Show HN: IDE for a general-purpose visual programming language "Pipe" | Hacker News | product_and_workflow_tools | raw 64, adjusted 66 | https://www.pipelang.com/
- Show HN: PatchWave - Add static analysis and automerge to Dependabot | Hacker News | product_and_workflow_tools | raw 64, adjusted 66 | https://patchwave.ai/
- Show HN: Riff – An iPhone calendar you zoom instead of switching views | Hacker News | product_and_workflow_tools | raw 64, adjusted 66 | https://riffcalendar.com
- Addressing EU Cyber Resilience Act | Hacker News | product_and_workflow_tools | raw 65, adjusted 65 | https://news.ycombinator.com/item?id=50157847

## Safety and interpretation

- A passing draft is a proposal for human review, not an automatic permission to publish.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Primary-source review remains mandatory.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
