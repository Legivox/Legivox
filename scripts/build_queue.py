import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDEAS = ROOT / "data" / "ideas.json"
OUT = ROOT / "output" / "content-queue.md"

def main():
    records = json.loads(IDEAS.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        raise ValueError("data/ideas.json must contain a JSON list")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Legivox content queue",
        "",
        "Generated: " + now,
        "",
        "> Drafts only. No post is published automatically. Verify evidence before sharing.",
        ""
    ]
    if not records:
        lines += ["No ideas available yet.", ""]
    else:
        index = (datetime.now(timezone.utc).hour // 6) % len(records)
        item = records[index]
        draft = (
            "One problem worth exploring in " + item["niche"] + ": "
            + item["problem"] + " A possible product hypothesis: "
            + item["solution_hypothesis"]
            + " What evidence would prove this matters? Real user behaviour, not just likes or compliments."
        )
        lines += [
            "## Suggested draft",
            "",
            draft,
            "",
            "## Research record",
            "",
            "- Niche: " + item["niche"],
            "- Problem: " + item["problem"],
            "- Evidence status: " + item["evidence"],
            "- Solution hypothesis: " + item["solution_hypothesis"],
            "- Idea ID: " + item["id"],
            "",
            "## Review checklist",
            "",
            "- [ ] Verify the evidence and save source links.",
            "- [ ] Remove unsupported claims.",
            "- [ ] Check recent posts for repetition.",
            "- [ ] Use only a publishing method authorized by X.",
            ""
        ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("Wrote output/content-queue.md")

if __name__ == "__main__":
    main()
