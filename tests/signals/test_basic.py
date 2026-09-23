"""Signal tests."""

from datetime import datetime, timedelta, timezone

from product_intelligence.domain.observations import Observation
from product_intelligence.domain.products import Product
from product_intelligence.signals.basic import acceleration, level, velocity


def test_level_velocity_acceleration_with_irregular_dates() -> None:
    product = Product.named("reusable cleaning product")
    base = datetime(2025, 1, 1, tzinfo=timezone.utc)
    history = [Observation.create(product_id=product.product_id, source="fixture", metric="interest", value=value, unit="relative", geography="INTL", source_event_at=base + timedelta(days=days), observed_at=base + timedelta(days=days + 1), provenance={"id": str(value)}, confidence=1) for days, value in ((0, 2), (3, 5), (10, 11))]
    assert [point.value for point in level(history)] == [2, 5, 11]
    assert [point.value for point in velocity(history)] == [3, 6]
    assert [point.value for point in acceleration(history)] == [3]


def test_insufficient_history_returns_empty_derived_signals() -> None:
    product = Product.named("compact kitchen appliance")
    item = Observation.create(product_id=product.product_id, source="fixture", metric="interest", value=1, unit="relative", geography="INTL", source_event_at=None, observed_at=datetime(2025, 1, 1, tzinfo=timezone.utc), provenance={"id": "1"}, confidence=1)
    assert velocity([item]) == ()
    assert acceleration([item]) == ()
