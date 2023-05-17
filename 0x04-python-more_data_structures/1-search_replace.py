#!/usr/bin/python3

def search_replace(my_list, search, replace):
    n_list = list(map(lambda m: replace if m == search else m, my_list))
    return (n_list)
