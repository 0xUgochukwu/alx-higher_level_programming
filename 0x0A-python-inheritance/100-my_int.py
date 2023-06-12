#!/usr/bin/python3
"""
The rebel Integer
"""


class MyInt(int):
    """
    Represents a rebel integer.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator (==) to invert its behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=) to invert its behavior.
        """
        return super().__eq__(other)
