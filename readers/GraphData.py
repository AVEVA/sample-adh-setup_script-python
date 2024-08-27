from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar('T')


@dataclass
class GraphData(Generic[T]):
    Data: list[T]
    TypeId: str = None
