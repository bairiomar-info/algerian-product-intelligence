"""Repository tests."""

from datetime import datetime, timezone
from uuid import uuid4

import pytest

from product_intelligence.domain.observations import Observation, RawObservation
from product_intelligence.domain.products import Product
from product_intelligence.storage.repository import InMemoryRepository


def test_repository_orders_history_and_rejects_conflicts() -> None:
    product = Product.named("portable mini printer")
    repo = InMemoryRepository()
    repo.add_product(product)
    first = Observation.create(product_id=product.product_id, source="x", metric="views", value=1, unit="count", geography="INTL", source_event_at=datetime(2025, 1, 1, tzinfo=timezone.utc), observed_at=datetime(2025, 1, 2, tzinfo=timezone.utc), provenance={"id": "1"}, confidence=1)
    second = Observation.create(product_id=product.product_id, source="x", metric="views", value=2, unit="count", geography="INTL", source_event_at=datetime(2025, 1, 3, tzinfo=timezone.utc), observed_at=datetime(2025, 1, 4, tzinfo=timezone.utc), provenance={"id": "2"}, confidence=1)
    repo.add_observation(second)
    repo.add_observation(first)
    assert [item.value for item in repo.history(product.product_id)] == [1, 2]
    with pytest.raises(ValueError):
        repo.add_observation(Observation(observation_id=first.observation_id, product_id=product.product_id, source="x", metric="views", value=99, unit="count", geography="INTL", source_event_at=first.source_event_at, observed_at=first.observed_at, provenance={"id": "changed"}, confidence=1))


def test_raw_observation_is_retrievable() -> None:
    repo = InMemoryRepository()
    raw = RawObservation(raw_id=uuid4(), source="fixture", payload={"views": 1}, observed_at=datetime(2025, 1, 1, tzinfo=timezone.utc))
    repo.add_raw(raw)
    assert repo.raw(raw.raw_id) == raw
