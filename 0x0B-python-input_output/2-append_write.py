#!/usr/bin/python3

"""This module contains a function to read text files"""


def append_write(filename="", text=""):
    """ Appends text to a file and returns the number of characters added

    Args:
        filename (str): file to read from
        text (str): text to append
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
