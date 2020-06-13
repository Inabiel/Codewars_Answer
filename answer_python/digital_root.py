"""
    Sum all the digit until sigle-number digit is produced.
"""


def digital_root(n: int) -> int:
    return (n - 1) % 9 + 1 if n else 0  # ...
