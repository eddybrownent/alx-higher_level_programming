#!/usr/bin/python3
"""
This module has a function that
reads a text file(utf8) and prints it
to stdout
"""


def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout

    Args:
        filename (str): the name of the file to read (Default: "")
    """
    with open(filename, "r", encoding="utf-8") as a_file:
        content = a_file.read()
        print(content, end="")
