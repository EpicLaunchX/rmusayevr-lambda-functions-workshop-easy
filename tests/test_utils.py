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
    assert sort_list([-1, -3, 2, 0]) == [-3, -1, 0, 2]
