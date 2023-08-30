#!/usr/bin/python3
"""a class Square that defines a square(object)"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The side length of the square.
    """
    def __init__(self, size):
        self.__size = size


my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
