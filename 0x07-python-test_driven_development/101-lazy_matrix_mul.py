#!/usr/bin/python3
import numpy as np
"""
Lazy Matrix Multiply

"""


def lazy_matrix_mul(m_a, m_b):
    """
        Function that mutiplies Matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not (all(isinstance(j, list) for j in m_a)):
        raise TypeError("m_a must be a list of lists")

    if not (all(isinstance(j, list) for j in m_b)):
        raise TypeError("m_b must be a list of lists")

    if m_a == [[]] or m_a == []:
        raise ValueError("m_a can't be empty")

    if m_b == [[]] or m_b == []:
        raise ValueError("m_b can't be empty")

    if not all(all(type(x) in [int, float] for x in j) for j in m_a):
        raise TypeError("m_a should contain only integers or floats")

    if not all(all(type(x) in [int, float] for x in j) for j in m_b):
        raise TypeError("m_b should contain only integers or floats")

    for x in range(len(m_a)):
        if x < len(m_a) - 1:
            if not (len(m_a[x]) == len(m_a[x + 1])):
                raise TypeError("each row of m_a must be of the same size")

    for x in range(len(m_b)):
        if x < len(m_b) - 1:
            if not (len(m_b[x]) == len(m_b[x + 1])):
                raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) is not len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    np_m_a = np.array(m_a)
    np_m_b = np.array(m_b)

    return (np_m_a @ np_m_b).tolist()
