#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list:
        n_list = []
        for item in my_list:
            if item == search:
                item = replace
            n_list.append(item)

        return n_list
                
