#!/usr/bin/python3
"""
This module defines a function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text fiole using a JASON respresentaion

    Args:
        my_obj: The object to be serialized to JSON and written to the file.
        filename (str): name of the file to which the JSON rep will be written.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
