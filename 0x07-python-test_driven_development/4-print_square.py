#!/usr/bin/python3
"""
this modules has a function that
prints a square
"""


def print_square(size):
    """
    function to print a square with # symbol

    Args:
        size (int): trhis is the lengh of the square

    Raises:
        TypeError: if size is not an int
        ValueError: if size is less than zero
        TypeError: if size is float and less tahn zero
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    for i in range(0, size):
        for side in range(size):
            print('#', end='')
        print('')
