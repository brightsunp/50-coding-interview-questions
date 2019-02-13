#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/24'

Given an array of integers where each value 1 <= x <= len(array), write a function that finds all the duplicates in the array.

dups([1, 2, 3])    = []
dups([1, 2, 2])    = [2]
dups([3, 3, 3])    = [3]
dups([2, 1, 2, 1]) = [1, 2]

Notes: result no need in same order, revert the original array if in-place modification not allowed.
'''
from collections import Counter


def dups1(nums):
    # hashmap: O(n) time, O(n) space
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    return [k for k, v in d.items() if v > 1]


def dups2(nums):
    # counting array: O(n) time, O(n) space
    count = [0 for _ in range(len(nums)+1)]
    res = []
    for num in nums:
        if count[num] == 1:
            res.append(num)
        count[num] += 1
    return res


def dups3(nums):
    # mapping base on '1 <= x <= len(nums)': O(n) time, O(1) space
    res = set()
    for i in range(len(nums)):
        sign = abs(nums[i]) - 1
        if nums[sign] > 0:
            nums[sign] = -nums[sign]
        else:
            res.add(abs(nums[i]))
    return list(res)


if __name__ == '__main__':
    for dups in [dups1, dups2, dups3]:
        assert dups([1, 2, 3]) == []
        assert dups([1, 2, 2]) == [2]
        assert dups([3, 3, 3]) == [3]
        assert Counter(dups([2, 1, 2, 1])) == Counter([1, 2])
