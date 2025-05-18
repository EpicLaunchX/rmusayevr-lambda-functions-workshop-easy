from src.pytemplate.utils.filtering import filter_even_numbers
from src.pytemplate.utils.sorting import sort_list


def test_sort_list_empty():
    assert sort_list([]) == []


def test_sort_list_sorted():
    assert sort_list([1, 2, 3]) == [1, 2, 3]


def test_sort_list_unsorted():
    assert sort_list([3, 1, 2]) == [1, 2, 3]


def test_sort_list_duplicates():
    assert sort_list([3, 1, 2, 1]) == [1, 1, 2, 3]


def test_sort_list_negative_numbers():
    assert sort_list([-1, -3, 4, 0]) == [-3, -1, 0, 4]


def test_filter_even_numbers_all_even():
    assert filter_even_numbers([2, 4, 6]) == [2, 4, 6]


def test_filter_even_numbers_mixed():
    assert filter_even_numbers([1, 2, 3, 4, 5]) == [2, 4]


def test_filter_even_numbers_none_even():
    assert filter_even_numbers([1, 3, 5]) == []


def test_filter_even_numbers_empty_list():
    assert filter_even_numbers([]) == []


def test_filter_even_numbers_with_zero():
    assert filter_even_numbers([0, 1, 2]) == [0, 2]
