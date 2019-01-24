#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/24'

Given a list of items with values and weights, as well as a max weight, find the maximum value you can generate from items where the sum of the weights is less than the max.

items = {(w:1, v:6), (w:2, v:10), (w:3, v:12)}
maxWeight = 5
knapsack(items, maxWeight) = 22

Notes: no duplicate weights, used only once.
'''


class Solution(object):
    def knapsack(self, items, max_weight):
        # backtracking: find best solution
        self.max_sum = 0
        self.dfs(items, max_weight, 0, len(items), 0)
        return self.max_sum

    def dfs(self, items, target, pos, n, cur_sum):
        if target < 0:
            return
        if target == 0:
            self.max_sum = max(self.max_sum, cur_sum)
            return
        for i in range(pos, n):
            weight, value = items[i]
            self.dfs(items, target-weight, i+1, n, cur_sum+value)


if __name__ == '__main__':
    test = Solution()

    assert test.knapsack([(1, 6), (2, 10), (3, 12)], 5) == 22
    assert test.knapsack([(1, 6), (2, 10), (4, 12)], 7) == 28
    assert test.knapsack([(1, 6), (2, 10), (3, 12), (4, 18)], 5) == 24
    assert test.knapsack([(1, 6), (2, 10), (3, 12), (4, 16)], 4) == 18
