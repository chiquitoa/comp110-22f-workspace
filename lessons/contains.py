"""An example of a list utility algorithm."""

# Name: contains
# Function with two parameters
#   needle - what we're searching for
#   haystack - what we're searching through
# Return Type: Bool

def contains(needle: int, haystack: list[int]) -> bool:
    i: int = 0
    while i < len(haystack):
        if needle == haystack[i]:
            return (True)
        i += 1
    return (False)