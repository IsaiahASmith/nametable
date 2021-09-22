from numpy.core.fromnumeric import repeat
from pytest import fixture
from itertools import product

from numpy import array, ubyte
from numpy.typing import NDArray

from nametable.Tile import Tile
from nametable.Pattern import Pattern


TILE_BYTES = (
    bytes.fromhex("41 C2 44 48 10 20 40 80 01 02 04 08 16 21 42 87"),
    bytes.fromhex("41 C2 44 48 10 20 40 80 01 02 04 08 16 21 42 87")[::-1],
    bytes.fromhex("14 2C 44 84 01 02 04 06 10 20 40 80 61 11 22 78"),
    bytes.fromhex("14 2C 44 84 01 02 04 06 10 20 40 80 61 11 22 78")[::-1],
)

TILE_NDARRAYS = (
    array(
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
        dtype=ubyte,
    ),
    array(
        [
            [3, 0, 0, 0, 0, 1, 1, 1],
            [0, 3, 0, 0, 0, 0, 1, 0],
            [0, 0, 3, 0, 0, 0, 0, 1],
            [0, 0, 0, 3, 0, 1, 1, 0],
            [0, 2, 0, 0, 3, 0, 0, 0],
            [0, 2, 0, 0, 0, 3, 0, 0],
            [2, 2, 0, 0, 0, 0, 3, 0],
            [0, 2, 0, 0, 0, 0, 0, 3],
        ],
        dtype=ubyte,
    ),
    array(
        [
            [0, 0, 0, 3, 0, 1, 0, 0],
            [0, 0, 3, 0, 1, 1, 0, 0],
            [0, 3, 0, 0, 0, 1, 0, 0],
            [3, 0, 0, 0, 0, 1, 0, 0],
            [0, 2, 2, 0, 0, 0, 0, 3],
            [0, 0, 0, 2, 0, 0, 1, 2],
            [0, 0, 2, 0, 0, 1, 2, 0],
            [0, 2, 2, 2, 2, 1, 1, 0],
        ],
        dtype=ubyte,
    ),
    array(
        [
            [0, 1, 1, 1, 1, 2, 2, 0],
            [0, 0, 1, 0, 0, 2, 1, 0],
            [0, 0, 0, 1, 0, 0, 2, 1],
            [0, 1, 1, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 2, 0, 0],
            [0, 3, 0, 0, 0, 2, 0, 0],
            [0, 0, 3, 0, 2, 2, 0, 0],
            [0, 0, 0, 3, 0, 2, 0, 0],
        ],
        dtype=ubyte,
    ),
)

TILE_DATA = tuple(zip(TILE_BYTES, TILE_NDARRAYS))

TILES: tuple[Tile, ...] = tuple(map(lambda bytes: Tile(bytes), TILE_BYTES))

PATTERNS: tuple[Pattern, ...] = tuple(map(lambda tile: Pattern(tile), TILES))

PATTERN_COMBOS: tuple[tuple[Pattern, ...], ...] = tuple(product(PATTERNS, repeat=2))


@fixture(params=TILE_BYTES)
def tile_bytes(request) -> tuple[bytes, ...]:
    """
    Generates a known list of bytes associated with `tile_ndarray`, used for testing.

    Returns
    -------
    bytes
        A series of 16 bytes commonly used for NES testing.
    """
    return request.param


@fixture(params=TILE_NDARRAYS)
def tile_ndarray(request) -> tuple[NDArray[ubyte], ...]:
    """
    Generates a known `NDArray` of type `ubyte` that is associated with `tile_bytes`.

    Returns
    -------
    NDArray[ubyte]
        A `NDArray` of type `ubyte` commonly used for NES testing.
    """
    return request.param


@fixture(params=TILE_DATA)
def tile_data(request) -> tuple[tuple[bytes, NDArray[ubyte]], ...]:
    """
    Merges `tile_bytes` and `tile_ndarray` into one for convenience.

    Parameters
    ----------
    tile_bytes : tuple[bytes, ...]
        The `tile_bytes` fixture.
    tile_ndarray : tuple[NDArray[ubyte], ...]
        The `tile_ndarray` fixture.

    Returns
    -------
    tuple[tuple[bytes, NDArray[ubyte]], ...]
        A tuple of the two merged together.
    """
    return request.param


@fixture(params=TILES)
def tile(request) -> Tile:
    """
    Generates the Tiles commonly used for testing.

    Returns
    -------
    Tile
        A Tile used for testing.
    """
    return request.param


tile_ = tile  # A copy as pytest does not let you copy fixtures otherwise.


@fixture(params=PATTERNS)
def pattern(request) -> Pattern:
    """
    Generates the Patterns commonly used for testing.

    Returns
    -------
    Pattern
        A Pattern used for testing.
    """
    return request.param


@fixture(params=PATTERN_COMBOS)
def pattern_combo(request) -> tuple[Pattern, ...]:
    """
    Generates an arrangement of Patterns used for testing.

    Returns
    -------
    tuple[Pattern, ...]
        An arrangement of Patterns used for testing.
    """
    return request.param
