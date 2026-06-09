# Paper

**42-True: A Large Meaning Model for Declared Human Intent**
*Resolving what people want, in conditions where nothing is watching.*

Shawn Jensen — Profila GmbH, Switzerland — `shawn@profila.com`

📄 [**42-True_LMM_paper.pdf**](42-True_LMM_paper.pdf) (convenience copy)
🔗 **Version of record:** [doi:10.5281/zenodo.20616391](https://doi.org/10.5281/zenodo.20616391) (Zenodo)

The Zenodo deposit is the canonical, citable, timestamped record for reference
and copyright provenance. The PDF in this directory mirrors that deposit.

## Abstract

Contemporary artificial intelligence is trained, with rare exception, on
observational data: text and behaviour recorded under conditions where the
subject was, or assumed they were, watched. Nine decades of behavioural science
establish that observation distorts behaviour; it follows that models trained on
observational corpora converge toward an upper bound on fidelity to the
unobserved human. This paper proposes a complementary class of training
data — *declared intent paired with verified outcome* — gathered in an
environment architecturally incapable of identifying the declarant. We define
its atomic unit, the **intent pair**, and the model trained upon it, the **Large
Meaning Model (LMM)**. The contribution is fourfold: (i) we formalise the intent
pair and contrast it with existing training primitives; (ii) we describe the
model it yields and why its inductive bias differs from language and world
models; (iii) we ground the classification and privacy architecture in two prior
empirical studies; and (iv) we argue that the corpus must be *produced*, and
describe the network and stewardship required to produce it.

**Index terms** — declared intent, large meaning model, privacy-preserving
machine learning, zero-knowledge advertising, semantic retrieval, intent
classification, training-data provenance, zero-party data.

## Figures

| Fig. | Subject |
|---|---|
| 1 | The signal lifecycle (declare → classify → match → approve → store → retrain) |
| 2 | The intent pair `( Id, C, M, O )` — the atomic unit (repo cover image) |
| 3 | Three model paradigms: language model, world model, Large Meaning Model |
| 4 | The compounding loop |
| 5 | Three-tier classification (agents, community, experts) |
| 6 | The zero-knowledge boundary |

## Note on the data in this repository

The example records in [`../data/example_intent_pairs.jsonl`](../data/example_intent_pairs.jsonl)
are **synthetic illustrations** authored to demonstrate the schema. They are not
real declared data — by design, real declared-intent data does not exist yet and
must be produced (paper §VIII).
