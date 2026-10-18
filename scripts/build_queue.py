import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDEAS = ROOT / "data" / "ideas.json"
OUTPUT = ROOT / "output"
REPORT = OUTPUT / "content-queue.md"
STATE = OUTPUT / "queue-state.json"

def clean(value):
    return " ".join(str(value).split()).strip()

def main():
    ideas = json.loads(IDEAS.read_text(encoding="utf-8"))
    if not isinstance(ideas, list):
        raise ValueError("data/ideas.json must contain a JSON list")
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    ideas = [row for row in ideas if isinstance(row, dict) and row.get("publish_text")]
    if not ideas:
        raise ValueError("Add at least one reviewed publish_text to data/ideas.json")
    last_id = state.get("last_idea_id")
    current = next((i for i, row in enumerate(ideas) if row["id"] == last_id), -1)
    item = ideas[(current + 1) % len(ideas)]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    draft = clean(item["publish_text"])
    lines = [
        "# Legivox content queue", "", "Generated: " + now, "",
        "> Individually written exploratory drafts. Starter records are hypotheses, not verified market research.", "",
        "## Suggested post", "", draft, "",
        "## Research record", "",
        "- Niche: " + clean(item["niche"]),
        "- Problem: " + clean(item["problem"]),
        "- Evidence status: " + clean(item["evidence"]),
        "- Product hypothesis: " + clean(item["solution_hypothesis"]),
        "- Idea ID: " + clean(item["id"]), "",
        "## Review checklist", "",
        "- [ ] Add source links for claims before describing them as evidence.",
        "- [ ] Check recent posts for repetition.",
        "- [ ] Confirm the copy is useful and sounds natural before publishing.", ""
    ]
    OUTPUT.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print("Wrote output/content-queue.md for " + item["id"])

if __name__ == "__main__":
    main()
