#!/usr/bin/python3
"""
module tha defines class Rectangle
"""


class Rectangle:
    """
    class that represents  a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initializing a class Rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """to retrive the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set the width attribute"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """to retive the attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set the height attribute"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        to get the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        To get the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0

        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """
        return a string repreentaion of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ''
        for colum in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if colum < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
        Get a string representation of the rectangle object
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """"
        prints this message when a rectangle instance is deleted
        """
        print("Bye rectangle...")
