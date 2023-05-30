#!/usr/bin/python3
"""Defines the Square class."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The length of a side of the square.
    """

    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size (int, optional): The length of a side of the square.
                Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None
        """
        try:
            if int(size) < 0:
                raise ValueError("size must be >= 0")
            self.__size = int(size)
        except (TypeError, ValueError):
            raise TypeError("size must be an integer")
