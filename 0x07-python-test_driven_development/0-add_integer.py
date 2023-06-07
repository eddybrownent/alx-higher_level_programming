#!/usr/bin/python3
"""
This module has one function
adding two integers
and returns the result
"""


def add_integer(a, b=98):
    """
    Returns the sums of two integers or floats
    and returns as integers

    Args:
        a: First argument
        b: the second argument

    Return:
        the sum of the two arguments

    Raises:
        TypeError: if either of the arguments are not a float or an int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return (result)
