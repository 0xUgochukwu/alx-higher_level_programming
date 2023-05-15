#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements from each tuple, or use 0 if the tuple is smaller than 2
    a = tuple_a[:2] + (0, 0)[:2 - len(tuple_a)]
    b = tuple_b[:2] + (0, 0)[:2 - len(tuple_b)]

    # Add the corresponding elements and return the resulting tuple
    return (a[0] + b[0], a[1] + b[1])

