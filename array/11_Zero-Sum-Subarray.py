#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/26'

Given an array, write a function to find any subarray that sums to zero, if one exists.

zeroSum({1, 2, -5, 1, 2, -1}) = [2, -5, 1, 2]

Notes: subarray means continuous range slice.
'''


def zeroSum(arr):
    # hashmap: {pre_sum: pre}
    d, pre_sum, n = {}, 0, len(arr)
    for i in range(n+1):
        pre = d.get(pre_sum, -1)
        if pre != -1:
            return arr[pre:i]
        else:
            if i == n:
                break
            else:
                d[pre_sum] = i
                pre_sum += arr[i]
    return None


solutions = []
solution = []


def find_one(arr):
    _dfs1(arr, 0, 0)
    return solution


def _dfs1(arr, target, pos):
    if solution and target == 0:
        return True
    for i in range(pos, len(arr)):
        solution.append(arr[i])
        if _dfs1(arr, target-arr[i], i+1):
            return True
        solution.pop()
    return False


def find_all(arr):
    _dfs2(arr, 0, 0, [])
    return solutions


def _dfs2(arr, target, pos, tmp):
    if tmp and target == 0:
        return solutions.append(tmp)
    for i in range(pos, len(arr)):
        _dfs2(arr, target-arr[i], i+1, tmp+[arr[i]])


if __name__ == '__main__':
    test = [1, 2, -5, 1, 2, -1]

    assert zeroSum([0]) == [0]
    assert zeroSum([0, 0, 0]) == [0]
    assert zeroSum([1, 2, 3, 0]) == [0]
    assert not zeroSum([1, 2, 3])
    assert zeroSum(test) == [2, -5, 1, 2]

    assert find_one(test) in find_all(test)
