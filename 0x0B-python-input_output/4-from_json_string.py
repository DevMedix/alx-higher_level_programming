#!/usr/bin/python3
import json

"""This module contains a function to read text files"""


def from_json_string(my_str):
    """ a function that returns the JSON representation of an object (string)

    Args:
        my_str (str): object string
    """
    data = json.loads(my_str)
    return data
