#!/usr/bin/python3
"""
Find Max Integer
"""


def max_integer(list=[]):
    """
    Function to find the maximum integer in a list and return it
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
