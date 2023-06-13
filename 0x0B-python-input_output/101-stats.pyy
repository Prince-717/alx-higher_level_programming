#!/usr/bin/python3
"""Read from standard input and calculate metrics
"""


def print_stats(d_size, state_code):
    """Print accumulated metrics
    """
    print("File d_size: {}".format(d_size))
    for opener in sorted(state_code):
        print("{}: {}".format(opener, state_code[opener]))


if __name__ == "__main__":
    import sys

    d_size = 0
    state_code = {}
    authentic_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    loop_count = 0

    try:
        for file_line in sys.stdin:
            if loop_count == 10:
                print_stats(d_size, state_code)
                loop_count = 1
            else:
                loop_count += 1

            file_line = file_line.split()

            try:
                d_size += int(file_line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if file_line[-2] in authentic_codes:
                    if state_code.get(file_line[-2], -1) == -1:
                        state_code[file_line[-2]] = 1
                    else:
                        state_code[file_line[-2]] += 1
            except IndexError:
                pass

        print_stats(d_size, state_code)

    except KeyboardInterrupt:
        print_stats(d_size, state_code)
        raise
