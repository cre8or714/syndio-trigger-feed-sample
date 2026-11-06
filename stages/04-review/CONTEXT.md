# CONTEXT: 04-review

**Inputs:** `../03-score/scored.json`, `../02-validate/quarantined.json`.

**Process:** turn both files into one plain-text report a person can
read without running anything. No scoring logic, no validation logic,
this stage only formats what already happened.

**Outputs:** `review.md`, printed to the terminal and saved to disk.

**Checkpoint:** every scored record shown includes its source URL and
subscore breakdown. Quarantined records are listed too, with the
reason, not silently dropped.

**Audit:** `review.md` is the one file meant for a human to actually
read. Everything above it is for inspection, this is the summary.
