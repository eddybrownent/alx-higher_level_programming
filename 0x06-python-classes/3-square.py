#!/usr/bin/python3
"""defining a class square"""


class Square:
    """
    class that represents a square
    Attributes:
        __size (int): the size of the square (private)
    """

    def __init__(self, size=0):
        """
        Initializesa a new instance of the Square class.

        Args:
            size (int): the size of the square.

        Rises:
            TypeError: if the size is not an integer
            ValueError: if the size is negative
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        area = self.__size * self.__size

        return area
