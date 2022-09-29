"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    for key in items:
        if str(key) in frequencies:
            frequencies[str(key)] += 1
        else:
            frequencies[str(key)] = 1
    return frequencies
