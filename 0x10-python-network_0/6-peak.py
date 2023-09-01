#!/usr/bin/python3
""" Let's find the peakkkkk!!!!!! """


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    """
    if not list_of_integers:
        return None

    ln = len(list_of_integers)
    if ln == 1:
        return list_of_integers[0]

    middle = ln // 2
    peak_candidate = list_of_integers[middle]

    if middle == 0 or peak_candidate >= list_of_integers[middle - 1]:
        if middle == ln - 1 or peak_candidate >= list_of_integers[middle + 1]:
            return peak_candidate

    if middle > 0 and list_of_integers[middle - 1] > peak_candidate:
        return find_peak(list_of_integers[:middle])
    return find_peak(list_of_integers[middle + 1:])
