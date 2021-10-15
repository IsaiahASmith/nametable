from typing import Protocol
from weakref import WeakKeyDictionary

from numpy import ubyte
from numpy.typing import NDArray

from nametable.PatternMeta import PatternMeta


class PatternProtocol(Protocol):
    """
    An `Object Oriented <https://en.wikipedia.org/wiki/Object-oriented_programming>`_
    wrapper around :class:`~nametable.PatternMeta.PatternMeta`.
    This class enables easier extensions and edits on
    :class:`~nametable.PatternMeta.PatternMeta` without needing to understand the
    internals of the NES.

    See Also
    --------
    :class:`~nametable.PatternMeta.PatternMeta`
    """

    @property
    def meta(self) -> PatternMeta:
        """
        Provides the wrapped meta class that the instance is representing.

        Returns
        -------
        PatternMeta
            The current :class:`~nametable.PatternMeta.PatternMeta` that this instance
            is representing.

        See Also
        --------
        :class:`~nametable.PatternMeta.PatternMeta`
        """

    @property
    def numpy_array(self) -> NDArray[ubyte]:
        """
        Provides a Numpy array that represents the pattern as a 2D matrix of the pixels of
        the pattern.

        Returns
        -------
        NDArray[ubyte]
            The array is equivalent to the meta that the instance is representing.

        Notes
        -----
        The purpose of extending the responsibility of creating an array to this instance
        is to provide additional ability to cache and utilize other techniques to
        improve performance.

        See Also
        --------
        :class:`~nametable.PatternMeta.PatternMeta`
        """


class Pattern:
    _patterns = WeakKeyDictionary()

    def __new__(cls, meta: PatternMeta):
        """
        As Tiles will often be copied and are immutable, this method ensures that only
        a single copy will be stored inside memory.

        Parameters
        ----------
        meta : PatternMeta
            The Tile to be hashed.
        """
        if meta not in cls._patterns:
            instance = super().__new__(cls)
            cls._patterns[meta] = instance
        return cls._patterns[meta]

    def __init__(self, meta: PatternMeta):
        self._meta = meta
        self._numpy_array = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._meta})"

    @classmethod
    def from_numpy_array(cls, array: NDArray[ubyte]):
        """
        Creates a Pattern from a numpy array of a size (8, 8).

        Parameters
        ----------
        array : NDArray[ubyte]
            The numpy array to be converted.
        """
        return cls(PatternMeta.from_numpy_array(array))

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
            self._numpy_array = self.meta.numpy_array
        return self._numpy_array

    @property
    def meta(self) -> PatternMeta:
        """
        Returns the Tile the Pattern represents.

        Returns
        -------
        Tile
            The Tile the Pattern represents.

        Notes
        -----
        The underlying `_meta` should never be changed.
        """
        return self._meta
