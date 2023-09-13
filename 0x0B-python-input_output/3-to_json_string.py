#!/usr/bin/python3
import json

"""This module contains a function to read text files"""


def to_json_string(my_obj):
    """ a function that returns the JSON representation of an object (string)

    Args:
        my_obj (str): object string
    """
    return json.dumps(my_obj)
