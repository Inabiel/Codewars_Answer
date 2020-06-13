"""
    Returning the last d digit of n integer as a list.
"""


def solution(n: int, d: int) -> list:
    lis = [int(i) for i in str(n)]
    res = lis[-d:]
    if d <= 0:
        return []
    else:
        return res
