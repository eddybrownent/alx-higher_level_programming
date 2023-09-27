#!/usr/bin/python3
"""
this module has a function that returns
True  if the object is an instance of a
specified class or any of its subclasses.
else False
"""


def is_kind_of_class(obj, a_class):
    """
    checks if an object is an instance of a
    specified class or any of its subclasses

    Args:
        obj (object): the object to check
        a_class (class): the class to check in

    Return:
        bool: True if its an instance else False
    """
    return isinstance(obj, a_class)
