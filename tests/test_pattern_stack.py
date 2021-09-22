from nametable.PatternStack import PatternStack


def test_initialization(pattern_combo):
    PatternStack(pattern_combo)


def test_length(pattern_combo):
    assert len(PatternStack(pattern_combo)) == len(pattern_combo)


def test_get_item(pattern_combo):
    for (guess, answer) in zip(pattern_combo, PatternStack(pattern_combo)):  # type: ignore
        assert guess == answer
