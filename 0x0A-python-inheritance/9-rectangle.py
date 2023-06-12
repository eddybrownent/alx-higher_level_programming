#!/usr/bin/pyrhon3
"""
this module contains a class Rectangle
that inherits BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle
    """

    def __init__(self, width, height):
        """
        initialize a Rectangle object

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle

        Raises:
            TypeError: if either the width or height is not an Integer
            ValueError: if either the width or height is <= 0
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def __str__(self):
        """
        To Return a string representing a rectangle

        Returns:
            str: a string in the format [Rectangle] <width>/<height>
        """
        return f"[Rectangle], {self.__width}/{self.__height}"

    def area(self):
        """
        calculates the area of the rectangle

        Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height
