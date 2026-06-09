"""Tests for the intent-pair primitive and its invariants."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from forty_two_true import (
    Classification,
    ClassificationTier,
    DeclaredIntent,
    IntentPair,
    Match,
    Outcome,
    OutcomeGrade,
)
from forty_two_true.recipes import assemble, classify, declare, match, observe_outcome


def _example_pair() -> IntentPair:
    return IntentPair(
        declared_intent=DeclaredIntent(
            text="a weekend that makes me feel twenty again",
            authored_at="2026-06-01T09:00:00Z",
            unlinkable_token="zk:7f3a1c9e",
        ),
        classification=Classification(
            taxonomy_code="travel.restorative",
            label="Restorative travel",
            tier=ClassificationTier.AGENT,
            confidence=0.91,
        ),
        match=Match(counterparty_kind="service", offer="A spa-and-hiking weekend in the Alps"),
        outcome=Outcome(grade=OutcomeGrade.CONVERSION, verified=True, proof_ref="att:e91c44"),
    )


def test_round_trips_through_json() -> None:
    pair = _example_pair()
    restored = IntentPair.model_validate_json(pair.model_dump_json())
    assert restored == pair


def test_models_are_frozen() -> None:
    pair = _example_pair()
    with pytest.raises(ValidationError):
        pair.declared_intent.text = "tampered"  # type: ignore[misc]


def test_outcome_grade_is_ordered() -> None:
    assert OutcomeGrade.NO_ENGAGEMENT < OutcomeGrade.CLICK < OutcomeGrade.CONVERSION
    assert OutcomeGrade.VERIFIED_RESOLUTION >= OutcomeGrade.CONVERSION


def test_confidence_is_bounded() -> None:
    with pytest.raises(ValidationError):
        Classification(
            taxonomy_code="travel.restorative",
            label="Restorative travel",
            tier=ClassificationTier.AGENT,
            confidence=1.5,
        )


def test_verified_outcome_requires_proof() -> None:
    with pytest.raises(ValueError):
        observe_outcome(OutcomeGrade.VERIFIED_RESOLUTION)
    backed = observe_outcome(OutcomeGrade.VERIFIED_RESOLUTION, proof_ref="att:1aa7e9")
    assert backed.verified is True


def test_recipes_run_end_to_end() -> None:
    intent = declare(
        "there's a leak under the kitchen sink and I can't fix it myself",
        authored_at="2026-06-03T07:15:00Z",
        unlinkable_token="zk:9c01ff52",
    )
    classification = classify(intent.text)
    offer = match(classification)
    outcome = observe_outcome(OutcomeGrade.VERIFIED_RESOLUTION, proof_ref="att:1aa7e9")
    pair = assemble(intent, classification, offer, outcome)

    assert classification.taxonomy_code == "home.repair"
    assert offer.counterparty_kind == "service"
    assert pair.outcome.grade is OutcomeGrade.VERIFIED_RESOLUTION


def test_empty_declaration_is_rejected() -> None:
    with pytest.raises(ValueError):
        declare("   ", authored_at="2026-06-03T07:15:00Z", unlinkable_token="zk:x")
