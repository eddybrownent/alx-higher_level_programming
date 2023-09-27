#!/usr/bin/python3
"""
This module defines a class Base
"""
import json
import csv
import turtle
import time


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
        returns a list of instances
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize a list of objects to CSV format
        and save it to a file
        Args:
            list_objs (list): A list of instances
        """
        with open(cls.__name__ + ".csv", 'w', newline='') as my_file:
            if list_objs is None or list_objs == []:
                my_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(my_file, fieldnames=fieldnames)
                for objct in list_objs:
                    writer.writerow(objct.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes CSV format from a file

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as my_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                dict_reader = csv.DictReader(my_file, fieldnames=fieldnames)
                parsed_dicts = [dict([key, int(value)]
                                     for key, value in row.items())
                                for row in dict_reader]

                return [cls.create(**parsed_dict)
                        for parsed_dict in parsed_dicts]

        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        opens a window and draws all the Rectangles and Squares

        Args:
            list_rectangles: all the Rectangles
            list_squares: all the squares
        """

        # creating a turtle instance
        my_turtle = turtle.Turtle()
        my_turtle.pensize(5)
        my_turtle.shape("turtle")

        my_turtle.color("black")

        # draw reactangles
        for rectangle in list_rectangles:
            my_turtle.showturtle()
            my_turtle.penup()
            my_turtle.goto(rectangle.x, rectangle.y)
            my_turtle.pendown()
            for i in range(2):
                my_turtle.forward(rectangle.width)
                my_turtle.left(90)
                my_turtle.forward(rectangle.height)
                my_turtle.left(90)

        my_turtle.color("red")

        # draw squares
        for square in list_squares:
            my_turtle.showturtle()
            my_turtle.penup()
            my_turtle.goto(square.x, square.y)
            my_turtle.pendown()
            for i in range(2):
                my_turtle.forward(square.width)
                my_turtle.left(90)
                my_turtle.forward(square.height)
                my_turtle.left(90)
            my_turtle.hideturtle()

        time.sleep(7)
