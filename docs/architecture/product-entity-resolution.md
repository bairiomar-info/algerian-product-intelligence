# Product entity resolution

**Status:** M0 — Research and architecture. No resolver is implemented.

## Problem

Different sources may describe the same underlying product using different names, languages, spelling, brands, variants, bundles, seller descriptions, or marketplace identifiers. A listing, ad, video, query, and supplier record must not be merged merely because they share a category word.

## Required relations

The future model must distinguish:

- **exact same product:** materially identical item/specification;
- **product variant:** same design/product identity with meaningful size, color, pack, region, or specification difference;
- **same product family:** related products sharing a design/use lineage but not exact identity;
- **adjacent product:** related solution or substitute with a distinct identity;
- **unrelated product:** insufficient or contradictory evidence.

Brand, generic product, offer, bundle, and underlying problem should remain separately addressable.

## Future pipeline

```text
Raw entity
    ↓
Normalization
    ↓
Candidate matching
    ↓
Semantic similarity
    ↓
Attribute comparison
    ↓
Human/reviewable evidence
    ↓
Canonical product entity
```

### Raw entity and normalization

Retain the source record unchanged. Normalize titles, brands, model numbers, dimensions, materials, pack size, language, transliterations, currency, images, URLs, seller, and marketplace into derived fields while retaining originals. Translation is evidence, not proof of identity.

### Candidate matching

Use deterministic IDs and URLs first. Block candidates by normalized tokens, language, brand/model, attributes, category/use, and image/perceptual fingerprints. Do not compare every record to every record.

### Similarity and attributes

Use multilingual text similarity only as candidate evidence. Compare structured attributes, images, specifications, bundle contents, and offer context. Conflicts must lower confidence or prevent a merge. Research on multimodal matching supports combining text and visual evidence; it does not remove the need for review ([Leipzig research](https://dbs.uni-leipzig.de/research/publications/intermediate-fusion-for-multimodal-product-matching), [entity-resolution embeddings](https://arxiv.org/abs/2304.12329)).

### Human/reviewable evidence

Store pairwise evidence, relation, reviewer/decision source, model/parser version, timestamp, and unresolved alternatives. High-impact merges require review or a documented deterministic rule. A later correction creates a new version; it must not rewrite earlier observations.

## Canonical output

A canonical product has a stable internal ID, versioned aliases, relation graph, product/family scope, evidence links, and uncertainty. It links to offers/listings, ads, queries, and problem concepts. Every signal must be able to trace through this graph to source observations.

## Evaluation

Create adjudicated match/non-match/variant/family datasets before optimizing thresholds. Measure precision and recall by language, source, category, brand presence, and bundle/variant class. Do not use future labels or later catalog knowledge in historical snapshots.
