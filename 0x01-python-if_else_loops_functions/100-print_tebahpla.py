#!/usr/bin/python3
for j in range(ord("z"), ord("a") - 1, -1):
    if j % 2 == 0:
        dispa = 0
    else:
        dispa = 32
    print("{}".format(chr(j - dispa)), end="")
