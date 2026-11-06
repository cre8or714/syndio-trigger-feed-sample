"""Stage 02: validate. Reads collected.json, splits into validated and
quarantined. Only checks source presence, no scoring logic lives here."""
import json
import sys
from pathlib import Path

IN = Path(__file__).parent.parent / "01-collect" / "collected.json"
OUT_VALID = Path(__file__).parent / "validated.json"
OUT_QUARANTINE = Path(__file__).parent / "quarantined.json"


def validate_one(entry: dict) -> str | None:
    """Return a reason code if this entry should be quarantined, else None."""
    if not entry.get("source_url"):
        return "SOURCE_MISSING"
    if not entry.get("source_name"):
        return "SOURCE_NAME_MISSING"
    return None


def run(collected: list[dict]):
    valid, quarantined = [], []
    for entry in collected:
        reason = validate_one(entry)
        if reason:
            quarantined.append({**entry, "quarantine_reason": reason})
        else:
            valid.append(entry)
    OUT_VALID.write_text(json.dumps(valid, indent=2))
    OUT_QUARANTINE.write_text(json.dumps(quarantined, indent=2))
    return valid, quarantined


if __name__ == "__main__":
    collected = json.loads(IN.read_text())
    valid, quarantined = run(collected)
    print(f"{len(valid)} validated, {len(quarantined)} quarantined -> {OUT_VALID.parent}",
          file=sys.stderr)
