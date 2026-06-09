"""42-True — the Large Meaning Model, as a schema and concept seed.

This package defines the **intent pair**, the atomic unit of the proposed
corpus, and a set of conceptual *recipes* for producing it. It is the first
public concept of the model described in the paper
("42-True: A Large Meaning Model for Declared Human Intent"); it is not a
training pipeline, because the corpus it is defined against does not yet exist
and cannot be scraped — it must be produced.
"""

from __future__ import annotations

from forty_two_true.intent_pair import (
    Classification,
    DeclaredIntent,
    IntentPair,
    Match,
    Outcome,
)
from forty_two_true.schema import (
    EXAMPLE_TAXONOMY,
    ClassificationTier,
    OutcomeGrade,
    TaxonomyNode,
)

__version__ = "0.0.1"

__all__ = [
    "Classification",
    "ClassificationTier",
    "DeclaredIntent",
    "EXAMPLE_TAXONOMY",
    "IntentPair",
    "Match",
    "Outcome",
    "OutcomeGrade",
    "TaxonomyNode",
    "__version__",
]
