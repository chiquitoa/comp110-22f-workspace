"""Function skeletons and implementations."""

__Author__ = "730295419"

from tracemalloc import start


def only_evens(given_list: list[int]) -> list[int]:
    """Takes a list of ints and returns a list of only the even values."""
    even_list: list[int] = []
    i: int = 0
    # print(f"The length of the given list is {len(given_list)}") # For troubleshooting
    while i < (len(given_list)):
        # print(f"i is currently {i}") # For troubleshooting
        if (given_list[i] % 2) == 0:
            even_list.append(given_list[i])
            # print(f"even_list is now {even_list}") # For troubleshooting
        i += 1
    return (even_list)

def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Takes two lists and concatenates them into a single list."""
    whole_list: list[int] = []
    i: int = 0
    # Concatenate list 1 zone
    while i < (len(list1)):
        whole_list.append(list1[i])
        i += 1
    i = 0
    # Concatenate list 2 zone
    while i < (len(list2)):
        whole_list.append(list2[i])
        i += 1
    return (whole_list)

def sub(list1: list[int], start: int, end: int) -> list[int]:
    """Takes a list and returns a requested subset."""
    subset_list: list[int] = []
    i: int = start
    if i < 0:
        i = 0
    while i < end and i < len(list1):
        subset_list.append(list1[i])
        i += 1
    return subset_list
