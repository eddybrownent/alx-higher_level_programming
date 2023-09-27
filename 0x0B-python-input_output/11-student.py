#!/usr/bin/python3
"""
This module describes a class Student
"""


class Student:
    """
    Represents a student

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    Methods:
        to_json(attrs=None): Retrieves a dictionary representation of a Student
        reload_from_json(json): Replaces attrs of the Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student intance

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve (optional).

        Returns:
            dict: The dictionary representation of the Student instance.
        """

        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a dict

        Args:
            json (dict): A dictionary containing attribute-value pairs.
        """

        for attr, value in json.items():
            setattr(self, attr, value)
