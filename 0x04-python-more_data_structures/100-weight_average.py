#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    w_sum = 0
    avg = 0
    for r, n in my_list:
        avg += r * n
        w_sum += n
    return avg / w_sum
