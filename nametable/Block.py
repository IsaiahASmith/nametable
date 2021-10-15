from typing import Protocol
from dataclasses import dataclass

from nametable.PatternTable import PatternTableProtocol


class BlockInvalidSizeException(ValueError):
    ...


class BlockProtocol(Protocol):
    pattern_table: PatternTableProtocol
    patterns: tuple[int, int, int, int]


@dataclass(frozen=True, eq=True)
class Block:
    pattern_table: PatternTableProtocol
    patterns: tuple[int, int, int, int]

    def __post_init__(self):
        if len(self.patterns) != 4:
            raise BlockInvalidSizeException(f"Block must only have four patterns, {len(self.patterns)} given")
