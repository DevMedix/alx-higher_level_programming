#!/usr/bin/python3
"""
This module defines a Rectangle class that represents
rectangles and provides various operations on them.
"""


class Rectangle:
    """
    A class to represent rectangles.

    Attributes:
        number_of_instances (int): A class attribute to keep
        track of the number of Rectangle instances created.

    Methods:
        __init__(self, width=0, height=0): Initializes a
        Rectangle instance with the specified width and height.
        width (property): Gets the width of the rectangle.
        width (setter): Sets the width of the rectangle
        with type and value checks.
        height (property): Gets the height of the rectangle.
        height (setter): Sets the height of the
        rectangle with type and value checks.
        area(self): Calculates and returns the area of the rectangle.
        perimeter(self): Calculates and returns the perimeter of the rectangle.
        __str__(self): Returns a string representation
        of the rectangle using "#" characters.
        __repr__(self): Returns a string representation
        of the rectangle suitable for reproduction.
        __del__(self): Decrements the number_of_instances when
        a Rectangle instance is deleted.

    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with the specified width and height.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with type and value checks.

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
        Gets the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with type and value checks.

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
        Calculates and returns the area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Returns a string representation of the rectangle using "#" characters.
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
        Returns a string representation of the rectangle
        suitable for reproduction.
        """
        return f"Rectangle({self.__width},{self.__height})"

    def __del__(self):
        """
        Decrements the number_of_instances when a Rectangle
        instance is deleted.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
