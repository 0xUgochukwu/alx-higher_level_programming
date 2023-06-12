#!/usr/bin/python3
""" Lookup function """


def is_same_class(obj, a_class):
    """ Checks if object is exactly an instance of the specified class """

    return (type(obj) is a_class)
