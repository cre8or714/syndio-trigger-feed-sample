# CONTEXT: 03-score

**Inputs:** `../02-validate/validated.json`. Quarantined records never
reach this stage, so this stage can never un-quarantine anything.

**Process:** apply the fixed, documented four-part rule, ICP fit,
signal strength, evidence strength, freshness, buyer path clarity.
Same rule, same weights, every time. No model call, no judgment call.

**Outputs:** `scored.json`, every validated record with its subscores
and total, sorted highest first.

**Checkpoint:** identical input always produces the identical score.
Proven in `../../test_score.py`, not just claimed here.

**Audit:** `scored.json` is plain JSON, every subscore is visible
next to the fact it was computed from.
