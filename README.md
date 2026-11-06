# Syndio trigger feed, a small functioning sample

This is a real, runnable tool, not a write-up. It takes 5 real, dated,
linked compensation-governance signals and scores them with a fixed,
documented rule, the same kind of trigger feed method behind ARI and
Set n Scale, applied to what Syndio's own GTM team would use.

## Run it

    python3 score.py           # readable output
    python3 score.py --json    # machine-readable
    python3 test_score.py      # 5 real tests, including the quarantine gate

## What it does

Each trigger in `triggers.py` is a real public source: a regulatory
tracker or a reported settlement, with a source URL, a published date,
and the specific fact it supports. Every entry separates observed fact,
inference, and unknown. Nothing is guessed into a date or a number.

`score.py` applies a fixed four-part rule to every trigger:

- ICP fit, 0 to 30: does the scope match an employer with real
  compensation-governance exposure
- Signal strength, 0 to 25: how direct a trigger is a regulatory
  deadline miss or settlement, versus a softer signal
- Evidence strength, 0 to 20: a regulator tracker or a named court
  order scores higher than a secondary summary blog
- Freshness, 0 to 15: decays with the real age of the event, an
  unknown date scores 0 rather than being guessed
- Buyer path clarity, 0 to 10: whether a real function, CHRO, Legal,
  Comp, is the clear buyer, never a named individual guessed from a
  LinkedIn search

Any entry missing a real source URL is quarantined regardless of
score. `test_score.py` proves that gate actually holds, not just
claimed.

## What this is not

Not a CRM, not a database, not a multi-user app. No auth, no
integrations, no deployment. It is sized to prove one thing: that the
same public-record trigger method behind Set n Scale and ARI applies
cleanly to Syndio's own market.

## Sources

- Deloitte, EU Pay Transparency Directive Legal Tracker, updated 21 Oct 2026
- Brown & Brown, EPL Market Update 2026
- LegalClarity, Google Discrimination Lawsuit: Settlements and Verdicts

## Known gaps

Two of the five entries (Target, Disney) rely on a secondary summary
article rather than a primary court filing, and the Target settlement's
exact date is not stated anywhere I could verify, it is marked unknown
and scores 0 on freshness as a result. This is disclosed, not hidden.
