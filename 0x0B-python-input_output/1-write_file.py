#!/usr/bin/python3
""" Python module that contains a function that returns the number of lines
    of a text file
"""


def number_of_lines(filename=""):
    """ Function that reads from a file and prints its number of lines

    Args:
        filename: filename

    """
    number_of_lines = 0
    with open(filename, 'r', encoding="utf-8") as f:
        for file_line in f:
            number_of_lines += 1
    return number_of_lines
