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

    def __eq__(self, other) -> bool:
        return list(self.data) == list(other.data)

    def __ne__(self, other) -> bool:
        return list(self.data) != list(other.data)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.data.hex()})"

    @classmethod
    def from_numpy_array(cls, array: NDArray[ubyte]):
        """
        Creates a Pattern from a numpy array of a size (8, 8).

        Parameters
        ----------
        array : NDArray[ubyte]
            The numpy array to be converted.
        """
        assert array.shape == (8, 8)

        a = array.flatten()
        bitmap = [element & 0b1 for element in a] + [(element & 0b10) >> 1 for element in a]
        ba = bytearray(16)
        for index, element in enumerate(bitmap):
            big_endian_offset = 8 * (index // 64)
            byte_offset = (index // 8) % 8
            bit_offset = abs(8 - (index % 8)) - 1
            ba[big_endian_offset + byte_offset] += element << bit_offset

        assert len(ba) == 16

        return cls(bytes(ba))

    @property
    def numpy_array(self) -> NDArray[ubyte]:
        """
        An array representation of the PatternMeta.

        Returns
        -------
        NDArray[ubyte]
            The PatternMeta represented as an array.
        """
        assert len(self.data) == 16

        array = unpackbits(frombuffer(self.data, dtype=ubyte)).reshape((2, self.HEIGHT, self.WIDTH))
        array = add(array[0, :, :], array[1, :, :] * 2)

        assert array.shape == (8, 8)

        return array
