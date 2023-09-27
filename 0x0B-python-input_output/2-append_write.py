#!/usr/bin/python3
"""
This module defines the function append_write
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8)
    and returns the number of characters added.

    Args:
        filename (str): name of file which the text should be appended.
        text (str): The string to append to the file.

    Returns:
        int: the number of characters added to the file
    """

    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
