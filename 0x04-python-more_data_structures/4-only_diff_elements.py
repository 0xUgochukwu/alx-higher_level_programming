#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_set = set([i for i in set_1 if i not in set_2]
                  + [i for i in set_2 if i not in set_1])

    return new_set
