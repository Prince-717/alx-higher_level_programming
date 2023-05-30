#!/usr/bin/python3
"""Defines a 'Square' class with a private instance attribute"""


class Square:
    """Class Square that defines a square object
    """
    def __init__(self, size):
        """Initialize method that stores the size of the square

        Args:
            param1 (int): size of the square
        """
        self.__size = size
