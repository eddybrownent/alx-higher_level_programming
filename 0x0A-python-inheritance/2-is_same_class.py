#!/usr/bin/python3
"""
this module has a function that returns
true if the object is an instance of the
specified class otherwise false
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is an instance else False

    Args:
        obj (object): the object to be checked
        a_class (class): the class to check in

    Return:
        bool: True if the obj is an instance else False
    """
    return type(obj) is a_class
