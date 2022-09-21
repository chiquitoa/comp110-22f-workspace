"""A program to practice fussing with lists."""

__author__ = "730295419"


def all(collection: list[int], item: int) -> bool:
    """Determines whether a given item matches every item in a given list."""
    i: int = 0
    
    if collection == []:
        return (False)

    while i <= (len(collection) - 1):
        if collection[i] == item:
            i += 1
        else:
            return (False)
    return (True)


def max(input: list[int]) -> int:
    """Returns the highest value in a provided list."""
    i: int = 0
    answer: int = 0
    
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    answer = input[0]

    while i <= (len(input) - 1):
        if input[i] > answer:
            answer = input[i]
            i += 1
        else:
            i += 1
    return (answer)


def is_equal(input: list[int], compare: list[int]) -> bool:
    """Informs whether two given lists are identical or not."""
    i: int = 0
    if len(input) != len(compare):
        return (False)

    while i <= (len(input) - 1):
        if input[i] == compare[i]:
            i += 1
        else:
            return (False)
    return (True)