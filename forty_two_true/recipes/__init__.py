"""Recipes — the four-stage lifecycle that produces an intent pair.

    declare  (Id)  ->  classify  (C)  ->  match  (M)  ->  verify  (O)

Each stage is a small, typed reference implementation. They run end-to-end on
the example data, but they are *concept demonstrations*: the real declaration
vault, classification tiers, counterparty market, and attestation layer do not
exist yet and must be produced (paper §VIII).
"""

from __future__ import annotations

from forty_two_true.recipes.classify import classify
from forty_two_true.recipes.declare import declare
from forty_two_true.recipes.match import match
from forty_two_true.recipes.verify import assemble, observe_outcome

__all__ = ["assemble", "classify", "declare", "match", "observe_outcome"]
