#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for key, _value in sorted(a_dictionary.items()):
        if _value == value:
            del a_dictionary[key]
    return a_dictionary
