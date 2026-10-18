# Legivox Automation

A zero-subscription-cost workflow that rotates through product-opportunity hypotheses, drafts original X posts, and keeps an auditable content queue. It is an initial scaffold, not a live market-research engine.

## Important limitation

This repository does **not** automatically publish to X. X's rules prohibit scripting its website instead of using the official API, and unofficial session-cookie tools risk account restrictions. The workflow does not access X or store X credentials. Publishing must use an X-authorized method.

## Scheduled workflow

GitHub Actions runs daily at 08:00, 14:00, and 20:00 India Standard Time (02:30, 08:30, and 14:30 UTC). The job rotates between entries in data/ideas.json, creates a draft report in output/content-queue.md, updates its rotation state, and commits output changes. It does not fetch or verify market evidence. Scheduled starts are not guaranteed to occur at the exact minute.

## Run locally

Requires Python 3.11+ and no third-party packages:

```bash
python scripts/build_queue.py
```

## Content standards

- Explore several niches, not only AI.
- Starter entries are hypotheses, not verified demand.
- Do not invent market statistics, customer quotes, testimonials, or sales claims.
- No auto-replies, unsolicited DMs, follows, likes, or reposts.
- A human-readable draft report is produced; this repository does not publish posts.

## Activity note

Scheduled workflows run from the default branch and can be delayed. GitHub automatically disables scheduled workflows in public repositories after 60 days without repository activity. Check the Actions tab after the first run.
