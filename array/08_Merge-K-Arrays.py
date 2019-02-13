#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/25'

Given k sorted arrays, merge them into a single sorted array.

merge({{1, 4, 7},{2, 5, 8},{3, 6, 9}}) = {1, 2, 3, 4, 5, 6, 7, 8, 9}
'''
from functools import reduce


def merge(arrs):
    # each time merge two arrays
    return reduce(_merge2, arrs, [])


def _merge2(arr1, arr2):
    res = []
    i, j, m, n = 0, 0, len(arr1), len(arr2)
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    res.extend(arr1[i:] + arr2[j:])
    return res


if __name__ == '__main__':
    assert merge([[]]) == []
    assert merge([[1, 4, 5], [], [2, 3, 6, 7]]) == [1, 2, 3, 4, 5, 6, 7]
    assert merge([[1, 4, 7], [2, 5, 8], [3, 6, 9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
