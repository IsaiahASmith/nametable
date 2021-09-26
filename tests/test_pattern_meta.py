from numpy import array_equal

from nametable.PatternMeta import PatternMeta


def test_initialization(tile_bytes):
    PatternMeta(tile_bytes)


def test_bytes_conversion(tile_data):
    assert array_equal(PatternMeta(tile_data["data"]).numpy_array, tile_data["numpy"])
