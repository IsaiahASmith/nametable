from typing import Protocol
from dataclasses import dataclass

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
    def pattern_array(self) -> tuple[Pattern, ...]:
        return self.pattern_tables[self.animator.frame].pattern_array
