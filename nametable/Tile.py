from dataclasses import dataclass

from numpy import ubyte, add, frombuffer, unpackbits
from numpy.typing import NDArray


@dataclass(frozen=True, eq=True)
class Tile:
    tile_data: NDArray[ubyte]

    WIDTH = 8
    HEIGHT = 8

    @classmethod
    def from_np_bits(cls, lower: NDArray[ubyte], upper: NDArray[ubyte]):
        """
        Creates a Tile from a NDArray representing a bitmap of the lower and upper bits.

        Parameters
        ----------
        lower : NDArray[ubyte]
            The bits representing the 0 or 1 of the color index.
        upper : NDArray[ubyte]
            The bits representing the 0 or 2 of the color index.

        Notes
        -----
        This method is meant primarily for NES styled Tiles.
        """
        return cls(add(lower, upper * 2))

    @classmethod
    def from_bytes(cls, data: bytes):
        """
        Creates a Tile from bytes representing a two bits per pixel format.

        Parameters
        ----------
        data : bytes
            The data representing the Tile.

        Notes
        -----
        This method is meant primarily for NES styled Tiles.
        """
        array = unpackbits(frombuffer(data, dtype=ubyte)).reshape((2, 8, 8))
        return cls.from_np_bits(array[0, :, :], array[1, :, :])
