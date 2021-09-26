from dataclasses import dataclass

from numpy import ubyte, add, frombuffer, unpackbits
from numpy.typing import NDArray


@dataclass(frozen=True, eq=True)
class PatternMeta:
    """
    The most basic representation of a Pattern that is valid.

    This contains the data for a Tile, which is referred to as a Pattern.
    """

    data: bytes

    WIDTH = 8
    HEIGHT = 8

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.data.hex()})"

    @property
    def numpy_array(self) -> NDArray[ubyte]:
        """
        An array representation of the PatternMeta.

        Returns
        -------
        NDArray[ubyte]
            The PatternMeta represented as an array.
        """
        array = unpackbits(frombuffer(self.data, dtype=ubyte)).reshape((2, self.HEIGHT, self.WIDTH))
        return add(array[0, :, :], array[1, :, :] * 2)
