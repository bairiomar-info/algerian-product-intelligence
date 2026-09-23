# M0 Research Report

**Architecture version:** v0.1
**Status:** Frozen documentation baseline; no production implementation.

## 1. Executive summary

The North Star requires identifying concrete products early, separating demand growth from competition and saturation, and testing whether the underlying need plausibly transfers to Algeria. The research indicates that no reviewed product or trend platform provides a sufficiently transparent, provider-independent, validated answer. Existing systems are useful as discovery references, but their scores, coverage, and forecasts must not be treated as established predictive capability.

The recommended foundation is an immutable, provenance-first evidence system. It should combine multiple source adapters, preserve raw observations and both source-event and collection times, resolve listings/ads/search terms into auditable product entities, and compute independent signals before any future prediction.

**Fact:** official documentation exists for several APIs and platforms linked below. **Vendor claim:** many commercial tools advertise trend discovery or forecasting. **Finding:** public evidence is generally insufficient to establish their forecasts as out-of-sample validated. **Recommendation:** begin with a small, legally accessible, reproducible source set and measure data sufficiency before adding providers.

## 2. North Star

Identify specific products that are beginning to gain momentum internationally, before they become saturated, and determine whether the underlying consumer demand can plausibly transfer to Algeria.

The unit of intelligence is a concrete product or product concept, not a generic category.

## 3. Problem definition

The system must distinguish a rising product from a temporary spike, quantify demand and competition trajectories separately, estimate lifecycle evidence, preserve historical state, and report Algeria-specific evidence without inferring local demand from international popularity. “Opportunity” is a time-bounded evidence hypothesis, not a winner label.

## 4. Competitive landscape

Exploding Topics and Trend Hunter emphasize topic/trend discovery and curation. Trendalytics emphasizes retail, search, social, and product attributes in selected verticals. Sell The Trend, Kalodata, and Minea emphasize product, store, or advertising intelligence. Amazon Product Opportunity Explorer provides Amazon-native search, purchase, and competition context. Helium 10 provides third-party Amazon estimates. Similarweb provides estimated digital traffic and keyword context. Meta Ad Library and TikTok commercial-content resources provide advertising/transparency evidence. Google Trends provides normalized relative search interest.

**Finding:** these systems demonstrate useful evidence patterns—trajectory views, product/creative context, persistence, and cross-source discovery—but proprietary scores and “prediction” claims are not independently established here. Details and links are in `competitive-analysis.md`.

## 5. Data-source landscape

The strongest initial candidates are permitted Google Trends observations, Meta Ad Library observations where access and terms permit, YouTube metadata, and carefully validated Algerian listing/search evidence. Reddit, TikTok, marketplaces, supplier ecosystems, and paid services are potential enrichment. The matrix records geography, history, access, uncertainty, and fallback for each source.

## 6. Important API/access limitations

A public website does not imply a public API. API status, quotas, authentication, historical retention, geography, pricing, export rights, and terms are source- and plan-specific. Unknowns remain explicitly marked in the matrix. No scraper or unofficial client is assumed permissible. Google Trends API access, TikTok commercial-content access, Meta API permissions, marketplace APIs, and Algerian platform access require verification at implementation time.

## 7. Core vs optional data sources

Core candidates are selected for repeatability and explainability, not popularity: one search source, one advertising source, one content source, and permitted local evidence. Paid providers—including Similarweb, Helium 10, Kalodata, and Exploding Topics—are optional adapters. No provider is mandatory; the system must degrade explicitly when a source is absent.

## 8. Product/entity-resolution problem

A listing, advertisement, search term, brand item, variant, bundle, and underlying problem are different entities. The resolver must retain raw entities and auditable hypotheses distinguishing exact product, variant, family, adjacent product, and unrelated item. It must support multilingual names and time-versioned decisions.

## 9. Signal architecture

Independent dimensions are: demand level, velocity, acceleration, persistence, cross-source confirmation, seller/advertiser competition, competition velocity, saturation, earlyness, feasibility, Algeria direct/adjacent/underlying demand, local competition, price, availability, and evidence confidence. No arbitrary weights or winner score are defined in M0.

## 10. Lifecycle architecture

A provisional vocabulary—UNKNOWN, SEED, EMERGING, ACCELERATING, BREAKOUT, PEAK, SATURATING, DECLINING—will be tested against historical trajectories. States require documented windows, baselines, seasonality controls, source coverage, and transition evidence. They are hypotheses until validated.

