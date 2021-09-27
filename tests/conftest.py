from typing import Optional
from pytest import fixture
from hypothesis.strategies import builds, binary, integers, lists, composite
from itertools import product

from numpy import array, ubyte
from numpy.typing import NDArray


def pattern_meta():
    from nametable.PatternMeta import PatternMeta

    return builds(PatternMeta, binary(min_size=16, max_size=16))


def pattern():
    from nametable.Pattern import Pattern

    return builds(Pattern, pattern_meta())


def pattern_stack(min_size: int = 0, max_size: Optional[int] = None):
    from nametable.PatternStack import PatternStack

    return builds(PatternStack, lists(pattern(), min_size=min_size, max_size=max_size))


def animator(min_frame: int = 0, max_frame: Optional[int] = None):
    from nametable.Animator import Animator

    return builds(Animator, integers(min_value=min_frame, max_value=max_frame))


@composite
def pattern_animated_tuple(draw, min_size: int = 0, max_size: Optional[int] = None):
    stack = draw(pattern_stack(min_size=min_size, max_size=max_size))
    ani = draw(animator(max_frame=len(stack)))
    return stack, ani


@composite
def pattern_animated(draw, min_frames: int = 0, max_frames: Optional[int] = None):
    from nametable.PatternAnimated import PatternAnimated

    stack, animator = draw(pattern_animated_tuple(min_size=min_frames, max_size=max_frames))

    return PatternAnimated(stack, animator)


@fixture
def _tile_data():
    def tile_data_generator():
        yield {
            "data": bytes.fromhex("41 C2 44 48 10 20 40 80 01 02 04 08 16 21 42 87"),
            "numpy": array(
                [
                    [0, 1, 0, 0, 0, 0, 0, 3],
                    [1, 1, 0, 0, 0, 0, 3, 0],
                    [0, 1, 0, 0, 0, 3, 0, 0],
                    [0, 1, 0, 0, 3, 0, 0, 0],
                    [0, 0, 0, 3, 0, 2, 2, 0],
                    [0, 0, 3, 0, 0, 0, 0, 2],
                    [0, 3, 0, 0, 0, 0, 2, 0],
                    [3, 0, 0, 0, 0, 2, 2, 2],
                ],
                dtype=ubyte,
            ),
        }
        yield {
            "data": bytes.fromhex("41 C2 44 48 10 20 40 80 01 02 04 08 16 21 42 87")[::-1],
            "numpy": array(
                [
                    [3, 0, 0, 0, 0, 1, 1, 1],
                    [0, 3, 0, 0, 0, 0, 1, 0],
                    [0, 0, 3, 0, 0, 0, 0, 1],
                    [0, 0, 0, 3, 0, 1, 1, 0],
                    [0, 2, 0, 0, 3, 0, 0, 0],
                    [0, 2, 0, 0, 0, 3, 0, 0],
                    [2, 2, 0, 0, 0, 0, 3, 0],
                    [0, 2, 0, 0, 0, 0, 0, 3],
                ],
                dtype=ubyte,
            ),
        }
        yield {
            "data": bytes.fromhex("14 2C 44 84 01 02 04 06 10 20 40 80 61 11 22 78"),
            "numpy": array(
                [
                    [0, 0, 0, 3, 0, 1, 0, 0],
                    [0, 0, 3, 0, 1, 1, 0, 0],
                    [0, 3, 0, 0, 0, 1, 0, 0],
                    [3, 0, 0, 0, 0, 1, 0, 0],
                    [0, 2, 2, 0, 0, 0, 0, 3],
                    [0, 0, 0, 2, 0, 0, 1, 2],
                    [0, 0, 2, 0, 0, 1, 2, 0],
                    [0, 2, 2, 2, 2, 1, 1, 0],
                ],
                dtype=ubyte,
            ),
        }
        yield {
            "data": bytes.fromhex("14 2C 44 84 01 02 04 06 10 20 40 80 61 11 22 78")[::-1],
            "numpy": array(
                [
                    [0, 1, 1, 1, 1, 2, 2, 0],
                    [0, 0, 1, 0, 0, 2, 1, 0],
                    [0, 0, 0, 1, 0, 0, 2, 1],
                    [0, 1, 1, 0, 0, 0, 0, 3],
                    [3, 0, 0, 0, 0, 2, 0, 0],
                    [0, 3, 0, 0, 0, 2, 0, 0],
                    [0, 0, 3, 0, 2, 2, 0, 0],
                    [0, 0, 0, 3, 0, 2, 0, 0],
                ],
                dtype=ubyte,
            ),
        }

    return tile_data_generator()


@fixture(params=[f"Tile Data {index}" for index in range(4)])
def tile_data(_tile_data) -> tuple[tuple[bytes, NDArray[ubyte]], ...]:
    return next(_tile_data)


@fixture(params=[f"Tile Bytes {index}" for index in range(4)])
def tile_bytes(_tile_data) -> tuple[bytes, ...]:
    return next(_tile_data)["data"]


@fixture(params=[f"Tile NDArray {index}" for index in range(4)])
def tile_ndarray(_tile_data) -> tuple[NDArray[ubyte], ...]:
    return next(_tile_data)["numpy"]


@fixture(params=[f"Tile {index}" for index in range(4)])
def tile(_tile_data):
    from nametable.PatternMeta import PatternMeta

    return PatternMeta(next(_tile_data)["data"])


tile_ = tile


@fixture(scope="function")
def _pattern_combinations():
    def create_pattern_combinations():
        from os import urandom
        from random import randint

        from nametable.PatternMeta import PatternMeta
        from nametable.Pattern import Pattern

        for combo in product(map(lambda data: Pattern(PatternMeta(data)), [urandom(0x10) for _ in range(0x10)])):
            yield combo[: randint(1, 0x10)]

    return create_pattern_combinations()


@fixture(params=([f"Pattern Combination {index}" for index in range(64)]))
def pattern_combo(_pattern_combinations):
    return next(_pattern_combinations)


@fixture(params=[f"Pattern Array {index}" for index in range(16)])
def pattern_array():
    from os import urandom
    from random import randint

    from nametable.PatternTable import PatternArray

    return PatternArray(urandom(0x10 * randint(0, 0x10)))
