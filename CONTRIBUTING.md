# Contributing

42-True is offered in the spirit of open science. At this stage the repository
is a **concept** — a schema and a set of recipes for a corpus that does not yet
exist — so the most valuable contributions are conceptual and structural.

## What's welcome

- **Critique of the schema.** Does the intent pair `( Id, C, M, O )` capture the
  right structure? What's missing, what's over-specified?
- **Classification & taxonomy.** Proposals for the machine-addressable schema and
  the three-tier resolution architecture (paper §V).
- **Privacy architecture.** Scrutiny of the zero-knowledge boundary and the
  unlinkability guarantees (paper §VI).
- **Production network.** Ideas on how the corpus could actually be *produced* —
  declaration surface, market design, outcome attestation (paper §VIII).
- **Stewardship.** Models for holding the result as a commons (paper §VII).

## Ground rules for data

This repository must never contain **real** declared-intent data. Any example
records committed here must be **synthetic** and **clearly labelled** as such (see
[`data/example_intent_pairs.jsonl`](data/example_intent_pairs.jsonl)). The whole
premise is that genuine declarations are gathered only under a consented,
unobservable protocol — not pasted into a public repo.

## Development

```bash
pip install -e ".[dev]"
pytest
ruff check .
```

Models are **frozen** (immutable) by design: prefer constructing new records over
mutating existing ones, and keep that invariant in any new code.

## Discussion

Open an issue, or reach the author at `shawn@profila.com`.
