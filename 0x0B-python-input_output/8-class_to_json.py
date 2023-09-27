#!/usr/bin/python3
"""
This module describe a function class_to_json
"""


def class_to_json(obj):
    """
    Returns the dictinary description with a simple data
    structure for JSON serialization of an object

    Args:
        obj: An instance of a class

    Returns:
        dict: dictionary representation ofthe object with simple data structure
    """

    return obj.__dict__
