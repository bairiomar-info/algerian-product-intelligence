# Competitive analysis

**M0 status:** research and architecture only. “Documented” means first-party documentation or an observable product description; “vendor claim” is not independent validation. Current access, price, history, and API details must be rechecked before use.

| System | Purpose and principal data | Product / history / trend approach | Competition, prediction, geography, access and cost | Limitation and architectural lesson |
|---|---|---|---|---|
| Exploding Topics | Vendor-described search, web, and mention/topic discovery | Usually topic/keyword clusters; trajectories and trend scores; exact persistence/acceleration undocumented | Saturation not established; forecasting validation not established; API, geography, pricing and limits **UNKNOWN — REQUIRES VERIFICATION** | Useful discovery and synonym grouping; do not treat opaque scores as product forecasts |
| Trend Hunter | Curated trends, community/editorial content, reports | Trend/theme/idea level, sometimes product examples; longitudinal depth and formulas proprietary | Forecasting and API are vendor-described or **UNKNOWN — REQUIRES VERIFICATION**; enterprise/custom cost **UNKNOWN — REQUIRES VERIFICATION** | Useful qualitative context; editorial curation is not measurable demand |
| Trendalytics | Retail, search, social and product/fashion intelligence | Product/attribute-oriented in selected verticals; historical/forecast features are vendor-described | Competition context possible; API, geography, history, price **UNKNOWN — REQUIRES VERIFICATION** | Learn to model attributes and retail context; do not generalize a proprietary vertical forecast |
| Sell The Trend | Product/store/ad research for ecommerce | Listing/product level through marketplace and store views; history **UNKNOWN — REQUIRES VERIFICATION** | Vendor indicators are not validated forecasting; API, geography and current price **UNKNOWN — REQUIRES VERIFICATION** | Product discovery lesson; dropshipping scores are not universal opportunity measures |
| Kalodata | Vendor-described social-commerce, store, product and ad intelligence | Product/store level claimed; collection, history and formulas **UNKNOWN — REQUIRES VERIFICATION** | API, geographic coverage, pricing, forecasting and competition definitions **UNKNOWN — REQUIRES VERIFICATION** | Optional enrichment only; retain provider uncertainty |
| Amazon Product Opportunity Explorer | Amazon-native search, purchase, niche and competition context | Product/niche level in Amazon Seller Central; history/export/API depth **UNKNOWN — REQUIRES VERIFICATION** | No public Opportunity Explorer API verified here; Amazon marketplace only; no validated forecast established | Strong marketplace-specific evidence; never equate Amazon behavior with Algeria or total demand |
| Helium 10 | Third-party Amazon product, keyword, listing and competitor estimates | Product/listing level; historical modules and estimates are plan-dependent | API documentation exists, but endpoint eligibility, limits and current pricing **UNKNOWN — REQUIRES VERIFICATION**; paid | Optional estimated context; never treat estimated sales as observed sales |
| Similarweb | Estimated web/app traffic, keywords, audiences and domains from proprietary sources | Domain/keyword/channel rather than physical SKU; time series where endpoint supports it | Official API and credit model documented; commercial pricing plan-dependent; forecasting not established; geography varies | Useful merchant/channel context; traffic is not transactions. See [docs](https://docs.similarweb.com/api-v5/api-reference/web-intelligence-api) |
| Meta Ad Library | Public ad/advertiser/creative transparency data | Creative/advertiser can expose products; first/last-seen and repetition support persistence proxies | API permissions, limits, retention and eligible use vary; public UI is not unrestricted API. [Library](https://www.facebook.com/ads/library/) | Useful advertising evidence; ad duration is not profitability or demand |
| TikTok Commercial Content API/Library | Commercial-content transparency in eligible programs/regions | Ad/creative/advertiser level where fields exist; coverage/history **UNKNOWN — REQUIRES VERIFICATION** | Application, geography, terms, limits and cost **UNKNOWN — REQUIRES VERIFICATION**; no forecast | Optional legal transparency signal; never infer global/Algerian coverage |
| Google Trends | Relative search interest for terms/topics by time/geography | Excellent candidate for level, velocity, acceleration, persistence and seasonality; not absolute volume | Official Trends API described as limited alpha; quota, auth, price and history **UNKNOWN — REQUIRES VERIFICATION**; no validated forecast | Transparent directional demand proxy; term identity and normalization are central. See [docs](https://developers.google.com/search/apis/trends) |

## Cross-system findings

**Research finding:** reviewed tools repeatedly combine search, social, advertising, marketplace, or editorial evidence, but their data definitions and proprietary scoring are rarely fully auditable. **Recommendation:** borrow evidence patterns, not scores. Keep demand, competition, saturation, lifecycle, earlyness, Algeria transfer, and feasibility independent.

**Independent demonstration:** no source reviewed establishes that a vendor’s ��winning,” “trend,” or “forecast” score predicts breakout or transfer out of sample. Such capability must be tested by us.

## False positives

Temporary virality, seasonality, news, influencer concentration, one-country anomalies, fake engagement, ad testing, product launches, and platform algorithm changes must be annotated and tested as contamination. Multi-week, multi-source evidence is a safeguard, not proof.

## Product entity lesson

Use source identifiers first, then multilingual normalization, attribute comparison, candidate blocking, semantic similarity, image/offer evidence, and human-reviewable relation labels. Preserve exact product, variant, family, adjacent, and unrelated distinctions.

## Source links

[Amazon SP-API](https://developer-docs.amazon.com/sp-api/), [eBay Developers](https://developer.ebay.com/develop), [YouTube Data API](https://developers.google.com/youtube/v3), [Meta Ad Library API](https://developers.facebook.com/docs/marketing-api/reference/ad-library), [TikTok Transparency Center](https://transparency.tiktok.com/), [Google Trends](https://developers.google.com/search/docs/monitor-debug/trends-start), and [product matching research](https://dbs.uni-leipzig.de/research/publications/intermediate-fusion-for-multimodal-product-matching).
