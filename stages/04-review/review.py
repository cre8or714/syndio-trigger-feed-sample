"""Stage 04: review. Reads scored.json and quarantined.json, writes
review.md. Pure formatting, no logic that changes a score or a gate."""
import json
import sys
from pathlib import Path

SCORED_IN = Path(__file__).parent.parent / "03-score" / "scored.json"
QUARANTINE_IN = Path(__file__).parent.parent / "02-validate" / "quarantined.json"
OUT = Path(__file__).parent / "review.md"


def build_review(scored: list[dict], quarantined: list[dict]) -> str:
    lines = ["# Trigger feed review\n"]
    for r in scored:
        s = r["subscores"]
        lines.append(f"## [{r['id']}] {r['company_or_scope']}, {r['total_score']}/100\n")
        lines.append(f"- icp_fit={s['icp_fit']}  signal={s['signal_strength']}  "
                      f"evidence={s['evidence_strength']} ({s['evidence_tier']})  "
                      f"freshness={s['freshness']} ({s['freshness_note']})  "
                      f"buyer_path={s['buyer_path_clarity']}")
        lines.append(f"- fact: {r['observed_fact']}")
        lines.append(f"- inference: {r['inference']}")
        lines.append(f"- unknown: {r['unknown']}")
        lines.append(f"- source: {r['source_url']}\n")
    if quarantined:
        lines.append("## Quarantined, not scored\n")
        for q in quarantined:
            lines.append(f"- [{q['id']}] {q['company_or_scope']}: {q['quarantine_reason']}")
    else:
        lines.append("## Quarantined, not scored\n\nNone, every collected record had a real source.\n")
    return "\n".join(lines)


def run(scored, quarantined):
    text = build_review(scored, quarantined)
    OUT.write_text(text)
    return text


if __name__ == "__main__":
    scored = json.loads(SCORED_IN.read_text())
    quarantined = json.loads(QUARANTINE_IN.read_text())
    print(run(scored, quarantined))
    print(f"\n(also written to {OUT})", file=sys.stderr)
