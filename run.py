#!/usr/bin/env python3
"""Single entry point. Walks stages 01 through 04 in order, each stage
reads only the file the stage before it wrote. This is the ICM pattern:
one agent, one job per numbered folder, plain text handoff between them.

Run: python3 run.py
Run: python3 run.py --json   (prints stage 3's scored.json instead of the review)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "stages" / "01-collect"))
sys.path.insert(0, str(ROOT / "stages" / "02-validate"))
sys.path.insert(0, str(ROOT / "stages" / "03-score"))
sys.path.insert(0, str(ROOT / "stages" / "04-review"))

import collect as stage01     # noqa: E402
import validate as stage02    # noqa: E402
import score as stage03       # noqa: E402
import review as stage04      # noqa: E402


def main():
    collected = stage01.run()
    valid, quarantined = stage02.run(collected)
    scored = stage03.run(valid)

    if "--json" in sys.argv:
        print(json.dumps(scored, indent=2))
        return

    print(stage04.run(scored, quarantined))


if __name__ == "__main__":
    main()
