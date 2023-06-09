#!/usr/bin/python3
"""
This module has a function that
multiplies two matrices using Numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy and returns the result

    Args:
        m_a (list): The first matrix a list of lists with integers or floats
        m_b (list): The second matrix a list of lists with integers or floats

    Returns:
        List: the result matrix list of lists
    """
    result = (np.matmul(m_a, m_b))

    return result
