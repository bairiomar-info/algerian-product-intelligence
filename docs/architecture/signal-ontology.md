# Signal ontology

**Status:** M0 — Research and architecture. These are independent measurable dimensions; no arbitrary weights or winner score are defined.

Every signal stores product/entity version, source observation IDs, geography, as-of timestamp, window, calculation version, missingness, and uncertainty.

## Demand

- **Level:** observed or estimated magnitude under a source-specific definition.
- **Velocity:** change in level over a stated interval.
- **Acceleration:** change in velocity across successive intervals.

Values are not comparable across sources without documented normalization. Relative search interest is not absolute demand.

## Persistence

- **Duration:** elapsed time with qualifying evidence.
- **Repeated growth:** number and sequence of positive periods.
- **Consistency:** agreement across windows after annotating seasonality, outages, and events.

## Cross-source confirmation

Record number of independent sources, source diversity, agreement/disagreement, coverage, and dependence. Ten records copied from one source are not ten independent confirmations.

## Competition

Track seller count, advertiser count, listing count, offer count, and each measure’s velocity. Preserve deduplication rules and market denominator. Counts are not market share.

## Saturation

Separate demand maturity, competition maturity, market penetration, availability density, and price pressure where measurable. Price compression requires comparable units, currency, time, and quality; it must not be inferred from headline prices.

## Earlyness

Measure lead time between the first qualifying alert and a retrospectively defined breakout or saturation event, plus distance from the historical level/competition pattern. “Early” is a measurable temporal relationship, not a marketing description.

## Algeria dimensions

Direct demand: explicit product/brand/model intent in Algeria. Adjacent demand: related product/solution intent. Underlying problem demand: evidence of the need/job independent of product naming. Also track local competition, local price evidence, local availability, delivery/payment feasibility, and context evidence.

## Confidence and uncertainty

Confidence is evidence quality, not probability of success. Record provenance completeness, source reliability, coverage, entity-match uncertainty, freshness, source independence, missingness, and contradictions. Calibrate any probabilistic interpretation later.

## Anti-patterns

Do not turn missing data into zero, sum incomparable provider scores, treat engagement as demand, treat ad duration as profitability, or collapse all dimensions into a single rank before validation.
