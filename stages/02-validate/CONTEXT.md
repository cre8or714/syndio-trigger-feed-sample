# CONTEXT: 02-validate

**Inputs:** `../01-collect/collected.json`.

**Process:** check every record for a real `source_url` and
`source_name`. Nothing else is judged here, no scoring, no freshness,
just: is there something a person could click and verify.

**Outputs:** `validated.json` (records that pass) and
`quarantined.json` (records that fail, with a reason code). An empty
`quarantined.json` is the expected result when every source is real.

**Checkpoint:** a record with no `source_url` is quarantined no
matter what else is true about it. This gate cannot be overridden by
a high score, because scoring happens in the next stage and never
sees quarantined records.

**Audit:** both output files are plain JSON. `quarantined.json`
always exists, even empty, so you can confirm the gate ran.
