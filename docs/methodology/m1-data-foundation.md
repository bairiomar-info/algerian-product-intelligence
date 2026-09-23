# M1 data foundation

**Status:** M1 foundation implemented with a deterministic fixture adapter. No live API credentials were available in this repository context, so no live source observations are claimed.

## Implemented architecture

`SourceAdapter → RawObservation → normalization → Product → append-only repository → historical signals`

The domain models are immutable dataclasses. The in-memory repository is intentionally small and replaceable; it preserves raw and normalized records separately and rejects conflicting duplicate identities.

## Sources and access

The source boundary is provider-independent. `FixtureAdapter` demonstrates reproducible source ingestion without fabricating external data. A YouTube Data API adapter is not claimed or implemented because credentials and a live access test were unavailable. YouTube’s official API documentation is at https://developers.google.com/youtube/v3. Ouedkniss automated access was not implemented: a public API and permitted automated-collection mechanism were not verified. No Ouedkniss data is included.

## Schema

Normalized observations contain `observation_id`, `product_id`, `source`, `metric`, `value`, `unit`, `geography`, `source_event_at`, `observed_at`, `provenance`, and `confidence`. Raw observations retain a source payload, source, raw ID, timestamps, and provenance. Products contain a stable ID, canonical name, optional family/category/attributes, creation time, and provenance.

## Normalization and timestamps

Normalization is deterministic and explicit. Missing metrics raise an error; they never become zero. `source_event_at` is when a source says an event happened, while `observed_at` is when the system collected or learned it. A delayed observation therefore cannot leak future information into a historical calculation.

Signals currently provide only level, first differences (velocity), and second differences (acceleration), ordered by source event time when available and observation time otherwise. Irregular spacing is preserved; these initial differences are not rate-per-day calculations.

## Data-quality policy

Timezone-aware timestamps, required identifiers, source/metric/geography fields, confidence bounds, finite values, immutable records, and conflicting duplicate detection are validated. Missing observations remain absent. Source outages and delayed records require explicit source metadata; they are not converted to zero. Full schema and geographic-code validation remain M1 follow-up work.

## Current limitations and next questions

There are no live observations, no external credentials, no persistent database, no advanced entity resolution, no source-specific geographic validation, and no prediction. M1 acceptance is therefore **not complete**: the foundation is testable, but the real-source and real-historical-dataset criteria still require a permitted credentialed ingestion run. Next, validate YouTube API access or another officially permitted source, then add one verified Algerian source or document a permitted alternative before claiming M1 completion.
