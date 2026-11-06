# Syndio trigger feed, a small functioning sample

A real, runnable tool, not a write-up. Built as ICM (Interpretable
Context Methodology, Jake Van Clief,
https://github.com/RinDig/Interpretable-Context-Methodology): one
agent, one job per numbered stage, plain text handoff between stages,
no framework underneath it. See `CONTEXT.md` for the stage map.

It takes 5 real, dated, linked compensation-governance signals and
scores them with a fixed, documented rule, the same trigger feed
method behind ARI and Set n Scale, applied to what Syndio's own GTM
team would use.

## Run it

    python3 run.py              # walks all 4 stages, prints the review
    python3 run.py --json       # same, machine-readable scored output
    python3 test_score.py       # real tests, including the quarantine gate

## Stages

1. `stages/01-collect` — the 5 sourced signals, nothing computed
2. `stages/02-validate` — source gate, quarantines anything unverifiable
   before scoring ever sees it
3. `stages/03-score` — the fixed four-part rule: ICP fit, signal
   strength, evidence strength, freshness, buyer path clarity
4. `stages/04-review` — the one human-readable output, `review.md`

Each stage has its own `CONTEXT.md` with Inputs, Process, Outputs,
Checkpoint, Audit. Open any of them directly, no code required, to
see exactly what that step does and why.

Every record separates observed fact, inference, and unknown.
Nothing is guessed into a date or a number. An entry missing a real
source is quarantined in stage 2, before stage 3 ever computes a
score for it, that gate cannot be bypassed by a high score because
scoring never sees quarantined records.

## What this is not

Not a CRM, not a database, not a multi-user app. No auth, no
integrations, no deployment. Sized to prove one thing: that the same
public-record trigger method behind Set n Scale and ARI applies
cleanly to Syndio's own market, built the way the role would expect
a pipeline to be built, inspectable at every step.

## Sources

- Deloitte, EU Pay Transparency Directive Legal Tracker, updated 21 Oct 2026
- Brown & Brown, EPL Market Update 2026
- LegalClarity, Google Discrimination Lawsuit: Settlements and Verdicts

## Known gaps

Two of the five entries (Target, Disney) rely on a secondary summary
article rather than a primary court filing, and the Target
settlement's exact date is not stated anywhere verifiable, it is
marked unknown and scores 0 on freshness as a result. Disclosed, not
hidden.
