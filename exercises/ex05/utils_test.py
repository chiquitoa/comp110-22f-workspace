"""Tests for utils.py"""

__Author__ = "730295419"

from utils import only_evens, concat, sub

# Testing only_evens

def test_only_evens_one_even() -> None:
    """Tests when there is a single even number."""
    given_list: list[int] = [1, 2, 3]
    assert only_evens([1, 2, 3]) == [2]

def test_only_evens_no_evens() -> None:
    """Tests when there are no even numbers in the list."""
    given_list: list[int] = [1, 5, 3]
    assert only_evens([1, 5, 3]) == []

def test_only_evens_no_input() -> None:
    """Tests when there is no list provided."""
    given_list: list[int] = []
    assert only_evens([]) == []

# Testing concat

def test_concat_normal_use1() -> None:
    """Tests a normal use case."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_concat_normal_use_2() -> None:
    """Tests a normal use case where the lists are not equal in length."""
    assert concat([3], [4, 5, 6]) == [3, 4, 5, 6]

def test_concat_empty_list1() -> None:
    """Tests a use case where the first list is empty."""
    assert concat([], [4, 5, 6]) == [4, 5, 6]

def test_concat_empty_list2() -> None:
    """Tests a use case where the second list is empty."""
    assert concat([1, 2, 3], []) == [1, 2, 3]

# Testing sub

def test_sub_site_example() -> None:
    """Tests the exampmle from the course website."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]

def test_sub_negative_start() -> None:
    """Tests when there is a negative start value."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, -2, 2) == [10, 20]

def test_sub_end_larger_than_length() -> None:
    """Tests when the end value is larger than the length of the provided list."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 2, 6) == [30, 40]

def test_sub_no_list() -> None:
    """Tests when there is no list provided."""
    a_list = []
    assert sub(a_list, 1, 3) == []

def test_sub_start_beyond_list() -> None:
    """Tests when the start value is beyond the length of the provided list."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 6, 8) == []

def test_sub_end_0() -> None:
    """Tests when the end value is smaller than 1."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, -4, 0) == []

def test_sub_disorderly_paramters() -> None:
    """Tests when the start value is greater than the end value."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 3, 1) == []