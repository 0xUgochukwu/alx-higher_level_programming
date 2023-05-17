#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None

    for key, _value in a_dictionary.items():
        if _value == value:
            del a_dictionary[key]
            break

    return a_dictionary
