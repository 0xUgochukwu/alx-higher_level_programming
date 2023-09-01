#!/usr/bin/python3

def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers  """
    loi = list_of_integers
    ln = len(loi)

    if (ln == 0):
        return None

    m = ln // 2
    if (m == ln - 1 or loi[m] >= loi[m + 1]) and
    (m == 0 or loi[m] >= loi[m - 1]):
        return loi[m]
    if m != ln - 1 and loi[m] < loi[m + 1]:
        return find_peak(loi[(m + 1):])
    return find_peak(loi[:m])
