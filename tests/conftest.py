from pytest import fixture

from numpy import array, ubyte
from numpy.typing import NDArray

from nametable.Tile import Tile
from nametable.Pattern import Pattern
from nametable.PatternStack import PatternStack

TILE_DATA = (
    {
        "data": bytes.fromhex("41 C2 44 48 10 20 40 80 01 02 04 08 16 21 42 87"),
        "numpy": array(
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
    },
    {
        "data": bytes.fromhex("41 C2 44 48 10 20 40 80 01 02 04 08 16 21 42 87")[::-1],
        "numpy": array(
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
    },
    {
        "data": bytes.fromhex("14 2C 44 84 01 02 04 06 10 20 40 80 61 11 22 78"),
        "numpy": array(
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
    },
    {
        "data": bytes.fromhex("14 2C 44 84 01 02 04 06 10 20 40 80 61 11 22 78")[::-1],
        "numpy": array(
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
    },
)


@fixture(params=TILE_DATA)
def tile_data(request) -> tuple[tuple[bytes, NDArray[ubyte]], ...]:
    return request.param


@fixture
def tile_bytes(tile_data) -> tuple[bytes, ...]:
    return tile_data["data"]


@fixture
def tile_ndarray(tile_data) -> tuple[NDArray[ubyte], ...]:
    return tile_data["numpy"]


@fixture(params=map(lambda data: Tile(data["data"]), TILE_DATA))
def tile(tile_bytes) -> Tile:
    return Tile(tile_bytes)


tile_ = tile


@fixture(scope="function")
def pattern(tile) -> Pattern:
    return Pattern(tile)


pattern_ = pattern


@fixture
def pattern_combo(pattern, pattern_) -> tuple[Pattern, ...]:
    return pattern, pattern_


@fixture
def animation(pattern_combo) -> PatternStack:
    return PatternStack(pattern_combo)
