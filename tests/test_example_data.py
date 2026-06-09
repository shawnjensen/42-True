"""The shipped example data must parse cleanly into intent pairs."""

from __future__ import annotations

import json
from pathlib import Path

from forty_two_true import IntentPair

DATA = Path(__file__).resolve().parent.parent / "data" / "example_intent_pairs.jsonl"


def test_example_jsonl_parses_into_intent_pairs() -> None:
    lines = [line for line in DATA.read_text().splitlines() if line.strip()]
    assert lines, "example data file is empty"

    pairs = [IntentPair.model_validate(json.loads(line)) for line in lines]

    assert len(pairs) == len(lines)
    # Every shipped example is explicitly marked synthetic.
    assert all("ynthetic" in p.corpus_note for p in pairs)
