#!/usr/bin/python3
"""module for the matrix rotation task
"""


def rotate_2d_matrix(matrix):
    """ method for rotating 2d matrix
    """
    matrix_length = len(matrix)
    matrix_type = type(matrix)
    if matrix_length <= 0:
        return
    if matrix_type != list:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows_ = len(matrix)
    columns_ = len(matrix[0])
    if not all(map(lambda x: len(x) == columns_, matrix)):
        return
    c, r = 0, rows_ - 1
    for i in range(columns_ * rows_):
        if i % rows_ == 0:
            matrix.append([])
        if r == -1:
            r = rows_ - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == columns_ - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
