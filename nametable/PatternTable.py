from typing import Protocol, Optional
from dataclasses import dataclass
from collections.abc import Iterable

from numpy import array, object_
from numpy.typing import NDArray

from nametable.PatternMeta import PatternMeta
from nametable.Pattern import Pattern, PatternProtocol


@dataclass(frozen=True, eq=True)
class PatternArray:
    data: bytes

    def __len__(self) -> int:
        return len(self.data) // 0x10

    def __getitem__(self, index: int) -> PatternProtocol:
        return Pattern(PatternMeta(self.data[index * 0x10 : (index + 1) * 0x10]))

    def __iter__(self) -> Iterable[PatternProtocol]:
        def iterator():
            data = self.data
            while len(data):
                next_pattern, data = data[:0x10], data[0x10:]
                yield Pattern(PatternMeta(next_pattern))

        return iterator()


class PatternTableProtocol(Protocol):
    pattern_array: PatternArray

    @property
    def numpy_array(self) -> NDArray[object_]:
        ...


@dataclass
class PatternTable:
    pattern_array: PatternArray

    @property
    def numpy_array(self) -> NDArray[object_]:
        """
        Generates an array of Patterns from `PatternArray`

        Returns
        -------
        NDArray[object_]
            A matrix of Patterns with a width of 16.

        Notes
        -----
        If the amount of Patterns does not evenly fit into 16, then None will be
        inserted into the remaining fields.
        """
        patterns: list[Optional[PatternProtocol]] = list(
            map(lambda i: self.pattern_array[i], range(len(self.pattern_array)))
        )
        patterns.extend([None] * (0x10 - (len(patterns) % 0x10)))
        return array(patterns, dtype=object_).reshape((0x10, len(patterns) // 0x10))
