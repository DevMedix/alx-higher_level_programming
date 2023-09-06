#!/usr/bin/python3
"""
This module contains print_square functions
it takes one parameter that accepts only integer
raises a TypeError and ValueError
"""


def print_square(size):
    """
    Print a square of '#' characters with the given size.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
