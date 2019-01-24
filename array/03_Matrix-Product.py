#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/24'

Given a matrix, find the path from top left to bottom right with the greatest product by moving only down and right.

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
1 -> 4 -> 7 -> 8 -> 9
2016

[-1, 2, 3]
[4, 5, -6]
[7, 8, 9]
-1 -> 4 -> 5 -> -6 -> 9
1080

Notes: brute force O(2^(m+n-2))
'''


def matrix_product(matrix):
    # dp: [min_cur, max_cur]
    m, n = len(matrix), len(matrix[0])
    if m == 0 or n == 0:
        return 0

    dp = [[[_, _] for _ in range(n)] for _ in range(m)]

    dp[0][0] = [matrix[0][0], matrix[0][0]]
    for i in range(1, m):
        dp[i][0] = sorted(pre * matrix[i][0] for pre in dp[i-1][0])
    for j in range(1, n):
        dp[0][j] = sorted(pre * matrix[0][j] for pre in dp[0][j-1])

    for i in range(1, m):
        for j in range(1, n):
            tmp = sorted(pre * matrix[i][j] for pre in dp[i-1][j] + dp[i][j-1])
            dp[i][j] = [tmp[0], tmp[-1]]

    return dp[-1][-1][-1]


if __name__ == '__main__':
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert matrix_product(matrix1) == 2016

    matrix2 = [[-1, 2, 3], [4, 5, -6], [7, 8, 9]]
    assert matrix_product(matrix2) == 1080
