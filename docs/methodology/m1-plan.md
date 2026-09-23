# M1 plan

**Status:** M0 architecture freeze. M1 is intentionally narrow and does not build the whole platform.

1. Define canonical data models, entity relations, observation contracts, provenance, confidence, and missingness semantics.
2. Implement append-only observation storage with both `observed_at` and `source_event_at`.
3. Establish product concept, product family, canonical product, offer, and relation records.
4. Implement one or two verified, permitted source adapters only.
5. Ingest a small historical observation set or permitted fixture with reproducible retrieval metadata.
6. Calculate basic level, velocity, and acceleration; do not claim prediction.
7. Add data-quality, entity-linkage, provenance, timestamp, and leakage tests.
8. Produce the first historical product trajectories and contamination annotations.
9. Determine whether the collected data has sufficient coverage, history, cadence, and product resolution for the intended research.

Only after this evidence should additional sources, paid enrichment, lifecycle thresholds, or ML be considered. The M1 exit decision is about data sufficiency, not feature count.
