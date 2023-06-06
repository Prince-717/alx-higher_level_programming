#!/usr/bin/python3
"""Creates a LockedClass class."""


class LockedClass:
    """Empty class that only permits a 'first_name' attribute."""
    __slots__ = ["first_name"]
