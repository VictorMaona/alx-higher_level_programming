#!/usr/bin/python3
# 2-matrix_divided.py
"""Establishes matrix division function."""


def matrix_divided(matrix, div):
    """Dividing a matrix components.

    Args:
        matrix (list): A list of lists containing ints or floats.
        div (int/float): Divisor.
    Raises:
        TypeError: If there are no numbers in the matrix.
        TypeError: if the matrix has rows with various sizes.
        TypeError: If div is not a float or int.
        ZeroDivisionError: div if it is 0.
    Returns:
        A fresh matrix displaying the division outcome.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
