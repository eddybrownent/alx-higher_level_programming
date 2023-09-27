#!/usr/bin/python3
"""
This module defines a class Square
that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a square object

        Args:
            size (int): size of the square ie width and height
            x (int): x-coordinate of the top-left corner of the square
            y (int): y-coordinate of the top-left corner of the square
            id (int): identifier of the square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Returns a string representation of the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Get the size of the square

        Returns:
            int: the size of the square(both width and height)
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Args:
            value (int): the size value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square

        Args:
            *args: Variable number of positional arguments
            **kwargs: Key/value arguments ie attributes and their values

        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

        if args:
            # *args exists and is not empty skip **kwargs
            return
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        """
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
