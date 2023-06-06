#!/usr/bin/python3
"""
Divide a matrix
"""


def matrix_divided(matrix, div):
    """
        Function that divides all integers in a list
        by a divisor
        It validates the input before division
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not (all(all(type(x) in [int, float] for x in j)
            for j in matrix) and all(isinstance(j, list) for j in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for x in range(len(matrix)):
        if x < len(matrix) - 1:
            if not (len(matrix[x]) == len(matrix[x + 1])):
                raise TypeError(
                    "Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or type(div) is bool:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map((lambda x: round(x / div, 2)), sub_list))
            for sub_list in matrix]
