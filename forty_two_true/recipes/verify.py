"""Recipe 4 — Verify (``O``) and assemble the intent pair.

The outcome is *supplied by the world* — the declarant's own subsequent action
— and, in the verified mode, is cryptographically attested (paper §III, §VI).
A grade of ``VERIFIED_RESOLUTION`` therefore requires a ``proof_ref``; this
recipe refuses to fabricate one.

The completed four-tuple is stored as an immutable record. Each completed cycle
retrains both the classifier and the Large Meaning Model (the compounding loop,
paper §IV.C, Fig. 4).
"""

from __future__ import annotations

from forty_two_true.intent_pair import (
    Classification,
    DeclaredIntent,
    IntentPair,
    Match,
    Outcome,
)
from forty_two_true.schema import OutcomeGrade


def observe_outcome(grade: OutcomeGrade, *, proof_ref: str | None = None) -> Outcome:
    """Record a realised outcome, enforcing that verification is backed by proof."""

    verified = grade is OutcomeGrade.VERIFIED_RESOLUTION
    if verified and not proof_ref:
        raise ValueError(
            "A VERIFIED_RESOLUTION outcome must carry a proof_ref — "
            "the outcome is attested by the world, not asserted by a label."
        )
    return Outcome(grade=grade, verified=verified, proof_ref=proof_ref)


def assemble(
    declared_intent: DeclaredIntent,
    classification: Classification,
    match: Match,
    outcome: Outcome,
) -> IntentPair:
    """Assemble the four parts into a stored, immutable intent pair."""

    return IntentPair(
        declared_intent=declared_intent,
        classification=classification,
        match=match,
        outcome=outcome,
    )
