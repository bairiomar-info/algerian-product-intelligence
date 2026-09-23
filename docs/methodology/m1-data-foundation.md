# M1 data foundation

**Status: NOT GREEN — BLOCKED BY REAL-DATA ACCESS**

The M1 implementation foundation exists and is deterministic, but the acceptance criteria require a real authorized/permitted source ingestion. No live API credential or authorized source response was available in the repository execution context, so this commit does not claim live observations or downgrade the requirement to fixtures.

## Implemented architecture

`SourceAdapter → RawObservation → normalization → Product → append-only repository → historical signals`

The domain models are immutable dataclasses. The in-memory repository is intentionally small and replaceable; it keeps raw and normalized records separate and rejects conflicting duplicate identities. `FixtureAdapter` is available for deterministic tests only and is never counted as real data.

## YouTube authorization and access status

**Status: NOT AUTHORIZED IN THIS ENVIRONMENT.** No API key, OAuth client, access token, or live YouTube response was available or used.

For read-only public YouTube Data API v3 metadata, the official setup path is:

1. Create or select a Google Cloud project.
2. Enable YouTube Data API v3 for that project.
3. Create an API key in Google Cloud credentials.
4. Restrict the key appropriately and keep it outside the repository.
5. Use the documented API endpoints and quota model.
6. Comply with the [YouTube Data API documentation](https://developers.google.com/youtube/v3), [getting-started guidance](https://developers.google.com/youtube/v3/getting-started), and [API Services Terms](https://developers.google.com/youtube/terms/api-services-terms-of-service).

An API key is the credential required for public read-only requests; OAuth 2.0 is required for private user data or operations on behalf of a user. The exact current quota allocation and endpoint costs must be read from Google’s current documentation/project console at activation time; they are not hard-coded here. Credentials must be supplied through the runtime environment or secret manager, never committed.

The generic `SourceAdapter` boundary is ready for a future YouTube adapter. No fabricated YouTube result, current snapshot, or historical series is included.

## Algerian source status

**Ouedkniss: BLOCKED pending permission verification.** No official public API or documented permission for automated collection was verified in the research performed. Therefore no scraper or automated Ouedkniss access was implemented. Status: **UNKNOWN — REQUIRES VERIFICATION**.

The next permitted option is an explicitly authorized Ouedkniss integration, a documented public dataset, a partner export, or another Algerian ecommerce/public source whose automated-access terms can be verified. Until then, no Algerian observations are claimed.

## Schema and raw preservation

Normalized observations contain `observation_id`, `product_id`, `source`, `metric`, `value`, `unit`, `geography`, `source_event_at`, `observed_at`, `provenance`, and `confidence`. Raw observations retain a source payload, raw ID, source, timestamps, and provenance. The raw payload is kept separate so normalization can be audited and replayed.

`source_event_at` records when the source says an event happened. `observed_at` records when our system collected or became aware of it. For example, a video published September 1 and discovered September 4 must preserve September 1 and September 4 separately. A historical calculation must be bounded by the information available at `observed_at`; a later discovery cannot be backdated into knowledge that did not exist earlier.

## Normalization and signals

Normalization is deterministic and explicit. Missing metrics raise an error; they never become zero. Timezone-aware timestamps are normalized to UTC. Signals currently provide only level, first differences (velocity), and second differences (acceleration). Irregular spacing is preserved; these first M1 differences are not rate-per-day calculations. No trend, opportunity, or predictive score exists.

## Leakage validation

A regression test supplies observations on January 1, 8, 15, and 22. The series through January 15 is calculated from only the first three observations. The January 22 value cannot change the January 15 velocity or acceleration. This test validates the caller’s as-of boundary and preserves the event/observation timestamp distinction. A future production query must return an as-of-bounded history before invoking signal calculations.

## Final validation record

- **Source actually validated:** None; fixture adapter only.
- **Authorization/access status:** YouTube credentials unavailable; Ouedkniss automated access not verified.
- **Real observations:** 0.
- **Real products:** 0.
- **Historical period:** No real period; deterministic test dates only.
- **Raw-data preservation:** Implemented and tested for fixture/raw records.
- **Normalization:** Implemented and tested deterministically.
- **Level/velocity/acceleration:** Implemented and tested on deterministic fixtures.
- **Leakage test:** Passed by the regression test when the suite is executed; execution status must be reported by the environment running pytest.
- **Algerian source:** No real source validated; Ouedkniss remains blocked pending official permission/API verification.
- **Remaining blocker:** Authorized real-source credentials and a permitted Algerian source/access mechanism.

M1 remains **NOT GREEN — BLOCKED BY REAL-DATA ACCESS** until a small live authorized ingestion is performed and its raw, normalized, chronological, and signal outputs are inspected.
