# Algerian Product Intelligence

## North Star

> Identify specific products that are beginning to gain momentum internationally, before they become saturated, and determine whether the underlying consumer demand can plausibly transfer to Algeria.

The system focuses on concrete products—not generic categories—and will eventually combine accumulated evidence from multiple sources to assess momentum, lifecycle stage, saturation, competition, and Algerian transfer potential.

## What the system is—and is not

This is a research-first product-intelligence system for identifying early international product momentum and evaluating whether the underlying demand may transfer to Algeria.

It is not currently:

- a generic category-ranking or trend-list system;
- a production scraper or collector platform;
- an ML system or predictive product;
- a source of fabricated market, API, pricing, or coverage claims; or
- a replacement for validated market research and local commercial judgment.

## Core objectives

1. Detect early international product momentum.
2. Measure velocity, acceleration, and persistence.
3. Distinguish emerging trends from temporary viral spikes.
4. Estimate product lifecycle stage.
5. Detect saturation and competition growth.
6. Assess whether underlying demand can plausibly transfer to Algeria.
7. Measure direct, adjacent, and underlying/problem-level Algerian demand.
8. Track Algerian competition and market availability.
9. Preserve historical observations for future training and validation.
10. Eventually predict breakout, saturation, and Algerian-transfer outcomes using historical data and proper out-of-sample validation.

## High-level architecture

```text
External sources
  → source adapters
  → normalized observations
  → product entity resolution
  → historical time series
  → signal engine
  → lifecycle engine
  → saturation engine
  → early-product candidates
  → Algeria transfer engine
  → opportunity evidence
  → historical validation/prediction
```

Collectors, ML, and intelligence engines are intentionally not implemented in this foundation commit. External providers will be isolated behind replaceable source adapters, keeping source access independent from the intelligence layer.

## Data-access philosophy

Use the best realistically accessible data. Prefer official free APIs, free public datasets, and permitted public data. Paid APIs and data providers are allowed when they provide material value or save substantial engineering effort, but must be replaceable adapters where practical. No single commercial provider should become a critical dependency.

API availability, pricing, historical coverage, and access must be validated rather than assumed. Data access must respect applicable source terms and restrictions.

## Research-first principles

- Preserve raw observations and timestamps.
- Never overwrite historical observations.
- Retain source provenance for every observation.
- Keep product-level intelligence separate from broad category claims.
- Separate momentum, acceleration, persistence, saturation, Algeria-transfer, and feasibility signals.
- Do not create an arbitrary “winning product” score before its components are measurable and validated.
- Do not make predictive claims without out-of-sample validation.
- Prevent look-ahead leakage and keep research reproducible.

## Development status

**M0 — Research + Architecture.** This repository is the clean foundation for deep competitive research, data-source validation, and subsequent architecture work. No collectors, trend engine, ML, or production pipeline are implemented yet.

## Repository structure

```text
AGENTS.md                 Development and research rules
pyproject.toml            Minimal Python 3.13 project configuration
docs/                     Research and architecture placeholders
  research/
  architecture/
  methodology/
src/product_intelligence/  Application package foundation
tests/                    Test package foundation
```

## Validation philosophy

Any future signal or prediction must use measurable, documented components and reproducible inputs. Evaluation must preserve temporal ordering, avoid look-ahead leakage, and use proper out-of-sample validation. Thresholds must not be optimized against holdout data. Missing data must not be silently substituted.
