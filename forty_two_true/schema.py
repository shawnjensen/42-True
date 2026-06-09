"""Shared enumerations and taxonomy types for the Large Meaning Model.

These types encode two structural commitments from the paper
("42-True: A Large Meaning Model for Declared Human Intent"):

* Classification is performed by a **three-tier architecture** — specialist
  agents, opted-in community, and independent experts (paper §V, Fig. 5).
* An outcome is graded on an **ordered ladder**, from no engagement through a
  cryptographically verified resolution (paper §III).

Everything here is small, typed, and import-light on purpose: this repository
is a schema and concept seed, not a training pipeline.
"""

from __future__ import annotations

from enum import Enum, IntEnum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ClassificationTier(str, Enum):
    """Which tier of the classification architecture resolved a signal.

    The tiers compensate for one another's failure modes (paper §V):

    * ``AGENT``     — specialist agents resolve high-confidence signals.
    * ``COMMUNITY`` — opted-in users resolve the ambiguous middle by vote.
    * ``EXPERT``    — independent domain experts handle the long tail and audit.
    """

    AGENT = "agent"
    COMMUNITY = "community"
    EXPERT = "expert"


class OutcomeGrade(IntEnum):
    """The realised outcome of a declared intent, as an ordered ladder.

    Ordering is meaningful: a conversion outranks a click, which outranks no
    engagement. Modelled as an ``IntEnum`` so comparisons (``>=``) and reward
    shaping read naturally. The outcome is *supplied by the world* — the
    subsequent action of the declarant — never assigned by an annotator.
    """

    NO_ENGAGEMENT = 0
    CLICK = 1
    QUALIFIED_LEAD = 2
    CONVERSION = 3
    VERIFIED_RESOLUTION = 4


class TaxonomyNode(BaseModel):
    """A node in the machine-addressable classification schema.

    A declared signal arrives as natural language and must be mapped to one of
    these nodes (paper §V). Kept deliberately tiny here — a real taxonomy is a
    living artefact extended by the expert tier.
    """

    model_config = ConfigDict(frozen=True)

    code: str = Field(description="Stable machine-addressable code, e.g. 'travel.restorative'.")
    label: str = Field(description="Human-readable label.")
    parent: Optional[str] = Field(default=None, description="Parent node code, if any.")


# A minimal illustrative taxonomy. Not authoritative — a demonstration of shape.
EXAMPLE_TAXONOMY: tuple[TaxonomyNode, ...] = (
    TaxonomyNode(code="travel", label="Travel"),
    TaxonomyNode(code="travel.restorative", label="Restorative travel", parent="travel"),
    TaxonomyNode(code="career", label="Career"),
    TaxonomyNode(code="career.transition", label="Career transition", parent="career"),
    TaxonomyNode(code="home", label="Home & living"),
    TaxonomyNode(code="home.repair", label="Home repair", parent="home"),
)
