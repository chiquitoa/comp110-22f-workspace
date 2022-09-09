"""Tracing Loops Practice Question."""

i: int = int(input("Give a # > 0: "))
s: str = ""

while i > 0:
    s += "h"
    h: int = 0
    while h < i:
        s += "e"
        h += 1
    i -= 1

print(s)