"""A Wordle variation with one chance to guess the word."""

__Author__ = "730295419"

from xml.dom.expatbuilder import FragmentBuilderNS


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
answer: str = "python"
guess: str = ""
index: int = 0
yellow_index: int = 0
result: str = ""

guess = input("What is your 6-letter guess? ")

while len(guess) != 6:
    guess = input("That was not 6 letters! Try again: ")

while index < len(answer):
    yellow_index = 0
    if guess[index] == answer[index]:
        result = result + GREEN_BOX
    else:
        while yellow_index < len(answer):
            if guess[index] == answer[yellow_index]:
                result = result + YELLOW_BOX
            yellow_index = yellow_index + 1
            # print(f"that's {yellow_index} for {guess[index]}!") # To make sure the loop is working properly for each letter
    if result[index] == "":
        result = result + WHITE_BOX
    print(result) # To print results per letter for troubleshooting.
    index = index + 1

print(result)

if guess != answer:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")