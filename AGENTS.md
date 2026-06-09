# Guidance for Claude Code / coding agents

## What this repository is

42-True is the **first public concept** of the Large Meaning Model (LMM)
described in [`paper/42-True_LMM_paper.pdf`](paper/42-True_LMM_paper.pdf). It is a
**schema and concept seed**, not a training pipeline. The corpus it is defined
against does not exist yet and, by design, cannot be scraped — it must be
*produced*. Keep that framing intact in any docs or code you write.

## Layout

- `forty_two_true/intent_pair.py` — the primitive: the frozen four-tuple
  `( Id, C, M, O )`.
- `forty_two_true/schema.py` — `ClassificationTier`, ordered `OutcomeGrade`,
  `TaxonomyNode`.
- `forty_two_true/recipes/` — conceptual `declare → classify → match → verify`
  stages. These are reference demonstrations, not real services.
- `data/example_intent_pairs.jsonl` — synthetic, clearly-labelled examples.
- `tests/` — schema invariants and example-data validation.

## Invariants — do not break

1. **Immutability.** All Pydantic models are `frozen=True`. Construct new records;
   never mutate in place.
2. **No real declared data.** Any example records must be synthetic and labelled
   as such. Genuine declarations are gathered only under the consented,
   unobservable protocol — never committed here.
3. **Outcomes are earned, not asserted.** A `VERIFIED_RESOLUTION` outcome must
   carry a `proof_ref`; `observe_outcome` enforces this.
4. **Honesty about status.** Don't describe the recipes as a working production
   system. They run on the example data; the network described in the paper is
   future work.

## Working on it

```bash
pip install -e ".[dev]"
pytest
ruff check .
```
