#!/usr/bin/python3

def square(a):
    return (a ** 2)


def square_matrix_simple(matrix=[]):
    square_matrix = matrix.copy()
    for i in range(len(matrix)):
        square_matrix[i] = list(map(square, matrix[i]))
    return square_matrix
