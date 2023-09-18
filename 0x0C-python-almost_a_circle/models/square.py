#!/usr/bin/python3
"""This module has Square class only"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.
            x (int): The X-coordinate of the
            square's top-left corner (default is 0).
            y (int): The Y-coordinate of the square's
            top-left corner (default is 0).
            id (int): An optional identifier for the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square, ensuring it's a positive integer.

        Args:
            value (int): The new size value to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the square's attributes
        using positional or keyword arguments.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments that can
        """
        if not args:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
        else:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

    def to_dictionary(self):
        """Returns a dictionary representation of the square's attributes."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
