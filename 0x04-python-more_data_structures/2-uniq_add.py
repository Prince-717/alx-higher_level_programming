#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list:
        un = set([x for x in my_list if my_list.count(x) > 1])
        sum = 0
        for n in un:
            sum += n
        for item in my_list:
            if item in un:
                continue
            else:
                sum += item

        return sum
