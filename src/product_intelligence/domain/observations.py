"""Immutable raw and normalized observations."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from types import MappingProxyType
from typing import Any, Mapping
from uuid import UUID, uuid4


def _utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        raise ValueError("timestamps must include a timezone")
    return value.astimezone(timezone.utc)


def _mapping(value: Mapping[str, Any]) -> Mapping[str, Any]:
    return MappingProxyType(dict(value))


@dataclass(frozen=True, slots=True)
class RawObservation:
    raw_id: UUID
    source: str
    payload: Mapping[str, Any]
    observed_at: datetime
    source_event_at: datetime | None = None
    provenance: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.source.strip():
            raise ValueError("source is required")
        object.__setattr__(self, "observed_at", _utc(self.observed_at))
        if self.source_event_at is not None:
            object.__setattr__(self, "source_event_at", _utc(self.source_event_at))
        object.__setattr__(self, "payload", _mapping(self.payload))
        object.__setattr__(self, "provenance", _mapping(self.provenance))


@dataclass(frozen=True, slots=True)
class Observation:
    observation_id: UUID
    product_id: UUID
    source: str
    metric: str
    value: float
    unit: str
    geography: str
    source_event_at: datetime | None
    observed_at: datetime
    provenance: Mapping[str, str]
    confidence: float

    def __post_init__(self) -> None:
        if not self.source.strip() or not self.metric.strip() or not self.unit.strip():
            raise ValueError("source, metric, and unit are required")
        if not self.geography.strip():
            raise ValueError("geography is required")
        if self.confidence < 0 or self.confidence > 1:
            raise ValueError("confidence must be between 0 and 1")
        if self.value != self.value:
            raise ValueError("value must not be NaN")
        object.__setattr__(self, "observed_at", _utc(self.observed_at))
        if self.source_event_at is not None:
            object.__setattr__(self, "source_event_at", _utc(self.source_event_at))
        object.__setattr__(self, "provenance", _mapping(self.provenance))

    @classmethod
    def create(cls, product_id: UUID, **kwargs: Any) -> "Observation":
        return cls(observation_id=uuid4(), product_id=product_id, **kwargs)
