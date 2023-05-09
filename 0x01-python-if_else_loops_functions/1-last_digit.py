#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = number % 10

if number < 0:
    number = -number
    l_digit = number % 10
    l_digit = -l_digit
    print(f'Last digit of {-number} is {l_digit} and is less than 6 and not 0')


elif l_digit > 5:
    print(f'Last digit of {number} is {l_digit} and is greater than 5')
elif l_digit == 0:
    print(f'Last digit of {number} is {l_digit} and is 0')
elif l_digit < 6 and l_digit != 0:
    print(f'Last digit of {number} is {l_digit} and is less than 6 and not 0')
