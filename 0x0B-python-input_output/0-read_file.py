#!/usr/bin/python3
""" Module that contains a function that reads from a file """


def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename: filename

    """

    with open(filename, 'r', encoding="utf-8") as file_obj:
        file_data = file_obj.read()
        print(file_data, end='')
