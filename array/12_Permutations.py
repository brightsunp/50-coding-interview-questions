#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/26'

Write a function that returns all permutations of a given list.

permutations({1, 2, 3})
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
'''

solutions = []


def permutations(arr):
    _dfs(arr, [])
    return solutions


def _dfs(arr, tmp):
    if len(tmp) == len(arr):
        return solutions.append(tmp)
    for num in arr:
        if num in tmp:
            continue
        _dfs(arr, tmp + [num])


if __name__ == '__main__':
    assert permutations([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
