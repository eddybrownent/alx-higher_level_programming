#!/usr/bin/python3
"""defining a class Suare"""


class Square:
    """
    This class represents a square

    Attributes:
        __size (int): the size of the square (private)
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class

        Args:
            size (int): the size of the square

        Riases:
            TypeError: if the size is not an integer
            ValueError: if the size is negative
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """get the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculates  the area of the square
        Returns:
            int: the size of the square
        """

        return (self.__size * self.__size)

    def my_print(self):
        """
        prints the square in with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
