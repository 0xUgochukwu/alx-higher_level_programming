#!/usr/bin/python3
""" Inherits from function """


def inherits_from(obj, a_class):
    """ Checks if an object inherited from a class """
    
    return (issubclass(obj, a_class) and type(obj) != a_class)
