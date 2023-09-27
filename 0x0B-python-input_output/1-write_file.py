#!/usr/bin/python3
"""
This module contains a function that
writes a string to a text file and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file utf-8 an returns chr written

    Args:
        filename (str): the name of the file file to write (Default: "")
        text (str): the string to to write (Default: "")

    Returns:
        int: The number of characters written to the file
    """

    with open(filename, "w", encoding="utf-8") as a_file:
        a_file.write(text)

        return len(text)
