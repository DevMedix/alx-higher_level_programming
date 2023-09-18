#!/usr/bin/python3
"""This module has Base class only"""
import json


class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with an optional 'id' parameter.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON-formatted string representing the list of dictionaries.

        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file named after the class.

        Args:
            list_objs (list): A list of objects to be saved to the file.

        """

        filename = cls.__name__+".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                json_string = cls.to_json_string([obj.to_dictionary()
                                                 for obj in list_objs])
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON-formatted string to a list of dictionaries.

        Args:
            json_string (str): A JSON-formatted string.

        Returns:
            list: A list of dictionaries.

        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of a class using a dictionary of attributes.

        This method is used to create instances of either the
        'Rectangle' or 'Square' class based on the
        class name.

        Args:
            dictionary (dict): A dictionary containing
                                attributes for the new instance.

        Returns:
            obj: An instance of the class with the specified attributes.

        Raises:
            ValueError: If the class name is not 'Rectangle' or 'Square'.

        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        try:
            filename = str(cls.__name__) + ".json"
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
