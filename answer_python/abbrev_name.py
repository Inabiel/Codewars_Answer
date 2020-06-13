"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.
"""


def abbrevName(name: str) -> str:
    a = name.split(" ")
    b = [i[0].upper() for i in a]
    return ".".join(b)
