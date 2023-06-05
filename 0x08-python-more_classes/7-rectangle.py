#!/usr/bin/python3
"""Defines a class Square"""


class Rectangle:
    """A Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializer of the class """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ Detect instance deletion """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """ Calculates the area of the rectangle """

        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of the rectangle """

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the informal string representaion
        of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""

        for _ in range(self.__height):
            rectangle += self.print_symbol * self.__width + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """
        Returns a string representation
        of the rectangle that can be used to recreate a new instance.
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
