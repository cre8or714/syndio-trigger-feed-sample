# CONTEXT: 01-collect

**Inputs:** none. This is the entry point.

**Process:** hold the 5 real, dated, sourced compensation-governance
signals as plain Python data. Every entry separates observed_fact,
inference, and unknown. Nothing here is computed or judged, this
stage only holds what was actually found and where it came from.

**Outputs:** `collected.json`, a plain list of the 5 trigger records,
written by `collect.py`.

**Checkpoint:** every record has a non-empty `source_url` and a
`source_name`. If either is missing, the record still passes through
to stage 2, which is the stage responsible for catching that, not
this one.

**Audit:** `collected.json` is plain JSON, open it in any text editor
to see exactly what entered the pipeline before any scoring touched it.
