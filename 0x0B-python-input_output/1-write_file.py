#!/usr/bin/python3
""" Write to A File """


def write_file(filename="", text=""):
    """ Function that writes to a file """
    with open(filename, mode='w', encoding="utf-8") as file:
        return file.write(text)
