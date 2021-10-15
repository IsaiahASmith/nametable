from hypothesis import given
from hypothesis.strategies import tuples

from nametable.Nametable import Nametable

from tests.conftest import block


@given(tuples(block()))
def test_initialization(blocks):
    Nametable(blocks)
