#!/usr/bin/python3
"""This Python module defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of a string object"""
    return json.dumps(my_obj)
