#!/usr/bin/python3
"""This module has Rectangle class only"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle with a specified width, height,
    position (x, y), and an optional ID.
    Inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        :param width: The width of the rectangle.
        :type width: int
        :param height: The height of the rectangle.
        :type height: int
        :param x: The x-coordinate of the rectangle's position.
        :type x: int
        :param y: The y-coordinate of the rectangle's position.
        :type y: int
        :param id: An optional ID for the rectangle.
        :type id: int
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.

        :return: The width of the rectangle.
        :rtype: int
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        :param value: The new width value.
        :type value: int
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        :return: The height of the rectangle.
        :rtype: int
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        :param value: The new height value.
        :type value: int
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get the x-coordinate of the rectangle's position.

        :return: The x-coordinate of the rectangle's position.
        :rtype: int
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle's position.

        :param value: The new x-coordinate value.
        :type value: int
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the rectangle's position.

        :return: The y-coordinate of the rectangle's position.
        :rtype: int
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle's position.

        :param value: The new y-coordinate value.
        :type value: int
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        :return: The area of the rectangle.
        :rtype: int
        """
        return self.__height * self.__width

    def display(self):
        """
        Display the rectangle by printing its representation to the console.
        """
        for item in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Get a string representation of the rectangle.

        :return: A string representation of the rectangle.
        :rtype: str
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle using either positional
        arguments or keyword arguments.

        :param args: Positional arguments in
            the order: (id, width, height, x, y).
        :type args: tuple
        :param kwargs: Keyword arguments for
            updating individual attributes (id, width, height, x, y).
        :type kwargs: dict
        """
        if not args:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value
        else:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]

    def to_dictionary(self):
        """
        Convert the rectangle object to a dictionary representation.

        :return: A dictionary containing the rectangle's attributes.
        :rtype: dict
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y}
