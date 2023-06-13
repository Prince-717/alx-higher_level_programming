#!/usr/bin/python3
"""Python module that defines a Pascal's Triangle function"""


def pascal_triangle(num):
    """Represents Pascal's Triangle of size num
    """
    if num <= 0:
        return []

    tr = [[1]]
    while len(tr) != num:
        trian = tr[-1]
        temporary = [1]
        for index in range(len(trian) - 1):
            temporary.append(trian[index] + trian[index + 1])
        temporary.append(1)
        tr.append(temporary)
    return tr
