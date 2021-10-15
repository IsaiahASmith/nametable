from typing import Protocol
from dataclasses import dataclass

from numpy import ubyte
from numpy.typing import NDArray

from nametable.PatternMeta import PatternMeta
from nametable.Animator import AnimatedProtocol, AnimatorProtocol
from nametable.Pattern import PatternProtocol


class PatternAnimatedProtocol(PatternProtocol, AnimatedProtocol, Protocol):
    pass


@dataclass
class PatternAnimated:
    stack: tuple[PatternProtocol]
    animator: AnimatorProtocol

    @property
    def numpy_array(self) -> NDArray[ubyte]:
        """
        An array representation of the Tile.

        Returns
        -------
        NDArray[ubyte]
            The Tile represented as an array.
        """
        return self.stack[self.animator.frame].numpy_array

    @property
    def meta(self) -> PatternMeta:
        """
        Returns the Tile the Pattern represents.

        Returns
        -------
        Tile
            The Tile the Pattern represents.
        """
        return self.stack[self.animator.frame].meta
