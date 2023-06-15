#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_list = []
    for rows in range(len(matrix)):
        for v in range(3):
            new_list.append(matrix[rows][v] ** 2)
        new_matrix.append(new_list)
        new_list = []
    return (new_matrix)
