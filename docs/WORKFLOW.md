# Workflow notes

## What runs automatically
GitHub Actions runs scripts/build_queue.py three times daily. It validates manually maintained idea records and updates output/content-queue.md. The script uses only Python's standard library and does not access X.

## What it does not do
- It does not perform live web research or verify market demand.
- It does not publish, reply, like, repost, follow, or send DMs.
- It does not store X session cookies or credentials.
- Scheduled jobs are not guaranteed to start at the exact minute.

## Add researched ideas
Edit data/ideas.json. Each record needs an ID, niche, problem, evidence, and solution hypothesis. Only enter evidence that has actually been reviewed. Starter ideas are hypotheses, not validated market findings.

## Credential hygiene
Keep the repository free of secrets. If an external service is later added, store credentials in repository Actions secrets and never print them in logs.

## Manual verification
Open the repository's Actions tab and run 'Legivox research and content queue' with Run workflow. Inspect the run and generated output file. Scheduled starts may be delayed by GitHub.
