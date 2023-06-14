#!/usr/bin/python3
"""Creates a lookup function."""


def lookup(obj):
    """Fetches all attributes and methods of an object.

    Args:
        obj: Object to retrieve attributes and methods of.

    Returns:
        List of attributes and methods.
    """
    return dir(obj)
