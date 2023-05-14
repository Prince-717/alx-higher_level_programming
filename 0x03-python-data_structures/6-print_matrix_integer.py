#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for m_row in matrix:
            for m_col in m_row:
                if m_col == m_row[-1]:
                    print("{:d}".format(m_col), end='')
                else:
                    print("{:d}".format(m_col), end=' ')

            print()
