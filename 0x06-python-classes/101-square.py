#!/usr/bin/python3
"""defining a class Square"""


class Square:
    """
    class that defines a square

    Attribute:
        __size (int): the size of the square (private)
        __position (tuple): the position of the square (private)
    """
    def __str__(self):
        """
        Return a string representation of the square

        Returns:
            str: a string representation of the square
        """
        return self.posi_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """
        inintializes a squre instance

        Args:
            size (int): the size of the square
            position (tuple): the position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        get the size of the square

        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size of the square

        Args:
            value (int): the size of value to set
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is negative
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0"')
        self.__size = value

    @property
    def position(self):
        """
        retrives the position of the square

        Returns:
            tuple: the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        set the position of the square

        Args:
            value (tuple): the position to be st

        Raises:
            TypeError; if value != tuole or dsnt contain 2 positive ints
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        claculate the are of the square

        Returns:
            int: the are of the square
        """
        return self.__size * self.__size

    def posi_print(self):
        """
        Return the printed square with position
        """
        posi = ""
        if self.size == 0:
            return '\n'
        posi += '\n' * self.position[1]
        for i in range(self.size):
            posi += " " * self.position[0] + '#' * self.size + "\n"
        return posi

    def my_print(self):
        """
        print the square using '#' character
        """
        print(self.posi_print(), end="")
