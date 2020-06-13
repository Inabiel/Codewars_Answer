"""
    Sum of all the number between the minimum and maximum number including the number itself.
"""


def get_sum(a: int, b: int) -> int:
    minim = min(a, b)
    maxi = max(a, b)
    return (maxi - minim + 1) * (minim + maxi) / 2
