"""Normalization tests."""

from datetime import datetime, timezone
from uuid import uuid4

from product_intelligence.domain.observations import RawObservation
from product_intelligence.normalization.observations import normalize_payload


def test_normalization_is_deterministic() -> None:
    product_id = uuid4()
    raw = RawObservation(raw_id=uuid4(), source="fixture", payload={"views": 4}, observed_at=datetime(2025, 1, 2, tzinfo=timezone.utc), provenance={"record": "a"})
    first = normalize_payload(raw, product_id=product_id, metric_key="views", unit="count", geography="DZ")
    second = normalize_payload(raw, product_id=product_id, metric_key="views", unit="count", geography="DZ")
    assert first == second


def test_missing_metric_fails_explicitly() -> None:
    raw = RawObservation(raw_id=uuid4(), source="fixture", payload={}, observed_at=datetime(2025, 1, 2, tzinfo=timezone.utc))
    try:
        normalize_payload(raw, product_id=uuid4(), metric_key="views", unit="count", geography="DZ")
    except ValueError as error:
        assert "missing metric" in str(error)
    else:
        raise AssertionError("missing metrics must not become zero")
