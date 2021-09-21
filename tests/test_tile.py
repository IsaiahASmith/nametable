from numpy import array_equal

from nametable.Tile import Tile


def test_initialization(tile_bytes):
    Tile(tile_bytes)


def test_bytes_conversion(tile_data):
    assert array_equal(Tile(tile_data[0]).numpy_array, tile_data[1])
