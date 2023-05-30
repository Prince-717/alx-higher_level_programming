#!/usr/bin/python3
"""Defines a 'Square' class with a private instance attribute"""


class Square:
    """Definition of of class Square"""
    def __init__(self, size=0):
        """Inits Square with a size integer

            Args:
                size: An integer representing size of the square.

            Raises:
                TypeError: The size argument is not an integer.
                ValueError: The size argument is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
