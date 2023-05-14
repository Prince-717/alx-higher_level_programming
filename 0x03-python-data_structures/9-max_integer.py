#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        m_int = my_list[0]
        for num in my_list:
            if num > m_int:
                m_int = num
        return m_int
