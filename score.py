#!/usr/bin/env python3
"""
Deterministic trigger scorer. Research-priority score, not a buying
probability. Same four categories CompSignal proposed, no app around it,
just a function you can run and read.

Run: python3 score.py
Run: python3 score.py --json   (for machine-readable output)
"""
import json
import sys
from datetime import date

from triggers import TRIGGERS

RULE_VERSION = "trigger-score-v1"

# Fixed, documented weight table. No hidden numbers, no model call.
ICP_FIT_POINTS = 30          # Does the scope/company match Syndio's buyer profile
                              # (employer with pay governance exposure)?
SIGNAL_STRENGTH_POINTS = {   # How direct is this as a compensation-governance trigger
    "regulatory_deadline_miss": 25,
    "pay_transparency_settlement": 25,
    "pay_equity_settlement": 22,
}
EVIDENCE_STRENGTH_POINTS = { # Source reliability: named court order/regulator tracker
                              # beats a secondary blog summary of a settlement.
    "primary_or_regulator": 20,
    "named_court_order": 20,
    "secondary_summary": 12,
}
FRESHNESS_FULL_DAYS = 365    # Full points if event happened within the last year
TODAY = date(2026, 11, 6)


def parse_year_or_date(value: str):
    """Best-effort parse. Returns a date or None if the value is not a real date."""
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
    """Primary/regulator or a named court order beats a secondary roundup blog."""
    source = entry["source_name"].lower()
    if "deloitte" in source or "legalclarity" in source or "courthouse" in source:
        return "named_court_order" if "court" in entry["observed_fact"].lower() else "primary_or_regulator"
    return "secondary_summary"


def score_trigger(entry: dict) -> dict:
    icp = ICP_FIT_POINTS  # all 5 entries are confirmed employers/scopes with real exposure
    signal = SIGNAL_STRENGTH_POINTS.get(entry["signal_type"], 0)

    tier = evidence_tier(entry)
    evidence = EVIDENCE_STRENGTH_POINTS[tier]

    event_dt = parse_year_or_date(entry["event_date"])
    if event_dt is None:
        freshness = 0
        freshness_note = "event date unknown or unverifiable, scored 0, not guessed"
    else:
        age_days = (TODAY - event_dt).days
        if age_days < 0:
            age_days = 0
        freshness = max(0, round(15 * max(0, 1 - age_days / (FRESHNESS_FULL_DAYS * 2))))
        freshness_note = f"event date {entry['event_date']}, {age_days} days old"

    buyer_path = 10  # function-level buyer path is clear (CHRO, Legal, Comp team),
                      # no named individual guessed, per the no-named-contact rule

    total = icp + signal + evidence + freshness + buyer_path

    # Hard gate: an entry with no verifiable source URL would be quarantined
    # regardless of score. All 5 have one, so none are quarantined here.
    quarantined = not entry.get("source_url")

    return {
        "id": entry["id"],
        "company_or_scope": entry["company_or_scope"],
        "rule_version": RULE_VERSION,
        "subscores": {
            "icp_fit": icp,
            "signal_strength": signal,
            "evidence_strength": evidence,
            "evidence_tier": tier,
            "freshness": freshness,
            "freshness_note": freshness_note,
            "buyer_path_clarity": buyer_path,
        },
        "total_score": total,
        "quarantined": quarantined,
        "source_url": entry["source_url"],
        "observed_fact": entry["observed_fact"],
        "inference": entry["inference"],
        "unknown": entry["unknown"],
    }


def main():
    results = [score_trigger(e) for e in TRIGGERS]
    results.sort(key=lambda r: r["total_score"], reverse=True)

    if "--json" in sys.argv:
        print(json.dumps(results, indent=2))
        return

    print(f"Rule version: {RULE_VERSION}  |  scored as of {TODAY.isoformat()}\n")
    for r in results:
        print(f"[{r['id']}] {r['company_or_scope']}  ->  score {r['total_score']}/100"
              + ("  QUARANTINED" if r["quarantined"] else ""))
        s = r["subscores"]
        print(f"    icp_fit={s['icp_fit']}  signal={s['signal_strength']}  "
              f"evidence={s['evidence_strength']} ({s['evidence_tier']})  "
              f"freshness={s['freshness']} ({s['freshness_note']})  "
              f"buyer_path={s['buyer_path_clarity']}")
        print(f"    fact: {r['observed_fact'][:110]}...")
        print(f"    source: {r['source_url']}")
        print()


if __name__ == "__main__":
    main()
