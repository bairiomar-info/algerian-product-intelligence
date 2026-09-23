"""Domain-model tests."""

from datetime import datetime, timezone
from uuid import uuid4

import pytest

from product_intelligence.domain.observations import Observation
from product_intelligence.domain.products import Product


def test_product_identity_is_stable() -> None:
    product_id = uuid4()
    product = Product(product_id=product_id, canonical_name="wearable neck fan")
    assert product.product_id == product_id


def test_product_requires_name() -> None:
    with pytest.raises(ValueError):
        Product(canonical_name="")


def test_observation_keeps_event_and_observation_time_separate() -> None:
    product_id = uuid4()
    event = datetime(2025, 9, 1, tzinfo=timezone.utc)
    observed = datetime(2025, 9, 4, tzinfo=timezone.utc)
    item = Observation.create(product_id=product_id, source="fixture", metric="views", value=2, unit="count", geography="DZ", source_event_at=event, observed_at=observed, provenance={"id": "x"}, confidence=1)
    assert item.source_event_at != item.observed_at


def test_invalid_confidence_fails() -> None:
    with pytest.raises(ValueError):
        Observation.create(product_id=uuid4(), source="x", metric="m", value=1, unit="count", geography="DZ", source_event_at=None, observed_at=datetime.now(timezone.utc), provenance={"id": "x"}, confidence=2)
