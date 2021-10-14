from typing import Protocol
from dataclasses import dataclass

from numpy import object_
from numpy.typing import NDArray

from nametable.Animator import AnimatedProtocol, AnimatorProtocol
from nametable.PatternTable import PatternTableProtocol
from nametable.Pattern import Pattern


class PatternTableAnimatedProtocol(PatternTableProtocol, AnimatedProtocol, Protocol):
    ...


@dataclass
class PatternTableAnimated:
    pattern_tables: tuple[PatternTableProtocol]
    animator: AnimatorProtocol

    @property
    def pattern_array(self) -> tuple[Pattern]:
        return self.pattern_tables[self.animator.frame].pattern_array

    @property
    def numpy_array(self) -> NDArray[object_]:
        return self.pattern_tables[self.animator.frame].numpy_array
