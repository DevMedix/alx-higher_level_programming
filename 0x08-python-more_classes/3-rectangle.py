#!/usr/bin/python3
"""
This module defines a Rectangle class that represents
rectangles and provides various operations on them.
"""


class Rectangle:
    """
    This class represents a rectangle with width
    and height attributes. It provides methods
    for calculating the area, perimeter, and
        string representation of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance with optional
        width and height parameters.

        :param width: The width of the rectangle (default is 0).
        :param height: The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        :return: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        :param value: The width value to set.
        :raise TypeError: If the value is not an integer.
        :raise ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        :return: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        :param value: The height value to set.
        :raise TypeError: If the value is not an integer.
        :raise ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        :return: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        :return: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Generate a string representation of the rectangle using '#' characters.

        :return: A string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = ""
            for item in range(self.__height):
                result += "#" * self.__width + "\n"
        return result[:-1]
