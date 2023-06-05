#!/usr/bin/python3
"""

Python module composed by a function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication

    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a each_lists
        ValueError: if m_a or m_b are empty
        TypeError: if the each_lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied


    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elements in m_a:
        if not isinstance(elements, list):
            raise TypeError("m_a must be a list of each_lists")

    for elements in m_b:
        if not isinstance(elements, list):
            raise TypeError("m_b must be a list of each_lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for each_lists in m_a:
        for elements in each_lists:
            if not type(elements) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for each_lists in m_b:
        for elements in each_lists:
            if not type(elements) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    list_length = 0

    for elements in m_a:
        if list_length != 0 and list_length != len(elements):
            raise TypeError("each row of m_a must be of the same size")
        list_length = len(elements)

    list_length = 0

    for elements in m_b:
        if list_length != 0 and list_length != len(elements):
            raise TypeError("each row of m_b must be of the same size")
        list_length = len(elements)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    index1 = 0

    for a in m_a:
        result2 = []
        index2 = 0
        number = 0
        while (index2 < len(m_b[0])):
            number += a[index1] * m_b[index1][index2]
            if index1 == len(m_b) - 1:
                index1 = 0
                index2 += 1
                result2.append(number)
                number = 0
            else:
                index1 += 1
        result.append(result2)

    return result
