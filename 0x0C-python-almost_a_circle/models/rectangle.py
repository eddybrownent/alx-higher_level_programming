#!/usr/bin/python3
"""
This module defines a class Rectangle
that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x-coordinate of the rectangle's position
            y (int, optional): y-coordinate of the rectangle's position
            id (int, optional): identifier for the instance
                it is passed to the super class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter for the width

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width

        Args:
            value (int): the width of the rectangle

        Raises:
            Typeerror: if the value is not an integer
            ValueError: if the value is under or equals 0
        """

        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter for the height

        Returns:
            int: the height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height

        Args:
            value(int): the height of the rectangle

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is under or equals 0
        """

        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x-coordinate attribute

        Returns:
            int: the x-coordinate of the rectangle's position
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x-coordinate attribute

        Args:
            value (int): x-coordinate of the rectangle's position

        Raises:
            TypeError: if the value is not an integer
            ValueError: if value is < then 0
        """

        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Getter for the y-coordinate attribute

        Returns:
            int: The y-coordinate of the rectangle's position
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y-coordinate attribute

        Args:
            value (int): The y-coordinate of the rectangle's position

        Raises:
            ValueError: if the value is less than 0
            TypeError: if the value is not an integer
        """

        if not type(value) is int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of a Rectangle intance

        Returns:
            int: the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(' ', end="")
            for _ in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """
        Returns a custom string representation of the Rectangle object
        """
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
                )
    
    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
