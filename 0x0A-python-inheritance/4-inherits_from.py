#!/usr/bin/python3
"""
checks if an object is an instance of a class
that inherited (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """
    checks if the object's type is a subclass of the specified class,

    Args:
        obj (object): the object to be checked
        a_class (class): the class to check in

    Return:
        bool: True if the object is an instance of a class else false
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
