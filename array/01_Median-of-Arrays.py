#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/23'

Find the median of two sorted arrays.

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
median(arr1, arr2) = 3.5
'''


def median(arr1, arr2):
    # merge and get median
    m, n = len(arr1), len(arr2)
    arr, i, j = [], 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    arr.extend(arr1[i:] + arr2[j:])
    total = m + n
    mid = total >> 1
    return arr[mid] if total&1 == 1 else (arr[mid-1]+arr[mid]) / 2.0


if __name__ == '__main__':
    assert median([1, 3, 5], [2, 4, 6]) == 3.5
    assert median([1, 3], [2, 4, 5, 6]) == 3.5
    assert median([1, 3, 5], [2, 4]) == 3
    assert median([], [1, 2, 3, 4, 5]) == 3
