#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/13'

Given two integers, write a function to sum the numbers without using any arithmetic operators.
'''


def add1(a, b):
    # recursive
    if not a:
        return b
    res = a ^ b
    carry = (a & b) << 1
    return add1(carry, res)


def add2(a, b):
    # iterative
    carry, res = a, b
    while carry:
        tmp = res
        res = carry ^ res
        carry = (carry & tmp) << 1
    return res


if __name__ == '__main__':
    for add in [add1, add2]:
        assert add(0, 137) == 137
        assert add(1, 3) == 4
        assert add(13, 27) == 40
