from numpy import array_equal

from nametable.Tile import Tile


def test_initialization(tile_ndarray):
    Tile(tile_ndarray)


def test_bytes_conversion(tile_data):
    assert array_equal(Tile.from_bytes(tile_data[0]).tile_data, tile_data[1])
