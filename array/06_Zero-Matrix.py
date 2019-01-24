#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/24'

Given a boolean matrix, update it so that if any cell is true, all the cells in that row and column are true.

[true,  false, false]      [true,  true,  true ]
[false, false, false]  ->  [true,  false, false]
[false, false, false]      [true,  false, false]
'''


def zero_matrix(matrix):
    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])
    points = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j]:
                points.append((i, j))

    for i, j in points:
        for x in range(m):
            matrix[x][j] = True
        for y in range(n):
            matrix[i][y] = True


if __name__ == '__main__':
    matrix1 = [[True, False, False], [False, False, False], [False, False, False]]
    zero_matrix(matrix1)
    assert matrix1 == [[True, True, True], [True, False, False], [True, False, False]]

    matrix2 = [[True, False, True], [False, False, False], [False, False, False]]
    zero_matrix(matrix2)
    assert matrix2 == [[True, True, True], [True, False, True], [True, False, True]]
