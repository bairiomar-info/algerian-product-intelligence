# Trend contamination methodology

**Status:** M0 — Research and architecture. No contamination classifier is implemented.

## Potential causes

Trend signals may be contaminated by seasonality, holidays, news events, celebrity or influencer effects, one-platform virality, commercial advertising campaigns, product launches, temporary events, platform algorithm changes, source outages, duplicate listings, or coordinated/fake engagement.

## Diagnostic evidence

Annotate event calendars, geographic concentration, source concentration, creator/advertiser concentration, paid-ad timing, query language, product availability, engagement-to-conversion proxies where lawful, and behavior after the spike. Compare the product with seasonal and category baselines.

## Temporary spike vs persistent adoption

A temporary spike may be short, concentrated, event-aligned, or disappear when a single platform changes. Multi-source persistent adoption should show repeated evidence over time, independent source confirmation, expanding or stable geographic/product coverage, and a trajectory that survives the triggering event. These are hypotheses, not guarantees.

## Research controls

Keep contamination annotations separate from demand signals. Test alert rules with and without contaminated periods, report false-positive reasons, and never delete contaminated observations: they are part of the historical record.
