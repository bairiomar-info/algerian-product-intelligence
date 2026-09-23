# System design

**Architecture version:** v0.1. Documentation only; no collectors, database, API, dashboard, ML, or production intelligence logic.

## Provider-agnostic flow

```text
Discovery Sources
        ↓
Source Adapters
        ↓
Raw Observations
        ↓
Entity Resolution
        ↓
Product Concept
        ↓
Canonical Product
        ↓
Historical Time Series
        ↓
Signal Engine
        ↓
Lifecycle Engine
        ↓
Saturation Engine
        ↓
Opportunity Window
        ↓
Algeria Transfer Engine
        ↓
Evidence Report
        ↓
Prediction / Validation
```

## Entity vocabulary

- **Raw entity:** a source-native listing, ad, video, query, seller, or other record.
- **Product concept:** an evidence-backed representation of a thing or solution, before identity is fully resolved.
- **Product family:** related products sharing a meaningful design/use relationship but not necessarily interchangeable.
- **Canonical product:** a versioned, auditable identity for the specific product being analyzed.
- **Offer/listing:** a seller- and marketplace-specific commercial instance linked to a canonical product when justified.

A product concept must not be silently promoted to a canonical product. Relations are exact, variant, family, adjacent, or unrelated.

## Source adapters

Adapters isolate credentials, pagination, provider schemas, rate handling, terms metadata, and raw payload storage. Core intelligence imports only the common observation contract, never a provider SDK. Paid sources are optional adapters and can be removed without redesigning the core.

## Formal observation model

```text
Observation
├── product_id
├── source
├── metric
├── value
├── geography
├── observed_at
├── source_event_at
├── provenance
└── confidence
```

`source_event_at` records when the source says the event happened. `observed_at` records when our system collected or became aware of it. A video published on September 1 and detected on September 4 has `source_event_at=September 1` and `observed_at=September 4`. Backtests must not use information before `observed_at`, even if the event date is earlier. Both may be nullable with explicit missingness; neither may be inferred silently.

Provenance includes source identifier, source record/URL, retrieval method, raw payload reference or checksum, source terms/version, parser version, and retrieval timestamp. Confidence records evidence quality, not success probability.

## Immutable evidence and reproducibility

Raw observations are append-only. Corrections create new records or versioned interpretations; historical observations are never overwritten. Derived signals include input observation IDs, as-of time, window, formula/version, and generation time. Re-running the same inputs and version must reproduce the result.

## Core engines

- **Entity resolution:** auditable matching and relation hypotheses.
- **Time series:** source-specific measures with explicit units, windows, gaps, and seasonality annotations.
- **Signal engine:** independent demand, persistence, cross-source, competition, saturation, earlyness, feasibility, and Algeria dimensions.
- **Lifecycle:** evidence-based provisional state transitions.
- **Saturation:** demand maturity and competition/penetration evidence kept separate.
- **Opportunity window:** compares demand and competition trajectories without a winner score.
- **Algeria transfer:** direct, adjacent, underlying, local competition, price, availability, and context evidence.
- **Prediction/validation:** isolated, temporal, retrospective experiments only.

## Evidence report

Reports must trace every conclusion to raw observations, entity relations, metric definitions, timestamps, source coverage, missing data, contradictions, and uncertainty. International popularity never proves Algerian demand.

## Operational constraints

Respect source terms, access restrictions, robots policies, privacy rules, and licensing. Use fixtures for tests. Do not silently substitute missing data with zero. Storage technology and deployment are M1 decisions, not M0 commitments.

## Related documents

See `product-entity-resolution.md`, `signal-ontology.md`, `lifecycle.md`, `opportunity-window.md`, `algeria-transfer.md`, `prediction.md`, and `trend-contamination.md`.
