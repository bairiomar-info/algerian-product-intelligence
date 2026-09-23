"""Provider-independent source adapter contracts and a deterministic fixture adapter."""

from abc import ABC, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime
from typing import Any
from uuid import UUID

from product_intelligence.domain.observations import RawObservation


class SourceAdapter(ABC):
    source_name: str
    capabilities: frozenset[str] = frozenset()

    @abstractmethod
    def collect(self, *, product_id: UUID, observed_at: datetime) -> Iterable[RawObservation]:
        """Collect source records without converting them into domain metrics."""


@dataclass(frozen=True, slots=True)
class FixtureAdapter(SourceAdapter):
    source_name: str
    records: tuple[dict[str, Any], ...]
    capabilities: frozenset[str] = frozenset({"fixture"})

    def collect(self, *, product_id: UUID, observed_at: datetime) -> Iterable[RawObservation]:
        for record in self.records:
            yield RawObservation(
                raw_id=UUID(record["raw_id"]) if "raw_id" in record else UUID(int=0),
                source=self.source_name,
                payload={"product_id": str(product_id), **record.get("payload", {})},
                observed_at=observed_at,
                source_event_at=record.get("source_event_at"),
                provenance={"adapter": "fixture", "fixture_id": str(record.get("id", "unknown"))},
            )
