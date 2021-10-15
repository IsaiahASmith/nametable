from hypothesis import given
from pytest import raises

from tests.conftest import pattern_table

from nametable.Block import Block, BlockInvalidSizeException


@given(pattern_table())
def test_only_four_patterns(pattern_table):
    with raises(BlockInvalidSizeException):
        Block(pattern_table, (0, 0, 0, 0, 0))
