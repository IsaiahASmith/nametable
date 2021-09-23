from dataclasses import dataclass

from numpy import ubyte, add, frombuffer, unpackbits
from numpy.typing import NDArray


@dataclass(frozen=True, eq=True)
class Tile:
    data: bytes

    WIDTH = 8
    HEIGHT = 8

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.data.hex()})"

    @property
    def numpy_array(self) -> NDArray[ubyte]:
        """
        An array representation of the Tile.

        Returns
        -------
        NDArray[ubyte]
            The Tile represented as an array.
        """
        array = unpackbits(frombuffer(self.data, dtype=ubyte)).reshape((2, Tile.HEIGHT, Tile.WIDTH))
        return add(array[0, :, :], array[1, :, :] * 2)
