#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for colum in row:
                if colum == row[-1]:
                    print("{:d}".format(colum), end="")
                else:
                    print("{:d}".format(colum), end=" ")
            print()
