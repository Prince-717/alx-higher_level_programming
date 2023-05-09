#!/usr/bin/python3
print("{:02d}, ".format(1), end="")
for a in range(10):
    for b in range(a + 1, 10):
        if a == 0 and b == 1:
            continue
        print("{:02d}, ".format(a * 10 + b), end="")
print()
