#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squ_matrix = matrix.copy()
    return([list(map(lambda x: x ** 2, i)) for i in matrix])
