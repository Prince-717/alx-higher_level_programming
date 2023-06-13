#!/usr/bin/python3
"""Python module that defines a class Student"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Fetch a dictionary representation of the Student
        If attrs is a list of strings, represents only those attributes
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {n: getattr(self, n) for n in attrs if hasattr(self, n)}
        return self.__dict__
