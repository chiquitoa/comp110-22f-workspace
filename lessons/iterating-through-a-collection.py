"""Example of looping through all characters in a string."""

__Author__ = "Andre Chiquito"

user_string: str = input("Give me a string without using a comma! : ")

# The variable i is a common computer variable name
# in programming. i is short for iteration
i: int = 0

while i < len(user_string):
    if user_string[i] == ",":
        print("Dawg. You had one job. Try again.")
        exit()
    i = i + 1

print("You're good to go!")