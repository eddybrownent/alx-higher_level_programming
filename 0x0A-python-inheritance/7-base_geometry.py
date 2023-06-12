#!/usr/bin/pyhon3
"""
this module defines a class BaseGeometry
"""


class BaseGeometry:
    """
    """
    def area(self):
        """
        calculate the area

        Raises:
            Exception: This method is not implemented in the base class
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the value is an integer greater than 0

        Args:
            name (str): the name of the value thats to be validated
            value (int): the value to validate

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
