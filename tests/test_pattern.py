from nametable.Pattern import Pattern


def test_initialization(tile):
    Pattern(tile)


def test_only_store_one_copy(tile, tile_):
    pattern_0, pattern_1 = Pattern(tile), Pattern(tile_)
    if tile == tile_:
        assert pattern_0 is pattern_1
    else:
        assert pattern_0 is not pattern_1
