from numpy import ubyte
from numpy.typing import NDArray

from nametable.Tile import Tile
from nametable.Pattern import PatternProtocol
from nametable.PatternStack import PatternStackProtocol


class PatternAnimatorProtocol(PatternProtocol):
    frame: int


class PatternAnimator:
    def __init__(self, stack: PatternStackProtocol, frame: int = 0):
        self.stack = stack
        self.frame = frame

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.stack}, {self.frame})"

    @property
    def numpy_array(self) -> NDArray[ubyte]:
        """
        An array representation of the Tile.

        Returns
        -------
        NDArray[ubyte]
            The Tile represented as an array.
        """
        return self.stack[self.frame].numpy_array

    @property
    def tile(self) -> Tile:
        """
        Returns the Tile the Pattern represents.

        Returns
        -------
        Tile
            The Tile the Pattern represents.
        """
        return self.stack[self.frame].tile
