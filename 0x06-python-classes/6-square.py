#!/usr/bin/python3
"""defining a square"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of the square (private).
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The position value to set.

        Raises:
            TypeError: If the value != tuple or doesn't contain 2 positive ints
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if not isinstance(i, int) or i < 0]) != 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def posi_print(self):
        """To return the position in spaces"""
        posi = ''
        if self.size == 0:
            return '\n'
        for i in range(self.position[1]):
            posi += '\n'
        for x in range(self.size):
            for j in range(self.position[0]):
                posi += ' '
            for n in range(self.size):
                posi += '#'
            posi += '\n'
        return posi

    def my_print(self):
        """
        Print the square in position with the character '#'.
        """
        print(self.posi_print(), end="")
