"""Recipe 3 — Match (``M``).

Counterparties compete on relevance against the *classification*, never the raw
declaration. The signal does not cross the zero-knowledge boundary; only the
schema node does (paper §VI, Fig. 6).

The stub below returns a single illustrative offer keyed on the taxonomy code.
A real market is a live auction of counterparty agents — out of scope for a
concept repository, and impossible without the corpus it would run on.
"""

from __future__ import annotations

from forty_two_true.intent_pair import Classification, Match

# Illustrative offers per taxonomy code.
_OFFERS: dict[str, tuple[str, str]] = {
    "travel.restorative": ("service", "A spa-and-hiking weekend in the Alps"),
    "career.transition": ("job", "A senior role at a mission-driven team"),
    "home.repair": ("service", "A vetted local plumber, available this week"),
}


def match(classification: Classification) -> Match:
    """Return a counterparty offer for a classification.

    Only the classification is visible to the counterparty layer; this function
    never receives the declared text, by design.
    """

    kind, offer = _OFFERS.get(
        classification.taxonomy_code,
        ("none", "No relevant counterparty offer"),
    )
    return Match(counterparty_kind=kind, offer=offer)
