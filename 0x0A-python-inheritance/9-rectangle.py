#!/usr/bin/python3
"""
Rectangle Module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle"""

    def __init__(self, width, height):
        """ Instantiation of the rectangle object """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Area Calculator """
        return self.__width * self.__height

    def __str__(self):
        """ Informal string representation of the rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
