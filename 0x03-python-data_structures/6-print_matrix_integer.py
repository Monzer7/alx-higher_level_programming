#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    m = len(matrix)
    n = len(matrix[0][0])
    for i in range(m):
        for j in range(n):
            print("{:d}".format(matrix[i][j]), end=' ')
        print("$")
