#!/usr/bin/python3
"""
this module has a function that
retursns the List of available
attributes and methods of an object
"""


def lookup(obj):
    """
    returns the list of attributes and methods of an object

    Args:
        obj (oject): the object who's methods and attributes are to be printed

    Return:
        list: the list of attributes and methods of an object
    """

    return dir(obj)
