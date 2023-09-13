#!/usr/bin/python3

"""This module contains a function to read text files"""


def read_file(filename=""):
    """ Reads a file and prints to stdout

    Args:
        filename (str): file to read from
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(read_data, end='')
