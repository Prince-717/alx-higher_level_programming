#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    num_integers = len(list_of_integers)
    middle_n = num_integers
    midle_index = num_integers // 2

    if num_integers == 0:
        return None

    while True:
        middle_n = middle_n // 2
        if (midle_index < num_integers - 1 and
                list_of_integers[midle_index] < list_of_integers[midle_index + 1]):
            if middle_n // 2 == 0:
                middle_n = 2
            midle_index = midle_index + middle_n // 2
        elif middle_n > 0 and list_of_integers[midle_index] < list_of_integers[midle_index - 1]:
            if middle_n // 2 == 0:
                middle_n = 2
            midle_index = midle_index - middle_n // 2
        else:
            return list_of_integers[midle_index]
