"""The intent pair — the atomic unit of the Large Meaning Model corpus.

    IntentPair = ( Id, C, M, O )

where ``Id`` is a declared intent in natural language, ``C`` its classification
against a machine-addressable taxonomy, ``M`` the offer returned in response,
and ``O`` the realised outcome — graded from no-engagement through to a
cryptographically verified resolution (paper §III).

Unlike a static NLU label (assigned by an annotator) or an RLHF preference
(whose consequence is synthetic), the outcome ``O`` is **supplied by the user's
own subsequent action in the world**. The label is not assigned; it is lived.

All models are frozen: an intent pair is a record of what happened, not a
mutable buffer. Corrections produce new records — the corpus grows by
accumulation, never by editing the past in place.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from forty_two_true.schema import ClassificationTier, OutcomeGrade


class DeclaredIntent(BaseModel):
    """``Id`` — a want, stated by the person, in conditions of non-observation.

    Carries the provenance that makes the record legitimate: it was *authored*
    and *consented*, and it is bound only to an unlinkable token, never to a
    persistent identity (the zero-knowledge boundary, paper §VI, Fig. 6).
    """

    model_config = ConfigDict(frozen=True)

    text: str = Field(description="The declaration, in the declarant's own natural language.")
    consented: bool = Field(default=True, description="The declaration was voluntarily authored.")
    authored_at: str = Field(description="ISO-8601 timestamp of authoring.")
    unlinkable_token: str = Field(
        description="Per-declaration token with no persistent identity (paper §VI)."
    )


class Classification(BaseModel):
    """``C`` — the declared intent mapped to a machine-addressable schema node."""

    model_config = ConfigDict(frozen=True)

    taxonomy_code: str = Field(description="Code of the resolved TaxonomyNode.")
    label: str = Field(description="Human-readable label of the resolved node.")
    tier: ClassificationTier = Field(description="Which tier resolved the signal.")
    confidence: float = Field(ge=0.0, le=1.0, description="Resolver confidence in [0, 1].")


class Match(BaseModel):
    """``M`` — the counterparty offer returned in response to the classification.

    Counterparties see only the classification, never the raw declaration
    (paper §VI). The match is what was *offered*; the outcome records what the
    person then did with it.
    """

    model_config = ConfigDict(frozen=True)

    counterparty_kind: str = Field(description="e.g. 'ad', 'job', 'service'.")
    offer: str = Field(description="The offer presented to the declarant.")


class Outcome(BaseModel):
    """``O`` — the realised outcome, supplied by the world rather than an annotator.

    A grade of ``VERIFIED_RESOLUTION`` should be backed by ``proof_ref`` — a
    reference to a cryptographic attestation — not merely asserted. The outcome
    is the consequence the declarant's own subsequent action produced.
    """

    model_config = ConfigDict(frozen=True)

    grade: OutcomeGrade = Field(description="Position on the outcome ladder.")
    verified: bool = Field(default=False, description="Whether the outcome is attested.")
    proof_ref: Optional[str] = Field(
        default=None, description="Reference to the attestation backing a verified outcome."
    )


class IntentPair(BaseModel):
    """The four-tuple ( Id, C, M, O ): one record of meaning in the corpus.

    Example
    -------
    >>> from forty_two_true import (
    ...     IntentPair, DeclaredIntent, Classification, Match, Outcome,
    ...     ClassificationTier, OutcomeGrade,
    ... )
    >>> pair = IntentPair(
    ...     declared_intent=DeclaredIntent(
    ...         text="a weekend that makes me feel twenty again",
    ...         authored_at="2026-06-01T09:00:00Z",
    ...         unlinkable_token="zk:7f3a...",
    ...     ),
    ...     classification=Classification(
    ...         taxonomy_code="travel.restorative",
    ...         label="Restorative travel",
    ...         tier=ClassificationTier.AGENT,
    ...         confidence=0.91,
    ...     ),
    ...     match=Match(counterparty_kind="service", offer="A spa-and-hiking weekend in the Alps"),
    ...     outcome=Outcome(grade=OutcomeGrade.CONVERSION, verified=True, proof_ref="att:e91c..."),
    ... )
    >>> pair.outcome.grade >= OutcomeGrade.CLICK
    True
    """

    model_config = ConfigDict(frozen=True)

    declared_intent: DeclaredIntent
    classification: Classification
    match: Match
    outcome: Outcome
    corpus_note: str = Field(
        default="Voluntarily authored; outcome anchored in the declarant's own action.",
        description="Provenance reminder carried with every record.",
    )
