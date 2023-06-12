#!/usr/bin/python3
""" My List """


class MyList(list):
    """ My Own List class """

    def __init__(self):
        """ Initializes my list object """
        super().___init__()

    def print_sorted(self):
        """ Prints the list but sorted """
        print(sorted(self))
