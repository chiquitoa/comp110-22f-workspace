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

def emojified(guess: str, key: str) -> str:
    """Provides the emoji string for the result of a given guess"""
    # Parameters and defining variables
    assert len(guess) == len(key)
    index: int = 0
    result: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    # print(guess[index]) # For debug
    # print(key[index]) # For debug

    while index < len(key):
        if guess[index] == key[index]:
            result += GREEN_BOX
            index += 1
            # print(result) # For debug
        else:
            if contains_char(key, guess[index]) == True:
                result += YELLOW_BOX
                index += 1
                # print(result) # For debug
            else:
                result += WHITE_BOX
                index += 1
                # print(result) # For debug
    return(result)

def input_guess(key_length: int) -> str:
    """Obtains a guess of the proper length from the user"""
    guess: str = ""
    guess = input(f"Enter a {key_length} character word: ")
    while len(guess) != key_length:
        guess = input(f"That wasn't {key_length} chars! Try again: ")
    print(guess)