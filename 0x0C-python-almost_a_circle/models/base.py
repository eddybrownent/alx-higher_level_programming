#!/usr/bin/python3
"""
This module defines a class Base
"""
import json


class Base:
    """
    Base class for models

    Private Attributes:
        __nb_objects (int): count of instances created from the class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the class Base

        Args:
            id (int): the identifier for the instance (optional)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation

        Args:
            list_dictionaries(List[dict]): list of dicts representing data
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes a JSOn string representation of list objs to a file

        Args:
            list_objs (list): list of instance that inherit fron base
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            json_string = "[]"
        else:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(dict_list)

        with open(filename, "w") as my_file:
            my_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a Json string to a list of python dicts

        Args:
            json_string (str): list of dictionaries in JSON format

        Returns:
            List: the list represented by the JSON string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a instance of the class with attrs set from a dict

        Args:
            cls (type): the class
            **dictionary: a dictionary containing attribute-value pairs.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # dummy Rectangle instace default attr
        elif cls.__name__ == "Square":
            dummy = cls(1)  # dummy Square instance default attr

        # upaditng the instance with the provided atrr and value
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as my_file:
                json_data = my_file.read()
                data = cls.from_json_string(json_data)
                instances = [cls.create(**atrributes) for atrributes in data]
                return instances
        except IOError:
            return []
