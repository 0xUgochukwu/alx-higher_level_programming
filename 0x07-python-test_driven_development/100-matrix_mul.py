#!/usr/bin/python3
"""
Multiply Matrices
"""


def matrix_mul(m_a, m_b):
    """
        Function to multiply matrices
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

    my_arr = []
    for i in range(len(m_a)):
        temp_arr = []
        for j in range(len(m_b[0])):
            value = 0
            for k in range(len(m_a[0])):
                value += m_a[i][k] * m_b[k][j]
            temp_arr.append(value)
        my_arr.append(temp_arr)

    return my_arr
