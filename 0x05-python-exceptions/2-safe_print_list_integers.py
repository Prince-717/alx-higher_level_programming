#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count_item = 0

    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end='')
        except (TypeError, ValueError):
            pass
        else:
            count_item += 1
    print()
    return (count_item)
