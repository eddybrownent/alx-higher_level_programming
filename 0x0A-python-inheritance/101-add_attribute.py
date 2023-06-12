#!/usr/bin/python3
"""
this module has a function that
adds a new attribute to an object if possible
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object id possible

    Args:
        obj(object): the obxject to add the attribute to
        attribute (str): the name of the attribute to add
        value (Any): the value of the attribute

    Raises:
        TypeError: if the object cant have a new attribute
    """

    if not hasattr(obj, '__dict__') and not hasattr(type(obj), '__sloats__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
