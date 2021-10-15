from typing import Protocol
from dataclasses import dataclass

from numpy import ubyte, concatenate
from numpy.typing import NDArray

from nametable.PatternTable import PatternTableProtocol


class BlockInvalidSizeException(ValueError):
    ...


class PatternTableIndexException(IndexError):
    ...


class BlockProtocol(Protocol):
    pattern_table: PatternTableProtocol
    patterns: tuple[int, int, int, int]

    @property
    def numpy_array(self) -> NDArray[ubyte]:
        ...


@dataclass(frozen=True, eq=True)
class Block:
    pattern_table: PatternTableProtocol
    patterns: tuple[int, int, int, int]

    def __post_init__(self):
        if len(self.patterns) != 4:
            raise BlockInvalidSizeException(f"Block must only have four patterns, {len(self.patterns)} given")
        if any(pattern > len(self.pattern_table.pattern_array) for pattern in self.patterns):
            raise PatternTableIndexException(
                f"Invalid index to Pattern Table of size {len(self.pattern_table.pattern_array)}"
            )
        if any(pattern < 0 for pattern in self.patterns):
            raise PatternTableIndexException("Pattern indexes to Pattern Table must be positive")

    @property
    def numpy_array(self) -> NDArray[ubyte]:
        return concatenate(
            (
                concatenate(
                    (
                        self.pattern_table.pattern_array[self.patterns[0]].numpy_array,
                        self.pattern_table.pattern_array[self.patterns[1]].numpy_array,
                    )
                ),
                concatenate(
                    (
                        self.pattern_table.pattern_array[self.patterns[2]].numpy_array,
                        self.pattern_table.pattern_array[self.patterns[3]].numpy_array,
                    )
                ),
            ),
            axis=1,
        )
