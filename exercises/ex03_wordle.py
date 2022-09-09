"""A game similar to the hugely popular Wordle, now owned by The New York Times"""

__author__ = "730295419"

# Function definition zone

def contains_char(key: str, guess_char: str) -> bool:
    """Detects whether a character in the users guess exists in the answer word"""
    assert len(guess_char) == 1
    yellow_index: int = 0
    yellow_presence: bool = False
    while yellow_presence is False and yellow_index < len(key):
        if guess_char == key[yellow_index]:
            yellow_presence = True
            return(True)
        else:
            yellow_index += 1
    return(False)