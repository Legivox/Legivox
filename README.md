# Legivox Automation

A zero-subscription-cost prototype for researching product opportunities, drafting original X posts, and keeping an auditable content queue.

## Important limitation

This repository does **not** automatically publish to X. X's rules prohibit scripting its website instead of using the official API, and unofficial session-cookie tools risk account restrictions. This version focuses on a scheduled content pipeline without storing X credentials. Publishing must use an X-authorized method.

## Scheduled workflow

GitHub Actions runs daily at 08:00, 14:00, and 20:00 India Standard Time (02:30, 08:30, and 14:30 UTC). Times are scheduled, not guaranteed delivery times. GitHub may delay jobs during high load.

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
- A human-readable draft report is produced; this repository does not publish posts.

## Activity note

Scheduled workflows run from the default branch and can be delayed. GitHub automatically disables scheduled workflows in public repositories after 60 days without repository activity. Check the Actions tab after the first run.
