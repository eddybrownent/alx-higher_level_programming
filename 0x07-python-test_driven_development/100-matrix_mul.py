#!/usr/bin/python3
"""
Module has a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    To multiply two matrices and return the result

    Args:
        m_a (list): the first matrix a list of lists with integers or floats
        m_b (list): the second matrix a list of lists with integers or floats

    Raises:
        TypeError:  if m_a or m_b is not a list
                    if one element of the matrices is not an integer or float
                    if the rows of m_a or m_b are not of the same size

        ValueError: if the rows of m_a or m_b are not of the same size
    """

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    if m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(
            isinstance(element, (int, float))
            for row in m_a
            for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(
            isinstance(element, (int, float))
            for row in m_b
            for element in row):
        raise TypeError("m_b should contain only integers or floats")

    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")

    rows_a = len(m_a)
    col_a = len(m_a[0])
    rows_b = len(m_b)
    col_b = len(m_b[0])

    if col_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    m_result = [[0 for elements in range(col_b)] for elements in range(rows_a)]

    for i in range(rows_a):
        for j in range(col_b):
            for k in range(col_a):
                m_result[i][j] += m_a[i][k] * m_b[k][j]

    return m_result
