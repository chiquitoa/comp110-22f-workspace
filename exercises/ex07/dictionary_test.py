"""This tests exercise 07. Today is also a day."""

__author__ = "730295419"

from exercises.ex07.dictionary import invert_dictionary, favorite_color, count

def test_invert_dictionary_normal() -> None:
    """Tests inverting a dictionary under normal circumstances."""
    assert invert_dictionary({"Patrick": "Wolfe", "Andre": "Chiquito"}) == {"Wolfe": "Patrick", "Chiquito": "Andre"}


def test_invert_dictionary_with_duplicate() -> None:
    """Tests inverting a dictionary where a duplicate key results."""
    assert invert_dictionary({"Patrick": "Wolfe", "Andre": "Chiquito", "Daniel": "Chiquito"}) == {"Wolfe": "Patrick", "Chiquito": "Andre"}


def test_invert_dictionary_empty_dict() -> None:
    """Tests running the function with an empty dictionary."""
    assert invert_dictionary({}) == {}


def test_count_normal() -> None:
    """Tests running the count function under normal circumstances."""
    assert count(["blue", "blue", "blue", "red", "green"]) == {"blue": 3, "red": 1, "green": 1}


def test_count_normal() -> None:
    """Tests running the count function under different normal circumstances."""
    assert count(["blue", "red", "green"]) == {"blue": 1, "red": 1, "green": 1}


def test_count_empty_list() -> None:
    """Tests running the count function with an empty input."""
    assert count([]) == {}


def test_favorite_color_tie() -> None:
    """Tests the favorite color function with two equal common colors."""
    assert favorite_color({"Marc": "purple", "Ezri": "blue", "Kris": "blue", "Andre": "purple"}) == "purple"


def test_favorite_color_normal() -> None:
    """Tests the favorite color function under normal circumstances."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_empty_dict() -> None:
    """Tests the favorite color function when it is provided with an empty dictionary."""
    assert favorite_color({}) == ""