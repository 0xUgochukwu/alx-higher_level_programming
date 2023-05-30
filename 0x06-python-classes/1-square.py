#!/usr/bin/python3
"""Definition of the Square class"""


class Square:
    """Represents a square object.

    Attributes:
        __size (int): The size of each side of the square.
    """

    def __init__(self, size):
        """Initializes a square with a given size.

        Args:
            size (int): The size of each side of the square.

        Returns:
            None
        """
        self.__size = size

