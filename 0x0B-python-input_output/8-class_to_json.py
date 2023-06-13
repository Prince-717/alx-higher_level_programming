#!/usr/bin/python3
"""Creates a class_to_json function."""


def class_to_json(obj):
    """Fetches the dictionary description of an object.

    Args:
        obj: Object to retrieve the dictionary from
    Returns:
        A dictionary description
    """
    return obj.__dict__
