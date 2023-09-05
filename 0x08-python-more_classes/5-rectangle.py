#!/usr/bin/python3
"""
This module defines a Rectangle class that represents
rectangles and provides various operations on them.
"""


class Rectangle:
    """
    The Rectangle class represents a rectangle with a given width and height.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        area(): Calculate the area of the rectangle.
        perimeter(): Calculate the perimeter of the rectangle.
        __str__(): Return a string representation of the rectangle.
        __repr__(): Return a string that can be used to recreate the rectangle.
        __del__(): Destructor that prints a message when the object is deleted.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle object with a specified width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
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

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = ""
            for item in range(self.__height):
                result += "#" * self.__width + "\n"
        return result[:-1]

    def __repr__(self):
        """
        Return a string that can be used to recreate the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rectangle({self.__width},{self.__height})"

    def __del__(self):
        """
        Destructor that prints a message when the object is deleted.
        """
        print("Bye rectangle...")
