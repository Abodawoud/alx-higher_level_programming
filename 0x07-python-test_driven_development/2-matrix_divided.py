#!/usr/bin/python3
"""matrix_divided module"""


def matrix_divided(matrix, div):
    """Checks for matrix & divisor"""

    if not isinstance(matrix, list) or len(matrix) == 0 or matrix is None:
        raise TypeError("matrix must \
be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)) or div is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div == float('inf'):
        return (0.0)
    if div == -float('inf'):
        return (-0.0)
    if div != div:
        raise TypeError("div must be a number")

    new_matrix = []

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
            if (elem / div) == float("inf"):
                new_row.append(float("inf"))
            elif (elem / div) == -float("inf"):
                new_row.append(-float("inf"))
            else:
                new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)
    return (new_matrix)
