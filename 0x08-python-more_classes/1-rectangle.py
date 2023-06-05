#!/usr/bin/python3
"""Defines a class Square"""


class Rectangle:
    """A Rectangle class"""

    def __init__(self, width, height):
        """ Initializer of the class """

        self.width = width
        self.height = height


    @property
    def width(self):
        """ Getter for the width property """

        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Getter for height property """

        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
