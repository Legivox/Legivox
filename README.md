# Legivox Automation

Low-cost GitHub Actions scaffold for rotating through individually written Legivox posts and publishing one original standalone post per day.

## Important risk

The publisher uses `tweetkit-x`, which replays X website requests with a session cookie rather than using the official API. X's automation rules prohibit website scripting and warn of possible permanent account suspension. This workflow pins the source to a specific upstream commit because version 0.3.1 is in the upstream repository but is not currently available from PyPI.

## One-time setup

1. Sign in to X as **@Legivox** in your browser.
2. Copy the Cookie **value** (not the literal `Cookie:` header label) from a request to `x.com` in Developer Tools → Network. The value must include `auth_token`, `ct0`, and `twid`. Treat it like a password.
3. Open this repository's Settings → Secrets and variables → Actions → New repository secret.
4. Set the name to `X_SESSION_COOKIE` and the value to the raw cookie value. Never put it into source code, an issue, a commit, or this chat.
5. Open the Actions tab and run **Legivox scheduled X publishing** with **Run workflow** to test a post.

The script verifies that the session matches the public @Legivox profile. A cookie for a different account fails closed.

## Schedule

The workflow is scheduled once daily at 14:00 India Standard Time (08:30 UTC). GitHub may delay scheduled runs. It runs on GitHub-hosted runners.

## Posting safeguards

- One standalone post per workflow run; no replies, DMs, follows, likes or reposts.
- Reads recent @Legivox posts and keeps a SHA-256 ledger to avoid exact duplicate text.
- Does not retry an uncertain posting request automatically.
- Logs post IDs, URLs, timestamps and idea IDs in `output/published.jsonl`.
- Uses a manually written `publish_text` field for each idea, never converting research labels into public copy.
- Stops when all curated drafts have been used rather than repeating generic templates.

## Research limitation

The starter ideas are hypotheses that have not been verified. The workflow does not scrape live discussions or independently validate demand. Add source links and evidence before making market-demand claims. The publishing mechanism is automated; meaningful market research remains a separate task.
