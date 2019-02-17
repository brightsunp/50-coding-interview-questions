#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/17'

Given an input amount of change x, write a function to determine the minimum number of coins required to make that amount of change.

Using American coins:
change(1) = 1
change(3) = 3
change(7) = 3
change(32) = 4
'''


def change(amount, coins):
    # bottom-up dp
    largest = amount + 1
    dp = [largest for _ in range(largest)]
    dp[0] = 0
    for i in range(1, largest):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return -1 if dp[amount] == largest else dp[amount]


if __name__ == '__main__':
    test = [1, 5, 10, 25, 50, 100]

    assert change(1, test) == 1
    assert change(3, test) == 3
    assert change(7, test) == 3
    assert change(32, test) == 4
