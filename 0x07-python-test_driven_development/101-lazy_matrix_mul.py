#!/usr/bin/python3.5
"""

Module composed by a function that multiplies 2 matrices

"""
import numpy as namp


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication


    """
    result = namp.matmul(m_a, m_b)

    return (result)
