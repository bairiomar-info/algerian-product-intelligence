# Lifecycle methodology

**Status:** M0 — Research and architecture. Lifecycle states are hypotheses until tested against historical data.

## Provisional states

- **UNKNOWN:** insufficient, contradictory, stale, or unresolved evidence.
- **SEED:** identifiable product with sparse early evidence and no persistence established.
- **EMERGING:** repeated evidence and rising level without confirmed acceleration.
- **ACCELERATING:** velocity is increasing across defined windows with adequate coverage.
- **BREAKOUT:** retrospectively defined threshold event relative to a product/source baseline.
- **PEAK:** high level with weakening growth or a local maximum; not automatically saturated.
- **SATURATING:** competition/availability maturity and slowing opportunity evidence jointly observed.
- **DECLINING:** sustained deterioration after seasonality, events, and source loss are controlled.

## Transition evidence

Each transition must specify as-of date, baseline, windows, minimum history, source coverage, metric definitions, thresholds, seasonality/event annotations, entity confidence, and missingness. Evidence can be source-specific; international and Algerian lifecycle states are separate.

A transition is not valid merely because a vendor labels a product “trending.” Future outcomes cannot be used in a historical state at the decision time.

## Validation

Test state stability across products, languages, sources, and time. Compare against simple rules, inspect false transitions, and freeze thresholds before holdout evaluation. A product can move backward or remain UNKNOWN; lifecycle is not a mandatory linear path.
