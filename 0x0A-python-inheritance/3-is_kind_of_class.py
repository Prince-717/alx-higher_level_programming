#!/usr/bin/python3
"""Creates a is_kind_of_class() function."""


def is_kind_of_class(obj, a_class):
    """Confirms if an object is an instance of a class.

    Args:
        obj: Object to check.
        a_class: Class to check with.
    Returns:
        True if the object is an instance of the class or False.
    """
    return isinstance(obj, a_class)
