from typing import Protocol, Optional
from dataclasses import dataclass

from numpy import array, object_
from numpy.typing import NDArray

from nametable.Pattern import Pattern, PatternProtocol


class PatternTableProtocol(Protocol):
    pattern_array: tuple[Pattern]

    @property
    def numpy_array(self) -> NDArray[object_]:
        ...


@dataclass
class PatternTable:
    pattern_array: tuple[Pattern]

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
