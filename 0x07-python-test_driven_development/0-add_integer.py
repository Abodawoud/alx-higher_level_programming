#!/usr/bin/python3
"""add ingeger module"""


def add_integer(a, b=98):
    """Returns an integer: the addition of int(a) and int(b)
    Arges:
        a: int or float
        b: int or float
    """
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")
    if type(a) not in [int, float] or a is None:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if a == float("inf"):
        return (float("inf"))
    if a == -float("inf"):
        return (-float("inf"))
    if b == float("inf"):
        return (float("inf"))
    if b == -float("inf"):
        return (-float("inf"))
    return (int(a) + int(b))
