from nametable.Tile import Tile

from numpy import array_equal


def test_initialization(tile_ndarray):
    Tile(tile_ndarray)


def test_bytes_conversion(tile_bytes, tile_ndarray):
    assert array_equal(Tile.from_bytes(tile_bytes).tile_data, tile_ndarray)
