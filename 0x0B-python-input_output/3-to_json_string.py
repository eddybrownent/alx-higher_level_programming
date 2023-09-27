#!/usr/bin/python3
"""
This module defines the function to_json_string
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj: the object to be converted to JSON

    Returns:
        str: the JSON representation of the object
    """

    return json.dumps(my_obj)
