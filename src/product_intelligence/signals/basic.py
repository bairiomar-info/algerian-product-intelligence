"""Initial transparent time-series signals."""

from collections.abc import Sequence
from dataclasses import dataclass
from datetime import datetime

from product_intelligence.domain.observations import Observation


@dataclass(frozen=True, slots=True)
class SignalPoint:
    at: datetime
    value: float


def level(history: Sequence[Observation]) -> tuple[SignalPoint, ...]:
    ordered = sorted(history, key=lambda item: (item.source_event_at or item.observed_at, item.observed_at, str(item.observation_id)))
    return tuple(SignalPoint(item.source_event_at or item.observed_at, item.value) for item in ordered)


def velocity(history: Sequence[Observation]) -> tuple[SignalPoint, ...]:
    points = level(history)
    return tuple(SignalPoint(current.at, current.value - previous.value) for previous, current in zip(points, points[1:]))


def acceleration(history: Sequence[Observation]) -> tuple[SignalPoint, ...]:
    velocities = velocity(history)
    return tuple(SignalPoint(current.at, current.value - previous.value) for previous, current in zip(velocities, velocities[1:]))
