from nametable.PatternAnimated import PatternAnimated


def test_initialization(animation, animator):
    PatternAnimated(animation, animator)


def test_is_same(animation, animator):
    pattern = PatternAnimated(animation, animator)
    for i in range(len(animation)):
        pattern.animator.frame = i
        assert pattern.tile == animation[i].tile
