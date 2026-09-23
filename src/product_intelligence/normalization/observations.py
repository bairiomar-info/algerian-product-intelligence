"""Normalize source records into canonical observations."""

from datetime import datetime
from uuid import UUID

from product_intelligence.domain.observations import Observation, RawObservation


def normalize(raw: RawObservation, *, product_id: UUID, metric: str, value: float, unit: str, geography: str, confidence: float = 1.0) -> Observation:
    if not metric.strip() or not geography.strip():
        raise ValueError("metric and geography are required")
    provenance = dict(raw.provenance)
    provenance.update({"source": raw.source, "raw_id": str(raw.raw_id)})
    return Observation.create(
        product_id=product_id,
        source=raw.source,
        metric=metric,
        value=float(value),
        unit=unit,
        geography=geography,
        source_event_at=raw.source_event_at,
        observed_at=raw.observed_at,
        provenance=provenance,
        confidence=confidence,
    )


def normalize_payload(raw: RawObservation, *, product_id: UUID, metric_key: str, unit: str, geography: str, confidence: float = 1.0) -> Observation:
    if metric_key not in raw.payload:
        raise ValueError(f"missing metric payload: {metric_key}")
    return normalize(raw, product_id=product_id, metric=metric_key, value=float(raw.payload[metric_key]), unit=unit, geography=geography, confidence=confidence)
