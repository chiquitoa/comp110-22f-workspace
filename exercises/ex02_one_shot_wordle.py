"""A Wordle variation with one chance to guess the word."""

__Author__ = "730295419"

from xml.dom.expatbuilder import FragmentBuilderNS

# Define variables and set them up in a neautral state where necessary
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
answer: str = "python"
guess: str = ""
index: int = 0
yellow_index: int = 0
yellow_presence: bool = False
green_presence: bool = False
result: str = ""

# "What is your quest?" Just kidding. Finding out what their guess is.
guess = input(f"What is your {len(answer)}-letter guess? ")

# Putting people down when they try to find a shortcut
while len(guess) != len(answer):
    guess = input(f"That was not {len(answer)} letters! Try again: ")

# A loop to go through and test each letter sequentially
while index < len(answer):

    # Resets variables after the previous letter is done being evaluated
    yellow_index = 0
    yellow_presence = False
    green_presence = False

    # Tests whether the letter should be green
    if guess[index] == answer[index]:
        green_presence = True

    # Tests whether the letter should be yellow
    else:

        # Compares each letter in the answer to the current letter in the guess
        while yellow_presence == False and yellow_index < len(answer):
            if guess[index] == answer[yellow_index]:
                yellow_presence = True
                yellow_index = yellow_index + 1
            else:
                yellow_index = yellow_index + 1

    # Tests each variable denoting presence of each color to determine what color that letter in the guess should be
    if yellow_presence == True:
        result = result + YELLOW_BOX
    if green_presence == True:
        result = result + GREEN_BOX
    if yellow_presence == False and green_presence == False:
        result = result + WHITE_BOX

    # print(result) # To print results per letter for troubleshooting.
    index = index + 1

print(result)

if guess != answer:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")