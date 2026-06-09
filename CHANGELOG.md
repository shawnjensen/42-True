# Changelog

All notable changes to this project are documented here. This project adheres to
[Semantic Versioning](https://semver.org/).

## [0.0.1] — 2026-06-09

Initial public concept release.

### Added
- The **intent pair** primitive `( Id, C, M, O )` as frozen Pydantic models
  (`forty_two_true/intent_pair.py`).
- Shared schema: `ClassificationTier`, ordered `OutcomeGrade`, `TaxonomyNode`,
  and an illustrative taxonomy (`forty_two_true/schema.py`).
- Conceptual **recipes** for the four-stage lifecycle — declare, classify,
  match, verify (`forty_two_true/recipes/`).
- Synthetic, clearly-labelled example data (`data/example_intent_pairs.jsonl`).
- Test suite covering schema round-trips, immutability, outcome ordering, and
  proof-backed verification.
- The paper, *42-True: A Large Meaning Model for Declared Human Intent*
  (`paper/`), and project documentation.
