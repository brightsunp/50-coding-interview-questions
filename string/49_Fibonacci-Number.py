#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/12'

Given an integer n, write a function to compute the nth Fibonacci number.

fibonacci(1) = 1
fibonacci(5) = 5
fibonacci(10) = 55

Notes: assume n positive number.
'''


def fibonacci1(n):
    # recursive
    if n == 1 or n == 2:
        return 1
    return fibonacci1(n-2) + fibonacci1(n-1)


def fibonacci2(n):
    # dp
    dp = [1 for _ in range(n)]
    for i in range(2, n):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n-1]


if __name__ == '__main__':
    for fibonacci in [fibonacci1, fibonacci2]:
        assert fibonacci(1) == 1
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55
