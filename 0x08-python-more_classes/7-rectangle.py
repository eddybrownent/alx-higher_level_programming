#!/usr/bin/python3
"""
module tha defines class Rectangle
"""


class Rectangle:
    """
    class that represents  a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
        Get a string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
            str(self.print_symbol) * self.__width for i in range(self.__height)
        )

    def __repr__(self):
        """
        returns a string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """"
        prints this message when a rectangle instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
