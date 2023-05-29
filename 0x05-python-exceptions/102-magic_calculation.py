#!/usr/bin/python3
def magic_calculation(a, b):
    outcome = 0
    for index in range(1, 3):
        try:
            if (index > a):
                raise Exception("Too far")
            else:
                outcome += (a ** b) / index
        except:
            outcome = b + a
            break
    return (outcome)
