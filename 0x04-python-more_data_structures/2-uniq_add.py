#!/usr/bin/python3
def uniq_add(my_list=[]):
    u_sum = 0
    i_set = set()
    for n in my_list:
        if n not in i_set:
            i_set.add(n)
            u_sum += n
    return u_sum
