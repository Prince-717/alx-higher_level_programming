#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for a, b in filter(lambda q: q[1] == value, list(a_dictionary.items())):
            del a_dictionary[a]
    return a_dictionary
