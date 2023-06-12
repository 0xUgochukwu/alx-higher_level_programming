#!/usr/bin/python3
"""
Can I?
"""

def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Raises:
        TypeError: If the object can't have a new attribute.

    """
    if hasattr(obj, '__dict__'):
        obj.__setattr__(attribute, value)
    else:
        raise TypeError("can't add new attribute")
