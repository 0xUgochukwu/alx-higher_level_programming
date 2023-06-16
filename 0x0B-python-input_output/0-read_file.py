#!/usr/bin/python3
""" Read A File """


def read_file(filename=""):
    """ Function that reads a file """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
