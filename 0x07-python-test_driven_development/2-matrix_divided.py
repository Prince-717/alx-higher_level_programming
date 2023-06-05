#!/usr/bin/python3
"""

Function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """ A Function that divides the integer/float numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: When the elements of the matrix aren't lists
                   When the elemetns of the lists aren't integers/floats
                   When div is not an integer/float number
                   When the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero


    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    message_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(message_type)

    length = 0
    msg_size = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(message_type)

        if length != 0 and len(elements) != length:
            raise TypeError(msg_size)

        for number in elements:
            if not type(number) in (int, float):
                raise TypeError(message_type)

        length = len(elements)

    new_matrix = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (new_matrix)
