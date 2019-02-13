#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/27'

Given an array containing all the numbers from 1 to n except two, find the two missing numbers.

missing([4, 2, 3]) = 1, 5
'''
from functools import reduce


def missing1(nums):
    # sort and count
    nums.sort()
    count, i, res = 0, 0, []
    while i < len(nums):
        if i+count+1 != nums[i]:
            count += 1
            res.append(i+count)
        i += 1
    while count < 2:
        count += 1
        res.append(i+count)
    return res


def missing2(nums):
    # convert to Single Number III (Leetcode)
    n = len(nums) + 2
    arr = nums + [i+1 for i in range(1, n)]
    calc = reduce(lambda x, y: x ^ y, arr)
    # last '1' bit
    calc &= -calc
    res = [0, 0]
    for num in arr:
        if num & calc == 0:
            res[0] ^= num
        else:
            res[1] ^= num
    return res


if __name__ == '__main__':
    test1 = []
    test2 = [4, 2, 3]
    test3 = [5, 1, 3]

    for missing in [missing1]:
        dup1 = test1[:]
        assert missing(dup1) == [1, 2]
        dup2 = test2[:]
        assert missing(dup2) == [1, 5]
        dup3 = test3[:]
        assert missing(dup3) == [2, 4]
