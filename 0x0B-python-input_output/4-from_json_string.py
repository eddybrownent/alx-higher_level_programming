#!/usr/bin/python3
"""
This module defines the function from_json_string
"""
import json


def from_json_string(my_str):
    """
    Returns the object represented by JSON string

    Args:
        my_str (str): the JSON string to be converted

    Returns:
        object: The Python data structure represented by the JSON string
    """

    return json.loads(my_str)
