#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    len_args = len(sys.argv)
    i = 1

    sum = 0

    while i < len_args:
        sum += int(sys.argv[i])

        i += 1

    print(f"{sum}")
