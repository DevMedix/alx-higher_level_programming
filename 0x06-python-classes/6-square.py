#!/usr/bin/python3
"""a class Square that defines a square(object)"""

class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The side length of the square.
        position (tuple): The position of the square's\
        top-left corner as (x, y) coordinates.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square with a given size and position.

        Args:
            size (int, optional): The side length of the square (default is 0).
            position (tuple, optional): The position of the\
            top-left corner (default is (0, 0)).
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The side length of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new side length for the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the top-left corner as (x, y) coordinates.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position as (x, y) coordinates.

        Raises:
            TypeError: If the value is not a tuple of two integers.
            ValueError: If the coordinates are negative.
        """
        if (not isinstance(value, tuple)) or (len(value) != 2) or \
                (not isinstance(value[0], int)) or \
                (not isinstance(value[1], int)) or \
                (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print a representation of the square.

        The square is represented using '#' characters. The top-left \
        corner is positioned according to the 'position'
        attribute. If size is 0, an empty line is printed.
        """
        try:
            if self.__size == 0:
                print()
            else:
                for i in range(self.__position[1]):
                    print()
                for item in range(self.__size):
                    print(" " * self.__position[0] + "#" * self.__size)
        except TypeError:
            print("position must be a tuple of 2 positive integers")

        try:
            if self.__size == 0:
                return ""
            else:
                result = ""
                for i in range(self.__position[1]):
                    result += "\n"
                for item in range(self.__size):
                    result += " " * int(self.__position[0]) \
                        + "#" * self.__size + "\n"
            return result
        except TypeError:
            print("position must be a tuple of 2 positive integers")
