#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list:
        new_list = []
        for item in my_list:
            if item == 0:
                new_list.append(True)
            elif item < 0 and item % 2 == 0:
                new_list.append(True)
            elif item < 0 and item % 2 != 0:
                new_list.append(False)
            elif item > 0 and item % 2 == 0:
                new_list.append(True)
            elif item > 0 and item % 2 != 0:
                new_list.append(False)

        return new_list

    else:
        return my_list

        
