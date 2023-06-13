#!/usr/bin/python3
"""
This module has a describes a class Student
"""


class Student:
    """
    Represents a student

    Atrributes:
        first_name (str): The first name of the student
        last_name (str): The last name of the student
        age (int): The age of the student

    Methods:
        to_json(): Retrieves a dictionary representation of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns:
            dict: The dictionary representation of the Student instance
        """

        return self.__dict__
