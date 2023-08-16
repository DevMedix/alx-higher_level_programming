#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    else:
        squared = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
        return squared
