#!/usr/bin/python3
"""a class Square that defines a square(object)"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The side length of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a square with a given size.

        Args:
            size (int, optional): The side length of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")