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
        """
        self.__size = size

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

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Compare two squares for equality based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare two squares for inequality based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compare if one square has a greater area than the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of this square is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare if one square has a greater or equal area than the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of this square is \
            greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compare if one square has a smaller area than the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of this square is smaller, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare if one square has a smaller or equal area than the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of this square \
            is smaller or equal, False otherwise.
        """
        return self.area() <= other.area()
