#!/usr/bin/python3
"""
This module contains matrix_divided function
it takes 2 parameters matrix and div
raises a TypeError and ZeroDivisionError
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a specified divisor.
    """
    if not all(isinstance(row, list) and all(isinstance(val, (int, float)) \
        for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(val / div, 2) for val in row] for row in matrix]

    return result
