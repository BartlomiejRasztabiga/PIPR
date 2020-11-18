from zad1 import get_max_consistent_subsequence


def test_regular():
    result = get_max_consistent_subsequence([-2, 15, -3, 4, -1, 2, 1, -5, 4])
    assert result == [15, -3, 4, -1, 2, 1]


def test_empty_sequence():
    result = get_max_consistent_subsequence([])
    assert result == []


def test_one_element():
    result = get_max_consistent_subsequence([-1])
    assert result == [-1]


def test_whole_subsequence():
    result = get_max_consistent_subsequence([1, 2, 3])
    assert result == [1, 2, 3]
