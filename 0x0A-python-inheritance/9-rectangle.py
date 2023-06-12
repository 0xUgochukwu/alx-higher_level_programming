#!/usr/bin/python3
"""
Square Module
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A Square"""

    def __init__(self, size):
        """ Instantiation of the square object """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)



    def area(self):
        """ Area Calculator """
        return self.__size ** 2

    def __str__(self):
        """ Informal string representation of the rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
