#!/usr/bin/python3
"""Python module that defines a JSON-to-object function"""
import json


def from_json_string(my_str):
    """Returns Python object representation of a JSON string"""
    return json.loads(my_str)
