"""Stage 01: collect. Writes collected.json from the real trigger data.
Reads nothing. Produces the only input the rest of the pipeline uses."""
import json
import sys
from pathlib import Path

from triggers import TRIGGERS

OUT = Path(__file__).parent / "collected.json"


def run():
    OUT.write_text(json.dumps(TRIGGERS, indent=2))
    return TRIGGERS


if __name__ == "__main__":
    data = run()
    print(f"Collected {len(data)} triggers -> {OUT}", file=sys.stderr)
