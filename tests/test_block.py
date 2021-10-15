from hypothesis import given
from pytest import raises

from tests.conftest import partially_correct_blocks

from nametable.Block import Block, BlockInvalidSizeException


@given(partially_correct_blocks(min_size=5))
def test_only_four_patterns(data):
    table, tiles = data
    with raises(BlockInvalidSizeException):
        Block(table, tiles)
