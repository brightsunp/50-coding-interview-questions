#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/24'

Given a 2D array of 1s and 0s, find the largest square subarray of all 1s.

subarray([1, 1, 1, 0]
         [1, 1, 1, 1]
         [1, 1, 0, 0]) = 2
'''


def subarray1(matrix):
    # brute
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res, _extend(matrix, i, j, m, n))
    return res


def _extend(matrix, i, j, m, n):
    length = 0
    while length < min(m-i, n-j):
        flag = True
        for x in range(i, i+1+length):
            if not matrix[x][j+length]:
                flag = False
                break
        for y in range(j, j+1+length):
            if not matrix[i+length][y]:
                flag = False
                break
        if flag:
            length += 1
        else:
            break
    return length


def subarray2(matrix):
    # bottom-up dp: extend up and left
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    res = 0
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if not i or not j:
                dp[i][j] = 1 if matrix[i][j] else 0
            elif matrix[i][j]:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
            res = max(res, dp[i][j])
    return res


if __name__ == '__main__':
    matrix1 = [[1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 0, 0]]
    matrix2 = [[1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 0]]

    for subarray in [subarray1, subarray2]:
        assert subarray(matrix1) == 2
        assert subarray(matrix2) == 3
