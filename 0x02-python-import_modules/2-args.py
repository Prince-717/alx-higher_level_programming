#!/usr/bin/python3
import sys

len_args = len(sys.argv)
i = 1

if len_args == 1:
    print(f"{len_args - 1} arguments.")

if len_args > 1:
    if len_args == 2:
        print(f"{len_args - 1} argument:")
        print(f"{len_args -1}: {sys.argv[1]}")

    elif len_args > 2:
        print(f"{len_args - 1} arguments:")

        while i < len_args:
            print(f"{i}: {sys.argv[i]}")

            i += 1
            
