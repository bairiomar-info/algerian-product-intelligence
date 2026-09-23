# Prediction methodology

**Status:** M0 — Research and architecture. Future research targets are not validated models.

## Candidate targets

`BREAKOUT_30D`, `BREAKOUT_60D`, `SUSTAINED_GROWTH`, `SATURATION_30D`, and `ALGERIA_TRANSFER` require explicit event definitions, product scope, geography, baseline, observation coverage, and censoring rules.

## Historical labeling

Freeze an as-of snapshot using only data available by `observed_at`. Construct labels from a future outcome window and never allow future source records, entity corrections, or derived fields into features. Preserve event and censoring timestamps.

## Evaluation

Use chronological train/validation/test periods and rolling or expanding walk-forward evaluation. Group related offers/product families where needed to avoid leakage. Freeze a final test period before decisions. Compare simple baselines: persistence, recent growth, seasonal rules, and source-only rules.

Report precision, recall, false-positive rate, confusion counts, PR-AUC where appropriate, calibration, detection rate, alerts per product/time window, and lead time from first qualifying alert to event. Segment results by source coverage, geography, product family, and lifecycle.

## Prospective standard

Prediction capability must be demonstrated through historical out-of-sample evaluation before being considered operational. After retrospective evidence, prospective shadow evaluation may test drift without influencing decisions. No predictive claim is made in M0.

## Leakage risks

Collection delay, source backfills, future entity-resolution decisions, duplicate offers across partitions, random row splits, target-derived thresholds, seasonality leakage, and holdout optimization must be controlled and documented.
