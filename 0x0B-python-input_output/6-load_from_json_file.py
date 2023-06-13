#!/usr/bin/python3
"""
This module defines the function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    creats an oject from a JSON file

    Args:
        filename: The name of the JSON file

    Returns:
        object: the object created from the JSON file
    """
    with open(filename, "r", encoding="utf-8") as a_file:
        return json.load(a_file)
