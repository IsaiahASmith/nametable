from typing import Protocol
from dataclasses import dataclass

from nametable.Pattern import Pattern


class PatternTableProtocol(Protocol):
    pattern_array: tuple[Pattern, ...]


@dataclass(frozen=True, eq=True)
class PatternTable:
    pattern_array: tuple[Pattern, ...]
