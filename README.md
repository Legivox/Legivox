# Legivox Automation

A zero-subscription-cost prototype for researching product opportunities, drafting original X posts, and keeping an auditable content queue.

## Important limitation

This repository does **not** automatically publish to X. X's rules prohibit scripting its website instead of using the official API, and unofficial session-cookie tools risk account restrictions. This version focuses on a scheduled content pipeline without storing X credentials. Publishing must use an X-authorized method.

## Scheduled workflow

GitHub Actions runs daily at 08:00, 14:00, and 20:00 UTC (13:30, 19:30, and 01:30 IST). GitHub may delay scheduled starts during high load.

## Run locally

Requires Python 3.11+ and no third-party packages:

```bash
python scripts/build_queue.py
```

## Content standards

- Explore several niches, not only AI.
- Do not invent market statistics, customer quotes, testimonials, or sales claims.
- Prefer observed pain points and clearly label hypotheses.
- No auto-replies, unsolicited DMs, follows, likes, or reposts.
- A human-readable review report is produced; publishing is not performed by this repository.

## Activity note

GitHub can disable scheduled workflows after long periods of repository inactivity. Check the Actions tab after the first scheduled run.
