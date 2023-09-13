#!/usr/bin/python3

"""This module contains a function to read text files"""


def write_file(filename="", text=""):
    """ Writes to a file and returns the number of characters written

    Args:
        filename (str): file to read from
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