## 11. Saturation concept

Saturation is not high demand. It is a market- and denominator-specific combination of mature demand, competition/availability growth, penetration, and possibly price pressure. Demand trajectory and competition trajectory must remain separate so a growing but lightly competed product can be distinguished from a popular, crowded one.

## 12. Opportunity-window concept

A potential opportunity window exists when demand is growing or accelerating while competition and saturation remain comparatively immature, subject to feasibility and uncertainty. The window is time-dependent and must be evaluated retrospectively using lead time to breakout or saturation. It is not a composite score in M0.

## 13. Algeria-transfer concept

Transfer evidence is divided into direct demand (explicit product intent), adjacent demand (related solutions), underlying demand (the problem/job), local competition, local price, availability, delivery, payment, and contextual evidence. International popularity is only a prior/context signal; it does not establish Algerian demand.

## 14. Prediction roadmap

Future targets may include BREAKOUT_30D, BREAKOUT_60D, SUSTAINED_GROWTH, SATURATION_30D, and ALGERIA_TRANSFER. Labels require frozen as-of snapshots and future-only outcome windows. Begin with interpretable baselines and walk-forward experiments before any complex model.

## 15. Validation philosophy

All conclusions must be reproducible. Features use only information available at observation time; source-event time and collection time are both retained. Use chronological train/validation/test periods, walk-forward evaluation, product-family leakage controls, precision/recall, false-positive rate, calibration, and lead time. Prediction is not operational until historical out-of-sample evidence demonstrates it.

## 16. Architecture v0.1

```text
Discovery Sources → Source Adapters → Raw Observations → Entity Resolution
→ Product Concept → Canonical Product → Historical Time Series → Signal Engine
→ Lifecycle Engine → Saturation Engine → Opportunity Window
→ Algeria Transfer Engine → Evidence Report → Prediction / Validation
```

Adapters own source mechanics; core intelligence owns normalized evidence and derived signals. Storage technology remains deliberately deferred.

Canonical observation:

```text
Observation {
  product_id, source, metric, value, geography,
  observed_at, source_event_at, provenance, confidence
}
```

`source_event_at` is when the source event occurred; `observed_at` is when our system learned or recorded it. For example, a video published September 1 and first detected September 4 must retain both dates. Historical backtests must use the latter as the information boundary to prevent look-ahead.

## 17. Risks

Source policy changes, inaccessible history, platform bias, entity-matching errors, duplicate listings, seasonality, news and influencer spikes, paid-ad testing, source outages, weak Algeria coverage, price/landed-cost uncertainty, and opaque vendor estimates can all produce false conclusions. Mitigate with provenance, explicit missingness, multi-source confirmation, contamination review, and validation.

## 18. Open questions

Which minimum sources provide sufficient repeatable history? What product identity and family boundaries are useful? Which Algeria queries and local observations are measurable? What labels have adequate event rates? How should source dependence, seasonality, censorship, and right-censoring be handled? What permissions and retention are available for each source?

## 19. M1 implementation plan

1. Define canonical data models and observation contracts.
2. Implement append-only observation storage with provenance and timestamps.
3. Establish product-entity and relation records.
4. Implement one or two verified adapters only.
5. Ingest a small historical fixture or permitted history.
6. Calculate level, velocity, and acceleration without claiming prediction.
7. Add data-quality and temporal-leakage tests.
8. Produce first product trajectories and contamination annotations.
9. Decide whether evidence is sufficient before adding sources or ML.

## Sources

[Google Trends](https://developers.google.com/search/docs/monitor-debug/trends-start), [Google Trends API](https://developers.google.com/search/apis/trends), [YouTube Data API](https://developers.google.com/youtube/v3), [Amazon SP-API](https://developer-docs.amazon.com/sp-api/), [Similarweb API](https://docs.similarweb.com/api-v5/api-reference/web-intelligence-api), [Meta Ad Library](https://www.facebook.com/ads/library/), [Meta API reference](https://developers.facebook.com/docs/marketing-api/reference/ad-library), [eBay Developers](https://developer.ebay.com/develop), [ONS Algeria](https://www.ons.dz/), [product matching research](https://dbs.uni-leipzig.de/research/publications/intermediate-fusion-for-multimodal-product-matching), and [temporal evaluation research](https://arxiv.org/html/2507.16289).
