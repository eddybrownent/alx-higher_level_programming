#!/usr/bin/python3
"""
checks if an object is an instance of a class
that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """
    checks if the object's type is a subclass of the specified class,
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
