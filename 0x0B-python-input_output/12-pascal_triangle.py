#!/usr/bin/python3
"""
this module defines a function
pascal_triangle(n)
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows

    Args:
        n (int): the number of rows in pascal's triangle

    Returns:
        list: A list of list representing pascal's triangle
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
