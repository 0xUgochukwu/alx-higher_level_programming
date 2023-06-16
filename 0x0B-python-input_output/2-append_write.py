#!/usr/bin/python3
""" Append to A File """


def append_write(filename="", text=""):
    """ Function that appends to a file """
    with open(filename, mode='a', encoding="utf-8") as file:
        return file.write(text)
