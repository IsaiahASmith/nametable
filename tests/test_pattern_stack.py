from hypothesis import given
from hypothesis.strategies import tuples

from nametable.PatternStack import PatternStack

from tests.conftest import pattern, pattern_stack


@given(tuples(pattern()))
def test_initialization(patterns):
    PatternStack(patterns)


@given(pattern_stack())
def test_length(pattern_stack):
    assert len(pattern_stack) == len(pattern_stack.stack)


@given(pattern_stack())
def test_get_item(pattern_stack):
    for (guess, answer) in zip(pattern_stack, pattern_stack.stack):
        assert guess == answer


@given(pattern_stack(), pattern_stack())
def test_equality(pattern_stack, pattern_stack_):
    assert (pattern_stack == pattern_stack_) == (list(pattern_stack.stack) == list(pattern_stack_.stack))


@given(pattern_stack(), pattern_stack())
def test_inequality(pattern_stack, pattern_stack_):
    assert (pattern_stack != pattern_stack_) == (list(pattern_stack.stack) != list(pattern_stack_.stack))


@given(pattern_stack(), pattern_stack())
def test_equality_cannot_be_not_equal(pattern_stack, pattern_stack_):
    assert (pattern_stack == pattern_stack_) != (pattern_stack != pattern_stack_)
