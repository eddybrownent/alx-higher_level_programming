#!/usr/bin/python3
"""
this module has a class that inherits(Rectarngle)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this class represents a square
    """
    def __init__(self, size):
        """
        Initialize a Square object

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is not a positive integer
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
