#!/usr/bin/env python3
"""Real tests across the ICM stages. Run: python3 test_score.py"""
import sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "stages" / "02-validate"))
sys.path.insert(0, str(ROOT / "stages" / "03-score"))
from validate import run as validate_run  # noqa: E402
from score import score_one, RULE_VERSION  # noqa: E402

passed = failed = 0


def check(name, condition):
    global passed, failed
    if condition:
        passed += 1
        print(f"PASS  {name}")
    else:
        failed += 1
        print(f"FAIL  {name}")


real_entry = {
    "id": "X1", "company_or_scope": "test", "signal_type": "pay_equity_settlement",
    "observed_fact": "fact", "inference": "inf", "unknown": "none",
    "source_url": "https://example.com/real-source",
    "source_name": "LegalClarity court order", "source_published_date": "2026",
    "accessed_date": "2026-11-06", "event_date": "2026-06-11",
}

# Stage 02 (validate): the quarantine gate itself
valid, quarantined = validate_run([real_entry])
check("entry with a source URL passes validation", len(valid) == 1 and len(quarantined) == 0)

bad_entry = dict(real_entry)
bad_entry["source_url"] = ""
valid2, quarantined2 = validate_run([bad_entry])
check("entry with no source URL is quarantined before scoring ever runs",
      len(valid2) == 0 and len(quarantined2) == 1
      and quarantined2[0]["quarantine_reason"] == "SOURCE_MISSING")

# Stage 03 (score): determinism and honest freshness handling,
# only ever called on records that already passed stage 02
r1 = score_one(real_entry)
check("scoring a validated entry never re-quarantines it", r1["quarantined"] is False)

r1b = score_one(real_entry)
check("same input produces identical score (determinism)", r1 == r1b)

unknown_date_entry = dict(real_entry)
unknown_date_entry["event_date"] = "unknown, not stated"
r2 = score_one(unknown_date_entry)
check("unknown event date scores 0 freshness, not guessed", r2["subscores"]["freshness"] == 0)

print(f"\n{passed} passed, {failed} failed. Rule version under test: {RULE_VERSION}")
sys.exit(1 if failed else 0)
