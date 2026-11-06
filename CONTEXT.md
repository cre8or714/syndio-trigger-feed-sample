# CONTEXT: Syndio trigger feed

ICM-style layout (Jake Van Clief, Interpretable Context Methodology,
https://github.com/RinDig/Interpretable-Context-Methodology). One agent,
one job per numbered stage, plain text handoff between stages, no
framework, no hidden state.

## Stage map

1. `stages/01-collect` — the 5 real sourced triggers, nothing else
2. `stages/02-validate` — source/evidence gate, quarantines anything unverifiable
3. `stages/03-score` — the fixed deterministic scoring rule
4. `stages/04-review` — human-readable output, the only thing a person reads

## How to run it

    python3 run.py              # walks all 4 stages in order, prints the review
    python3 run.py --json       # same, machine-readable scored output
    python3 test_score.py       # 5 real tests against the scoring stage

## Rule

Each stage reads only the file the stage before it wrote. No stage
reaches back into another stage's internals. Every handoff is plain
JSON or markdown, readable without running any code.
