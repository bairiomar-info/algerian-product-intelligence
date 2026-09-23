# Development and research rules

## Scope and runtime

- Python version: `>=3.13,<3.14`.
- This repository is currently at **M0 — Research + Architecture**.
- This commit is the project foundation only. Do not implement collectors, the trend engine, ML, or speculative features without completed research and validation.
- Preserve the project objective: product-level intelligence for international momentum and plausible demand transfer to Algeria.

## Engineering and reproducibility

- Use tests for non-trivial behavior.
- Prefer deterministic, reproducible processing.
- Preserve raw observations and timestamps.
- Record provenance for every data observation.
- Never overwrite historical observations; append new observations instead.
- Do not silently substitute missing data.
- Every research conclusion must be reproducible from documented inputs, methods, and versions.

## Intelligence and methodology

- Product-level intelligence is mandatory; do not substitute broad category claims.
- Keep momentum, acceleration, persistence, saturation, Algeria-transfer, and feasibility signals separate.
- Do not create an arbitrary “winning product” score before its components are measurable and validated.
- Avoid look-ahead leakage in research and prediction.
- Do not optimize thresholds against holdout data.
- Make no prediction claims without proper out-of-sample validation.

## Data sources and access

- Keep source adapters independent from the intelligence layer.
- Abstract external providers behind source adapters.
- Prefer official free APIs, free public datasets, and permitted public data.
- Paid providers may be optional adapters when materially valuable, but do not make a paid provider a mandatory architectural dependency without explicit justification.
- Do not fabricate API availability, pricing, historical coverage, or access.
- Do not scrape or access data in violation of applicable source terms, restrictions, or access controls.

## Change discipline

Keep changes focused, reviewable, and documented. Update methodology and architecture documentation when decisions change. Do not commit credentials, sensitive data, or unvalidated research conclusions.
