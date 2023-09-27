#!/usr/bin/python3
"""defining  a Square class """


class Square:
    """
    This class represents a square.
    Attributes:
    _size (int): the size of the square (private)
    """
    def __init__(self, size):
        """
        initializes a new instance of the Square class
        Args:
        size (int): the size of the square.
        """
        self.__size = size
