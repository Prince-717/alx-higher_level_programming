#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if char == 113 or char == 101:
        continue
    print('{:c}'.format(char), end='')

