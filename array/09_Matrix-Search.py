#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/25'

Given an n x m array where all rows and columns are in sorted order, write a function to determine whether the array contains an element x.

contains([[1,  2,  3,  4]
         [5,  6,  7,  8]
         [9, 10, 11, 12]], 4) = True
'''


def contains1(matrix, x):
    # binary search: land the row, then the col
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    lasts = [row[-1] for row in matrix]
    i = _search(lasts, x)
    if i == m:
        return False
    j = _search(matrix[i], x)
    if j == n:
        return False
    if x == matrix[i][j]:
        return True
    return False


def _search(arr, x):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) >> 1
        if x <= arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


def contains2(matrix, x):
    # brute but concise
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    i, j = 0, n - 1
    while i < m and j >= 0:
        if x == matrix[i][j]:
            return True
        if x < matrix[i][j]:
            j -= 1
        else:
            i += 1
    return False


if __name__ == '__main__':
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    for contains in [contains1, contains2]:
        assert contains(A, 4)
        assert contains(A, 6)
        assert contains(A, 9)
        assert not contains(A, 0)
        assert not contains(A, 13)
