#!/usr/bin/python3
"""
This module defines a function
append_after()
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts line of text after each line containing specific string in file.

    Args:
        filename (str): Name or path of the file.
        search_string (str): String to search for in each line of the file.
        new_string (str): text to be inserted after
            each line containing search string.
    """

    with open(filename, "r") as a_file:
        lines = a_file.readlines()

    with open(filename, "w") as a_file:
        for line in lines:
            a_file.write(line)
            if search_string in line:
                a_file.write(new_string + "\n")
