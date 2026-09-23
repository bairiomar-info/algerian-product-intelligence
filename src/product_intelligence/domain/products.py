"""Canonical product entities."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from types import MappingProxyType
from typing import Mapping
from uuid import UUID, uuid4


def _utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        raise ValueError("timestamps must include a timezone")
    return value.astimezone(timezone.utc)


@dataclass(frozen=True, slots=True)
class Product:
    product_id: UUID = field(default_factory=uuid4)
    canonical_name: str = ""
    product_family: str | None = None
    category: str | None = None
    attributes: Mapping[str, str] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    provenance: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.canonical_name.strip():
            raise ValueError("canonical_name is required")
        object.__setattr__(self, "created_at", _utc(self.created_at))
        object.__setattr__(self, "attributes", MappingProxyType(dict(self.attributes)))
        object.__setattr__(self, "provenance", MappingProxyType(dict(self.provenance)))

    @classmethod
    def named(cls, name: str, **kwargs: object) -> "Product":
        return cls(canonical_name=name, **kwargs)
