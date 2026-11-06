"""Stage 03: score. Reads validated.json, writes scored.json.
The deterministic rule itself, no quarantine logic lives here,
that already happened in stage 02."""
import json
import sys
from datetime import date
from pathlib import Path

IN = Path(__file__).parent.parent / "02-validate" / "validated.json"
OUT = Path(__file__).parent / "scored.json"

RULE_VERSION = "trigger-score-v1"
ICP_FIT_POINTS = 30
SIGNAL_STRENGTH_POINTS = {
    "regulatory_deadline_miss": 25,
    "pay_transparency_settlement": 25,
    "pay_equity_settlement": 22,
}
EVIDENCE_STRENGTH_POINTS = {
    "primary_or_regulator": 20,
    "named_court_order": 20,
    "secondary_summary": 12,
}
FRESHNESS_FULL_DAYS = 365
TODAY = date(2026, 11, 6)


def parse_year_or_date(value: str):
    if not value or "unknown" in value.lower():
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        pass
    if value.strip().isdigit() and len(value.strip()) == 4:
        return date(int(value.strip()), 1, 1)
    return None


def evidence_tier(entry: dict) -> str:
    source = entry["source_name"].lower()
    if "deloitte" in source or "legalclarity" in source or "courthouse" in source:
        return "named_court_order" if "court" in entry["observed_fact"].lower() else "primary_or_regulator"
    return "secondary_summary"


def score_one(entry: dict) -> dict:
    icp = ICP_FIT_POINTS
    signal = SIGNAL_STRENGTH_POINTS.get(entry["signal_type"], 0)
    tier = evidence_tier(entry)
    evidence = EVIDENCE_STRENGTH_POINTS[tier]

    event_dt = parse_year_or_date(entry["event_date"])
    if event_dt is None:
        freshness, freshness_note = 0, "event date unknown or unverifiable, scored 0, not guessed"
    else:
        age_days = max(0, (TODAY - event_dt).days)
        freshness = max(0, round(15 * max(0, 1 - age_days / (FRESHNESS_FULL_DAYS * 2))))
        freshness_note = f"event date {entry['event_date']}, {age_days} days old"

    buyer_path = 10
    total = icp + signal + evidence + freshness + buyer_path

    return {
        "id": entry["id"],
        "company_or_scope": entry["company_or_scope"],
        "rule_version": RULE_VERSION,
        "subscores": {
            "icp_fit": icp, "signal_strength": signal,
            "evidence_strength": evidence, "evidence_tier": tier,
            "freshness": freshness, "freshness_note": freshness_note,
            "buyer_path_clarity": buyer_path,
        },
        "total_score": total,
        "quarantined": False,  # anything reaching this stage already passed 02-validate
        "source_url": entry["source_url"],
        "observed_fact": entry["observed_fact"],
        "inference": entry["inference"],
        "unknown": entry["unknown"],
    }


def run(validated: list[dict]):
    scored = [score_one(e) for e in validated]
    scored.sort(key=lambda r: r["total_score"], reverse=True)
    OUT.write_text(json.dumps(scored, indent=2))
    return scored


if __name__ == "__main__":
    validated = json.loads(IN.read_text())
    scored = run(validated)
    print(f"Scored {len(scored)} records -> {OUT}", file=sys.stderr)
