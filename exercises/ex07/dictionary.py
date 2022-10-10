"""This is exercise 07. Today is a day."""

__author__ = "730295419"


def invert_dictionary(sample: dict[str, str]) -> dict[str, str]:
    """Inverts a provided dictionary."""
    inverse_sample: dict[str, str]
    inverse_sample = dict()
    for x in sample:
        if sample[x] in inverse_sample:
            print(f"{sample[x]} already present in inverse_sample.")
        else:
            inverse_sample[sample[x]] = x
    return (inverse_sample)


def count(input: list[str]) -> dict[str, int]:
    """Returns a dictionary with the count of each item in a list."""
    result: dict[str, int]
    result = dict()
    for x in input:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return (result)


def favorite_color(colors: dict[str, str]) -> str:
    """Spits out the most popular favorite color from a dictionary of peoples' favorite colors."""
    favorite_color: str = ""
    colors_only: list = list(colors.values())
    colors_counted: dict = count(colors_only)
    if colors == {}:
        return ("")
    favorite_color = (max(colors_counted, key=colors_counted.get))
    return (favorite_color)