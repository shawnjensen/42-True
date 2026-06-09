"""Recipe 1 — Declare (``Id``).

Construct a consented declared intent inside a domain the person controls.
This is the only step that touches the raw natural-language signal; from here
on, counterparties see classifications, never declarations (paper §VI).

This is a reference implementation of the *shape* of declaration. The real
declaration surface is an on-device, consented vault — see the paper's privacy
architecture (§VI, Fig. 6).
"""

from __future__ import annotations

from forty_two_true.intent_pair import DeclaredIntent


def declare(text: str, *, authored_at: str, unlinkable_token: str) -> DeclaredIntent:
    """Wrap a natural-language want as a consented, unlinkable declaration.

    Parameters
    ----------
    text:
        The declaration, in the declarant's own words.
    authored_at:
        ISO-8601 timestamp of authoring.
    unlinkable_token:
        A per-declaration token with no persistent identity. Generating such a
        token under a zero-knowledge protocol is the work of the network, not
        of this function — the argument makes the requirement explicit.
    """

    if not text.strip():
        raise ValueError("A declared intent cannot be empty.")
    return DeclaredIntent(
        text=text,
        consented=True,
        authored_at=authored_at,
        unlinkable_token=unlinkable_token,
    )
