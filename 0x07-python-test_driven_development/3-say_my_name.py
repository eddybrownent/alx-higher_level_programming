#!/usr/bin/python3
"""
This module contains a function
that prints name
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints My name is <first name> <last name>

    Args:
        first_name (str): the first name
        last_name (str): the second name

    Raises:
        TypeError: if either the first_name and last name
                    is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))
