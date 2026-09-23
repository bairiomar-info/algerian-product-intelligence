"""Small append-only in-memory repository for M1."""

from collections import defaultdict
from collections.abc import Iterable
from uuid import UUID

from product_intelligence.domain.observations import Observation, RawObservation
from product_intelligence.domain.products import Product


class InMemoryRepository:
    def __init__(self) -> None:
        self._products: dict[UUID, Product] = {}
        self._raw: dict[UUID, RawObservation] = {}
        self._observations: dict[UUID, Observation] = {}

    def add_product(self, product: Product) -> None:
        existing = self._products.get(product.product_id)
        if existing is not None and existing != product:
            raise ValueError("conflicting product identity")
        self._products[product.product_id] = product

    def add_raw(self, raw: RawObservation) -> None:
        existing = self._raw.get(raw.raw_id)
        if existing is not None and existing != raw:
            raise ValueError("conflicting raw observation")
        self._raw[raw.raw_id] = raw

    def add_observation(self, observation: Observation) -> None:
        if observation.product_id not in self._products:
            raise ValueError("product must exist before observation")
        existing = self._observations.get(observation.observation_id)
        if existing is not None and existing != observation:
            raise ValueError("conflicting observation identity")
        self._observations[observation.observation_id] = observation

    def history(self, product_id: UUID, metric: str | None = None) -> tuple[Observation, ...]:
        values = (item for item in self._observations.values() if item.product_id == product_id and (metric is None or item.metric == metric))
        return tuple(sorted(values, key=lambda item: (item.source_event_at or item.observed_at, item.observed_at, str(item.observation_id))))

    def raw(self, raw_id: UUID) -> RawObservation:
        return self._raw[raw_id]
