#!/usr/bin/python3
"""
this module has a class MyInt
that inherits(int)
and inverts the equal and not-equal
operator
"""


class MyInt(int):
    """
    a class that represents a rebel integer
    """
    def __ne__(self, value):
        """
        inverted inequality operator

        Args:
            Value(int): object to compare with

        Returns:
            bool: True if its equal else False
        """
        return int(self) == value

    def __eq__(self, value):
        """
        inverted equality operator

        Args:
            value (int): the object to compare with

        Return:
            bool: False if its equal else True
        """
        return int(self) != value
