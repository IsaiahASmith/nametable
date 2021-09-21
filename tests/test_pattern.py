from pytest import fixture

from numpy import meshgrid

from tests.conftest import TILE_BYTES

from nametable.Tile import Tile
from nametable.Pattern import Pattern

TILES: tuple[Tile, ...] = tuple(map(lambda bytes: Tile(bytes), TILE_BYTES))


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


@fixture(params=tuple(map(tuple, meshgrid(TILES, TILES))))
def tile_combo(request) -> tuple[Tile, Tile]:
    """
    Generates the cartesian product of Tiles.

    Returns
    -------
    tuple[Tile, Tile]
        The combination of Tiles.
    """
    return request.param[0]


def test_initialization(tile):
    Pattern(tile)


def test_only_store_one_copy(tile_combo):
    pattern_0, pattern_1 = Pattern(tile_combo[0]), Pattern(tile_combo[1])
    if tile_combo[0] == tile_combo[1]:
        assert pattern_0 is pattern_1
    else:
        assert pattern_0 is not pattern_1
