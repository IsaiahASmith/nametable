from hypothesis import given
from hypothesis.strategies import binary

from numpy import array_equal

from nametable.PatternMeta import PatternMeta


@given(binary(min_size=16, max_size=16))
def test_initialization(bytes):
    PatternMeta(bytes)


@given(binary(min_size=16, max_size=16), binary(min_size=16, max_size=16))
def test_equality(bytes, bytes_):
    assert (PatternMeta(bytes) == PatternMeta(bytes_)) == (list(bytes) == list(bytes_))


@given(binary(min_size=16, max_size=16), binary(min_size=16, max_size=16))
def test_inequality(bytes, bytes_):
    assert (PatternMeta(bytes) != PatternMeta(bytes_)) == (list(bytes) != list(bytes_))


@given(binary(min_size=16, max_size=16), binary(min_size=16, max_size=16))
def test_equality_cannot_be_not_equal(bytes, bytes_):
    assert (PatternMeta(bytes) == PatternMeta(bytes_)) != (PatternMeta(bytes) != PatternMeta(bytes_))


@given(binary(min_size=16, max_size=16))
def test_conversion(bytes):
    assert PatternMeta(bytes) == PatternMeta.from_numpy_array(PatternMeta(bytes).numpy_array)


@given(binary(min_size=16, max_size=16))
def test_numpy_array_shape(bytes):
    assert PatternMeta(bytes).numpy_array.shape == (8, 8)


def test_bytes_conversion(tile_data):
    assert array_equal(PatternMeta(tile_data["data"]).numpy_array, tile_data["numpy"])
