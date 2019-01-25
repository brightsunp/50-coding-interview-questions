#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/25'

Given 2 sorted arrays, A and B, where A is long enough to hold the contents of A and B, write a function to copy the contents of B into A without using any buffer or additional memory.

A = {1,3,5,0,0,0}
B = {2,4,6}
mergeArrays(A, B)
A = {1,2,3,4,5,6}

Notes: in-place modification
'''


def merge1(arr1, arr2):
    # bottom-up swap
    m, n = len(arr1), len(arr2)
    if not m or m < n:
        return
    last = 0
    while arr1[last]:
        last += 1
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] > arr2[j]:
            for x in range(last, i, -1):
                arr1[x], arr1[x-1] = arr1[x-1], arr1[x]
            arr1[i] = arr2[j]
            j, last = j+1, last+1
        i += 1
    while j < n:
        arr1[last] = arr2[j]
        j, last = j+1, last+1


def merge2(arr1, arr2):
    # top-down merge
    m, n = len(arr1), len(arr2)
    if not m or m < n:
        return
    length = 0
    while arr1[length]:
        length += 1
    i, j = length-1, n-1
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[i+j+1] = arr1[i]
            i -= 1
        else:
            arr1[i+j+1] = arr2[j]
            j -= 1
    while j >= 0:
        arr1[j] = arr2[j]
        j -= 1


if __name__ == '__main__':
    A = [3, 5, 0, 0, 0, 0, 0, 0]
    B = [1, 2, 4, 6, 7]

    for merge in [merge1, merge2]:
        nums1, nums2 = A[:], B[:]
        merge(nums1, nums2)
        assert nums1 == [1, 2, 3, 4, 5, 6, 7, 0]
