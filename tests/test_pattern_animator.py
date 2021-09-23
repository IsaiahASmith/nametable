from nametable.PatternAnimator import PatternAnimator


def test_initialization(animation):
    PatternAnimator(animation)
    PatternAnimator(animation, len(animation))


def test_is_same(animation):
    animator = PatternAnimator(animation)
    for i in range(len(animation)):
        animator.frame = i
        assert animator.tile == animation[i].tile
