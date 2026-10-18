import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDEAS = ROOT / "data" / "ideas.json"
OUTPUT = ROOT / "output"
REPORT = OUTPUT / "content-queue.md"
STATE = OUTPUT / "queue-state.json"

def clean(value):
    return re.sub(r"\s+", " ", str(value)).strip()

def main():
    ideas = json.loads(IDEAS.read_text(encoding="utf-8"))
    if not isinstance(ideas, list):
        raise ValueError("data/ideas.json must contain a JSON list")
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    required = ("id", "niche", "problem", "evidence", "solution_hypothesis")
    ideas = [row for row in ideas if isinstance(row, dict) and all(row.get(key) for key in required)]
    if not ideas:
        raise ValueError("Add at least one complete idea to data/ideas.json")
    last_id = state.get("last_idea_id")
    current = next((i for i, row in enumerate(ideas) if row["id"] == last_id), -1)
    item = ideas[(current + 1) % len(ideas)]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    draft = (
        "One problem worth exploring in " + clean(item["niche"]) + ": "
        + clean(item["problem"]) + " A possible product hypothesis: "
        + clean(item["solution_hypothesis"])
        + " What evidence would prove this matters? Real user behaviour, not just likes or compliments."
    )
    lines = [
        "# Legivox content queue", "", "Generated: " + now, "",
        "> Draft only. No post is published automatically. Starter ideas are hypotheses, not market validation.", "",
        "## Suggested draft", "", draft, "",
        "## Research record", "",
        "- Niche: " + clean(item["niche"]),
        "- Problem: " + clean(item["problem"]),
        "- Evidence status: " + clean(item["evidence"]),
        "- Solution hypothesis: " + clean(item["solution_hypothesis"]),
        "- Idea ID: " + clean(item["id"]), "",
        "## Review checklist", "",
        "- [ ] Verify the evidence and save source links.",
        "- [ ] Remove unsupported or exaggerated claims.",
        "- [ ] Check recent posts for repetition.",
        "- [ ] Publish only through a method authorized by X.", ""
    ]
    OUTPUT.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    state = {"last_idea_id": item["id"], "generated_at": now}
    STATE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    print("Wrote output/content-queue.md for " + item["id"])

if __name__ == "__main__":
    main()
