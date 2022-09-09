"""A game similar to the hugely popular Wordle, now owned by The New York Times"""

__author__ = "730295419"

# Tests for yellow blocks
def contains_char(key: str, guess_char: str) -> bool:
    """Detects whether a character in the users guess exists in the answer word"""
    # Variable definition zone
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

# Creates the colored block string for each guess
def emojified(guess: str, key: str) -> str:
    """Provides the emoji string for the result of a given guess"""
    # Parameters and defining variables
    assert len(guess) == len(key)
    index: int = 0
    result: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while index < len(key):
        if guess[index] == key[index]:
            result += GREEN_BOX
            index += 1
        else:
            if contains_char(key, guess[index]) == True:
                result += YELLOW_BOX
                index += 1
            else:
                result += WHITE_BOX
                index += 1
    return(result)

# Gets the proper length guess from the user
def input_guess(key_length: int) -> str:
    """Obtains a guess of the proper length from the user"""
    # Variable definition zone
    guess: str = ""

    guess = input(f"Enter a {key_length} character word: ")
    while len(guess) != key_length:
        guess = input(f"That wasn't {key_length} chars! Try again: ")
    return(guess)

# The loop for the main game
def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Variable definition zone
    attempt_counter: int = 1
    success: bool = False
    key: str = "codes"
    user_guess: str = ""

    while attempt_counter < 7 and success == False:
        print(f"=== Turn {attempt_counter}/6 ===")
        user_guess = input_guess(len(key))
        print(emojified(user_guess, key))
        if user_guess == key:
            print(f"You won in {attempt_counter}/6 turns!")
            success = True
        attempt_counter += 1
        if attempt_counter == 7:
            print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()