from typing import Protocol
from dataclasses import dataclass

from numpy import ubyte
from numpy.typing import NDArray

from nametable.Tile import Tile
from nametable.Animator import AnimatedProtocol, AnimatorProtocol
from nametable.Pattern import PatternProtocol
from nametable.PatternStack import PatternStackProtocol


class PatternAnimatorProtocol(PatternProtocol, AnimatedProtocol, Protocol):
    pass


@dataclass
class PatternAnimated:
    stack: PatternStackProtocol
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
    def tile(self) -> Tile:
        """
        Returns the Tile the Pattern represents.

        Returns
        -------
        Tile
            The Tile the Pattern represents.
        """
        return self.stack[self.animator.frame].tile
