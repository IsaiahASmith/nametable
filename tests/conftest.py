from pytest import fixture

from numpy import array, ubyte
from numpy.typing import NDArray


@fixture
def tile_bytes() -> bytes:
    """
    Generates a known list of bytes associated with `tile_ndarray`, used for testing.

    Returns
    -------
    bytes
        A series of 16 bytes commonly used for NES testing.
    """
    return bytes.fromhex("41 C2 44 48 10 20 40 80 01 02 04 08 16 21 42 87")


@fixture
def tile_ndarray() -> NDArray[ubyte]:
    """
    Generates a known `NDArray` of type `ubyte` that is associated with `tile_bytes`.

    Returns
    -------
    NDArray[ubyte]
        A `NDArray` of type `ubyte` commonly used for NES testing.
    """
    return array(
        [
            [0, 1, 0, 0, 0, 0, 0, 3],
            [1, 1, 0, 0, 0, 0, 3, 0],
            [0, 1, 0, 0, 0, 3, 0, 0],
            [0, 1, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 0, 2, 2, 0],
            [0, 0, 3, 0, 0, 0, 0, 2],
            [0, 3, 0, 0, 0, 0, 2, 0],
            [3, 0, 0, 0, 0, 2, 2, 2],
        ],
        dtype=float,
    )
