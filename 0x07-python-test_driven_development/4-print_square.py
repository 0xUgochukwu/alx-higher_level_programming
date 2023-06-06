#!/usr/bin/python3
"""
Print Square
"""


def print_square(size):
    """
        Function to print a square
    """

    if type(size) is not int or \
            (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if not (size >= 0):
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
    # this works too
    # [print("#", end="") for x in range(size) for y in range(size)] 
    # [print(print("#", end="") for x in range(size)) for x in range(size]
