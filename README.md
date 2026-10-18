# Legivox Automation

Zero-cost GitHub Actions scaffold for rotating through Legivox post ideas and publishing one original standalone post at each scheduled run.

## Important risk

The publisher uses `tweetkit-x`, which replays X website requests with a session cookie rather than using the official API. X's automation rules explicitly prohibit website scripting and warn of possible permanent account suspension. You chose to proceed despite that risk. This repository makes no guarantee the unofficial integration will continue working.

## One-time setup required

1. Sign in to X as **@Legivox** in your browser.
2. Copy the Cookie **value** (not the literal `Cookie:` header label) from a request to `x.com` in Developer Tools → Network. The value must include `auth_token`, `ct0`, and `twid`. Treat it like a password.
3. Open this repository's Settings → Secrets and variables → Actions → New repository secret.
4. Set the name to `X_SESSION_COOKIE` and the value to the raw cookie value. Never put it into source code, an issue, a commit, or this chat.
5. Open the Actions tab and run **Legivox scheduled X publishing** with **Run workflow** to test the first post.

The script verifies that the session's `twid` matches the public profile ID for @Legivox before it can publish. A cookie for a different account fails closed. Do not enable access for untrusted contributors or third-party actions.

## Schedule

The workflow is scheduled for 08:00, 14:00 and 20:00 India Standard Time (02:30, 08:30 and 14:30 UTC). GitHub may delay scheduled runs. It runs on GitHub-hosted runners, so your personal computer does not need to be on.

## Posting safeguards

- One standalone post per workflow run; no replies, DMs, follows, likes or reposts.
- Reads recent @Legivox posts and keeps a SHA-256 ledger to avoid reposting identical text.
- Does not automatically retry an uncertain posting request, because the first request may already have succeeded.
- Logs post IDs, URLs, timestamps and idea IDs in `output/published.jsonl`.
- Rotates through multiple templates per idea. It stops after every existing idea/template combination has been used rather than intentionally repeating old copy. Add fresh, researched ideas to `data/ideas.json` to replenish the queue.

## Research limitation

The starter ideas are hypotheses and have not been verified. This workflow does not scrape live discussions or independently validate demand. Replace and expand them only with evidence and source links you have reviewed. The posting mechanism is automated; market research is still a separate task.
