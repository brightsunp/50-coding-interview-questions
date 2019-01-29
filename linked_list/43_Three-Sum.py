#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/29'

Given a list of integers, write a function that returns all sets of 3 numbers in the list, a, b, and c, so that a + b + c == 0.

threeSum({-1, 0, 1, 2, -1, -4})
[-1, -1, 2]
[-1, 0, 1]
'''


def three_sum1(nums):
    # sort and clamp (Two Sum)
    nums.sort()
    res = []
    for fir in range(len(nums)-2):
        if fir == 0 or nums[fir] > nums[fir-1]:
            sec, thi = fir+1, len(nums)-1
            while sec < thi:
                cur = [nums[fir], nums[sec], nums[thi]]
                if sum(cur) == 0:
                    res.append(cur)
                if sum(cur) < 0:
                    pre = sec
                    while nums[sec] == nums[pre] and sec < thi:
                        sec += 1
                else:
                    pre = thi
                    while nums[thi] == nums[pre] and sec < thi:
                        thi -= 1
    return res


solutions = []


def three_sum2(nums):
    # backtracking
    _dfs(nums, 0, 0, [])
    return sorted(solutions)


def _dfs(nums, pos, target, tmp):
    if len(tmp) == 3:
        tmp.sort()
        if target == 0 and tmp not in solutions:
            solutions.append(tmp)
        return
    for i in range(pos, len(nums)):
        _dfs(nums, i+1, target-nums[i], tmp+[nums[i]])


if __name__ == '__main__':
    test = [-1, 0, 1, 2, -1, -4]

    for three_sum in [three_sum1, three_sum2]:
        assert three_sum(test) == [[-1, -1, 2], [-1, 0, 1]]
