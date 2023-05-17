#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    r_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r_prev = 0
    r_int = 0
    for n in roman_string:
        if r_num[n] > r_prev:
            r_int += r_num[n] - r_prev - r_prev
            r_prev = r_num[n]
        else:
            r_int += r_num[n]
            r_prev = r_num[n]
    return r_int
