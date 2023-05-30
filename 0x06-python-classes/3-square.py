#!/usr/bin/python3
"""Creating a Square class with a private instance attribute."""


class Square:
    """Definition of square"""
    def __init__(self, size=0):
        """Inits Square with a size integer.

            Args:
                size: An integer size of the square.

            Raises:
                TypeError: The size argument is not an integer.
                ValueError: The size argument is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square."""
        return self.__size * self.__size
