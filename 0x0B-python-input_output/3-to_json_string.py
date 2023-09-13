#!/usr/bin/python3

"""This module contains a function to read text files"""
import json


def to_json_string(my_obj):
    """ a function that returns the JSON representation of an object (string)

    Args:
        my_obj (str): object string
    """
    data = json.dumps(my_obj)
    return data
