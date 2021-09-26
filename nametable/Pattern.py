from typing import Protocol
from weakref import WeakKeyDictionary

from numpy import ubyte
from numpy.typing import NDArray

from nametable.PatternMeta import PatternMeta


class PatternProtocol(Protocol):
    @property
    def tile(self) -> PatternMeta:
        ...

    @property
    def numpy_array(self) -> NDArray[ubyte]:
        ...


class Pattern:
    _patterns = WeakKeyDictionary()

    def __new__(cls, tile: PatternMeta, *args, **kwargs):
        """
        As Tiles will often be copied and are immutable, this method ensures that only
        a single copy will be stored inside memory.

        Parameters
        ----------
        tile : PatternMeta
            The Tile to be hashed.
        """
        if tile not in cls._patterns:
            instance = super().__new__(cls, *args, **kwargs)
            cls._patterns[tile] = instance
        return cls._patterns[tile]

    def __init__(self, tile: PatternMeta):
        self._tile = tile
        self._numpy_array = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._tile})"

    @property
    def numpy_array(self) -> NDArray[ubyte]:
        """
        An array representation of the Tile.

        Returns
        -------
        NDArray[ubyte]
            The Tile represented as an array.

        Notes
        -----
        This is a more efficient implementation of the same `Tile` implementation.
        This implementation will cache the result, which can dramatically reduce math operations.
        """
        if self._numpy_array is None:
            self._numpy_array = self.tile.numpy_array
        return self._numpy_array

    @property
    def tile(self) -> PatternMeta:
        """
        Returns the Tile the Pattern represents.

        Returns
        -------
        Tile
            The Tile the Pattern represents.

        Notes
        -----
        The underlying `_tile` should never be changed.
        """
        return self._tile
