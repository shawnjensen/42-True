"""Recipe 2 — Classify (``C``).

Map a declared signal to a machine-addressable taxonomy node. The paper's
three-tier architecture (paper §V, Fig. 5) routes by confidence:

* high confidence  -> specialist **agents**,
* the ambiguous middle -> opted-in **community** vote,
* the long tail and audit -> independent **experts**.

The function below is a deliberately naive keyword resolver standing in for the
agent tier. It exists to make the pipeline runnable on the example data, not to
classify anything for real — a genuine resolver is domain-tuned and audited.
"""

from __future__ import annotations

from forty_two_true.intent_pair import Classification
from forty_two_true.schema import EXAMPLE_TAXONOMY, ClassificationTier, TaxonomyNode

# Illustrative keyword cues per taxonomy code. A real resolver does far more.
_CUES: dict[str, tuple[str, ...]] = {
    "travel.restorative": ("weekend", "twenty again", "getaway", "recharge", "rest"),
    "career.transition": ("new job", "career", "switch", "leave my job", "hiring"),
    "home.repair": ("leak", "fix", "broken", "repair", "plumber"),
}

_BY_CODE: dict[str, TaxonomyNode] = {node.code: node for node in EXAMPLE_TAXONOMY}


def classify(text: str, *, confidence_floor: float = 0.6) -> Classification:
    """Resolve ``text`` to a taxonomy node via a toy agent-tier heuristic.

    Returns the best-matching leaf node. If nothing matches above the floor, the
    signal is routed to the community tier with low confidence — mirroring the
    real escalation path, where ambiguity is resolved by vote, not guessing.
    """

    lowered = text.lower()
    best_code: str | None = None
    best_hits = 0
    for code, cues in _CUES.items():
        hits = sum(1 for cue in cues if cue in lowered)
        if hits > best_hits:
            best_hits, best_code = hits, code

    if best_code is None or best_hits == 0:
        return Classification(
            taxonomy_code="unresolved",
            label="Unresolved — route to community",
            tier=ClassificationTier.COMMUNITY,
            confidence=0.25,
        )

    node = _BY_CODE[best_code]
    confidence = min(1.0, confidence_floor + 0.15 * best_hits)
    return Classification(
        taxonomy_code=node.code,
        label=node.label,
        tier=ClassificationTier.AGENT,
        confidence=confidence,
    )
