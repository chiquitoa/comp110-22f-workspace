"""Helper functions imported elsewhere."""

# def merge(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
#     """Merge two dictionaries."""
#     result: dict[str, int] = {}
#     for key in a:
#         result[key] = a[key]
#     for key in b:
#         result[key] = b[key]
#     return result

# game0: dict[str, int] = {"KJ": 0, "ML": 1}
# game1: dict[str, int] = {"ML": 2, "EW": 3}
# merged: dict[str, int] = merge(game0, game1)
# print(merged)

# def zip(a: list[str], b: list[str]) -> dict[str, str]:
#     assert len(a) == len(b)
#     dictionary: dict[str, str] = {}
#     for x in a:
#         dictionary += {[a[x]]: [b[x]]}
#     print(dictionary)
#     return(dictionary)

a: list[str] = ["farts", "are", "great"]
b: list[str] = ["but", "I", "amn't"]
dictionary: dict[str, str] = {}
for x in range(0,len(a)):
    dictionary[a[x]] = [b[x]]
print(dictionary)