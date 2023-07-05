#!/usr/bin/python3
"""print_square module"""


def print_square(size=None):
    """Print square"""

    if (not isinstance(size, int)) or size is None:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
