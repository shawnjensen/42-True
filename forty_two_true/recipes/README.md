# Recipes

These recipes describe the four-stage lifecycle that produces one **intent
pair** — the atomic unit of the Large Meaning Model corpus:

```text
declare (Id)  ->  classify (C)  ->  match (M)  ->  verify (O)
```

> **These are concept demonstrations, not a production pipeline.** Each module is
> a small, typed reference implementation that runs end-to-end on the example
> data. The real declaration vault, classification tiers, counterparty market,
> and attestation layer **do not exist yet and must be produced** (paper §VIII).
> The toy resolver in `classify.py` exists only to make the example runnable.

## Stages

- **[`declare.py`](./declare.py)** — wrap a natural-language want as a consented,
  unlinkable declaration. This is the only stage that touches the raw signal;
  from here on, counterparties see classifications, never declarations
  (paper §VI, Fig. 6).
- **[`classify.py`](./classify.py)** — map the declaration to a taxonomy node.
  The paper routes by confidence across three tiers — specialist **agents**, an
  opted-in **community** vote, and independent **experts** (paper §V, Fig. 5).
- **[`match.py`](./match.py)** — return a counterparty offer keyed on the
  classification. Only the classification crosses the zero-knowledge boundary.
- **[`verify.py`](./verify.py)** — record the realised outcome and assemble the
  immutable four-tuple. A `VERIFIED_RESOLUTION` must be backed by a `proof_ref`;
  the recipe refuses to fabricate one.

## End-to-end

```python
from forty_two_true.recipes import declare, classify, match, observe_outcome, assemble
from forty_two_true import OutcomeGrade

intent = declare(
    "there's a leak under the kitchen sink and I can't fix it myself",
    authored_at="2026-06-03T07:15:00Z",
    unlinkable_token="zk:9c01ff52",
)
classification = classify(intent.text)                 # -> home.repair, agent tier
offer = match(classification)                          # -> a vetted local plumber
outcome = observe_outcome(OutcomeGrade.VERIFIED_RESOLUTION, proof_ref="att:1aa7e9")
pair = assemble(intent, classification, offer, outcome)
```

## The compounding loop

Every completed cycle is stored, and each stored pair retrains both the
classifier and the model: signals yield intent pairs, which improve matching,
which earns the trust that yields more signals (the compounding loop,
paper §IV.C, Fig. 4). The asset compounds with participation rather than compute.
