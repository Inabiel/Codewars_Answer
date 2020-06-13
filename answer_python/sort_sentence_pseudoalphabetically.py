"""
    Sort sentence pseudo-alphabetically, from lowercase to Uppercase
"""
import re


def pseudo_sort(st: str):
    lower = []
    upper = []
    a = re.sub("[^A-Za-z0-9]+", " ", st).split()
    for i in a:
        if i.islower():
            lower.append(i)
        else:
            upper.append(i)
    return " ".join(sorted(lower) + sorted(upper, reverse=True))
