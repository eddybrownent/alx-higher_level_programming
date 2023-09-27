#!/usr/bin/python3
"""Defining a class MagicClass"""
import math


class MagicClass:
    """
    Represents a class that performs magic calcs on a cirle

    Attributes:
        __radius (float) the radius of the circle
    """

    def __init__(self, radius=0):
        """
        initializes a new instance of the MagicClass

        Args:
            radius (float): the radious of the circle
        Raises:
            TypeError: if the radious is not a float or int
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        calculates the area of the cirlce

        Returns:
        float: the area of the cirle
        """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
