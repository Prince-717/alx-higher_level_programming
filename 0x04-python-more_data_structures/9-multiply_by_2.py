#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    n_dict = {}
    for key, value in a_dictionary.items():
        n_dict[key] = value * 2
    return n_dict
