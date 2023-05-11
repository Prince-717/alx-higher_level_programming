#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import sub, add

    if a < b:
        res = add(a, b)
        for num in range(4, 6):
            res = add(c, num)
        return (res)

    else:
        return (sub(a, b))
