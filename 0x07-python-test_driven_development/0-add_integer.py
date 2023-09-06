#!/usr/bin/python3
"""This module contains one function that add integers
"""


def add_integer(a, b=98):
    """
    This functions add two integers (a) and (b)
    """
    if isinstance(a, float) or isinstance(b, float):
        return int(a) + int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")

    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    if isinstance(a, int) or isinstance(b, int):
        return a + b

