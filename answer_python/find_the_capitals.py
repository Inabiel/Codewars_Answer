"""
    Write a method that takes a sequence of objects with two keys each: country or state, and capital. Keys may be symbols or strings

    The method should return an array of sentences declaring the state or country and its capital.
"""


def capital(capitals: dict) -> str:
    return [
        f"The capital of {c.get('state') or c['country']} is {c['capital']}"
        for c in capitals
    ]
