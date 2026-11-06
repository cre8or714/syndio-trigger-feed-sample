#!/usr/bin/env python3
"""Minimal real tests. Run: python3 test_score.py"""
from score import score_trigger, RULE_VERSION

passed = 0
failed = 0


def check(name, condition):
    global passed, failed
    if condition:
        passed += 1
        print(f"PASS  {name}")
    else:
        failed += 1
        print(f"FAIL  {name}")


# Test 1: a real entry is never quarantined
real_entry = {
    "id": "X1", "company_or_scope": "test", "signal_type": "pay_equity_settlement",
    "observed_fact": "fact", "inference": "inf", "unknown": "none",
    "source_url": "https://example.com/real-source",
    "source_name": "LegalClarity court order", "source_published_date": "2026",
    "accessed_date": "2026-11-06", "event_date": "2026-06-11",
}
r1 = score_trigger(real_entry)
check("entry with a source URL is not quarantined", r1["quarantined"] is False)

# Test 2: an entry with no source URL is quarantined, no matter the score
bad_entry = dict(real_entry)
bad_entry["source_url"] = ""
r2 = score_trigger(bad_entry)
check("entry with no source URL is quarantined", r2["quarantined"] is True)
check("quarantine holds even though subscores still computed high",
      r2["total_score"] >= 80 and r2["quarantined"] is True)

# Test 3: determinism, same input twice gives the identical result
r3a = score_trigger(real_entry)
r3b = score_trigger(real_entry)
check("same input produces identical score (determinism)", r3a == r3b)

# Test 4: unknown event date scores 0 freshness instead of being guessed
unknown_date_entry = dict(real_entry)
unknown_date_entry["event_date"] = "unknown, not stated"
r4 = score_trigger(unknown_date_entry)
check("unknown event date scores 0 freshness, not guessed", r4["subscores"]["freshness"] == 0)

print(f"\n{passed} passed, {failed} failed. Rule version under test: {RULE_VERSION}")
exit(1 if failed else 0)
