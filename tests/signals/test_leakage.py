"""Regression tests for temporal leakage boundaries."""

from datetime import datetime, timedelta, timezone

from product_intelligence.domain.observations import Observation
from product_intelligence.domain.products import Product
from product_intelligence.signals.basic import acceleration, velocity


def test_as_of_series_does_not_use_future_observations() -> None:
    product = Product.named("wearable neck fan")
    base = datetime(2025, 1, 1, tzinfo=timezone.utc)
    history = [
        Observation.create(
            product_id=product.product_id,
            source="authorized-fixture",
            metric="views",
            value=value,
            unit="count",
            geography="INTL",
            source_event_at=base + timedelta(days=offset),
            observed_at=base + timedelta(days=offset + 1),
            provenance={"record": str(offset)},
            confidence=1.0,
        )
        for offset, value in ((0, 10), (7, 15), (14, 25), (21, 1000))
    ]

    through_jan_15 = history[:3]
    assert [point.value for point in velocity(through_jan_15)] == [5, 10]
    assert [point.value for point in acceleration(through_jan_15)] == [5]

    # The Jan 22 observation changes only calculations after Jan 22; it cannot
    # alter the Jan 15 historical result.
    assert acceleration(history[:3])[-1].value == 5
    assert acceleration(history)[-2].value == 5
