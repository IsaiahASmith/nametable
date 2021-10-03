from hypothesis import given

from nametable.Pattern import Pattern
from nametable.PatternTable import PatternTable

from tests.conftest import pattern_table, pattern_array


@given(pattern_array())
def test_initialization(pattern_array):
    PatternTable(pattern_array)


@given(pattern_table())
def test_numpy_array(pattern_table):
    assert pattern_table.numpy_array.shape[0] == 0x10


@given(pattern_table())
def test_numpy_array_of_pattern_meta(pattern_table):
    for pattern_meta in pattern_table.numpy_array.flatten():
        if pattern_meta is not None:
            assert isinstance(pattern_meta, Pattern)
