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
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """
        Get a string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
        returns a string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        prints this message when a rectangle instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compares two Rectangles acording to area and returns the bigger one

        Args:
            rect_1 (Rectangle): the first Rectangle object
            rect_2 (Rectangle): the second Rectangle object

        Raises:
            TypeError: if either rect is not an instance of class Rectangle

        Returns:
            the bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        to return a new Rectangle instance with equal
        width and height
        """
        return Rectangle(size, size)
