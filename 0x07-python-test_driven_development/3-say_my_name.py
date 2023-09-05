#!/usr/bin/python3
"""This module contains say_my_name(first_name, last_name="")
    the function prints My name is <first name> <last name>
    first_name and last_name must be strings otherwise, raise a TypeError
    exception with the message first_name must be a string or last_name
"""


def say_my_name(first_name, last_name=""):
    """ This function prints first name and last name
    Args:
        first_name (str): first name string
        second_name (str): second name string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
         raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))