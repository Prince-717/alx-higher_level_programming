#!/usr/bin/python3
def remove_char_at(str, pos):
    if pos < 0:
        return (str)
    return (str[:pos] + str[pos+1:])
