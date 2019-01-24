#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/24'

Given an unsorted array, find the length of the longest sequence of consecutive numbers in the array.

consecutive([4, 2, 1, 6, 5]) = 3, [4, 5, 6]
consecutive([5, 5, 3, 1]) = 1, [1], [3], or [5]
'''


def consecutive1(nums):
    # sort and count: O(nlogn) time, O(1) space
    if not nums:
        return 0
    nums.sort()
    res, cur = 1, 1
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            cur += 1
        else:
            res = max(res, cur)
            cur = 1
    res = max(res, cur)
    return res


def consecutive2(nums):
    # hashset: O(n) time, O(n) space
    uniques = set(nums)
    res = 0
    for unique in uniques:
        # not the leftmost value in the sequence
        if unique - 1 in uniques:
            continue
        cur = 0
        while unique in uniques:
            unique, cur = unique + 1, cur + 1
        res = max(res, cur)
    return res


if __name__ == '__main__':
    for consecutive in [consecutive1, consecutive2]:
        assert consecutive([]) == 0
        assert consecutive([4, 2, 1, 6, 5]) == 3
        assert consecutive([5, 5, 3, 1]) == 1
