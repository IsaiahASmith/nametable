from nametable.PatternTable import PatternTable


def test_initialization(pattern_array):
    PatternTable(pattern_array)


def test_numpy_array(pattern_array):
    ptn_tbl = PatternTable(pattern_array)
    assert ptn_tbl.numpy_array.shape[0] == 0x10
