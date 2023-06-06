#!/usr/bin/python3
"""
Say My Name

"""


def say_my_name(first_name, last_name=""):
    """
        Function to print full name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
