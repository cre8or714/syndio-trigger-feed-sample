"""
Real trigger data for the Syndio proof sample.
Every entry is a public, dated, linkable source. Nothing invented.
Each field is explicitly labeled: observed_fact, inference, or unknown.
Unsupported or undated claims are left as unknown rather than guessed.
"""

TRIGGERS = [
    {
        "id": "T1",
        "company_or_scope": "Any multinational employer with EU headcount",
        "signal_type": "regulatory_deadline_miss",
        "observed_fact": (
            "Only 4 of 27 EU member states (Italy, Lithuania, Malta, Slovakia) "
            "met the 7 June 2026 transposition deadline for the EU Pay "
            "Transparency Directive. First gender pay gap reports are due "
            "2027 to 2028 depending on employer size."
        ),
        "inference": (
            "Employers with EU operations likely do not yet have a working "
            "gender pay gap reporting process in place, since most member "
            "states have not finalized the implementing rules they would "
            "report against."
        ),
        "unknown": "Which specific companies are behind on this. Not named here.",
        "source_url": "https://www.deloitte.com/be/en/services/tax/analysis/eu-pay-transparency-directive.html",
        "source_name": "Deloitte EU Pay Transparency Directive Legal Tracker",
        "source_published_date": "2026-10-21",
        "accessed_date": "2026-11-06",
        "event_date": "2026-06-07",
    },
    {
        "id": "T2",
        "company_or_scope": "IHOP franchise operator, Washington locations",
        "signal_type": "pay_transparency_settlement",
        "observed_fact": (
            "An IHOP franchise operator with several Washington locations "
            "agreed to a 6.3 million dollar settlement in 2025 resolving "
            "claims it did not disclose wage scales and salary ranges in "
            "job postings, violating Washington state law."
        ),
        "inference": (
            "Multi-location employers that post jobs in Washington without "
            "salary ranges carry comparable exposure."
        ),
        "unknown": "Exact settlement date, franchise operator's legal name.",
        "source_url": "https://us.bbrown.com/blog/epl-market-update-2026-pay-transparency-and-pay-equity-litigation",
        "source_name": "Brown & Brown, EPL Market Update 2026",
        "source_published_date": "2026",
        "accessed_date": "2026-11-06",
        "event_date": "2025",
    },
    {
        "id": "T3",
        "company_or_scope": "Target Corporation",
        "signal_type": "pay_transparency_settlement",
        "observed_fact": (
            "Target agreed to a 2.25 million dollar settlement of a class "
            "action alleging it failed to disclose wage scales and salary "
            "ranges in Washington job postings, in violation of state law."
        ),
        "inference": "Large multi-state retailers carry the same posting-disclosure exposure.",
        "unknown": "Exact settlement date, not stated in the source beyond 'recently' as of a 2026 article.",
        "source_url": "https://us.bbrown.com/blog/epl-market-update-2026-pay-transparency-and-pay-equity-litigation",
        "source_name": "Brown & Brown, EPL Market Update 2026",
        "source_published_date": "2026",
        "accessed_date": "2026-11-06",
        "event_date": "unknown, reported as recent in a 2026 article",
    },
    {
        "id": "T4",
        "company_or_scope": "The Walt Disney Company",
        "signal_type": "pay_equity_settlement",
        "observed_fact": (
            "A California court approved a 43 million dollar settlement in "
            "2025 resolving gender pay discrimination claims against Disney, "
            "where plaintiffs alleged female employees were paid less than "
            "male counterparts in comparable roles."
        ),
        "inference": (
            "Companies with no real-time pay governance layer keep landing "
            "in settlements of this size, this is a pattern, not an isolated case."
        ),
        "unknown": "Exact approval date within 2025.",
        "source_url": "https://us.bbrown.com/blog/epl-market-update-2026-pay-transparency-and-pay-equity-litigation",
        "source_name": "Brown & Brown, EPL Market Update 2026",
        "source_published_date": "2026",
        "accessed_date": "2026-11-06",
        "event_date": "2025",
    },
    {
        "id": "T5",
        "company_or_scope": "Google LLC",
        "signal_type": "pay_equity_settlement",
        "observed_fact": (
            "A US Magistrate Judge granted final approval on 11 June 2026 "
            "of a 50 million dollar settlement covering more than 4,000 "
            "current and former Black Google employees, resolving claims "
            "the company systematically underpaid and under-promoted them. "
            "Google also agreed to three years of pay equity review reforms."
        ),
        "inference": (
            "Even a company with mature HR systems and heavy prior scrutiny "
            "still needed a court-ordered pay equity review process, this is "
            "the ceiling case for why a continuous governance layer matters."
        ),
        "unknown": "Nothing material, this fact is well documented with a named court order.",
        "source_url": "https://legalclarity.org/google-discrimination-lawsuit-settlements-and-verdicts/",
        "source_name": "LegalClarity, Google Discrimination Lawsuit: Settlements and Verdicts",
        "source_published_date": "2026-06-18",
        "accessed_date": "2026-11-06",
        "event_date": "2026-06-11",
    },
]
