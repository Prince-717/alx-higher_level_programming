#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = []
        for row in matrix:
            n_row = []
            for col in row:
                square = col*col
                n_row.append(square)

            new_matrix.append(n_row)
        return new_matrix
