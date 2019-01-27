#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/27'

Given an integer, write a function to compute the number of ones in the binary representation of the number.
'''


def ones1(num):
    # operate util 0
    count = 0
    while num:
        num &= num-1
        count += 1
    return count


def ones2(num):
    # judge last bit
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count


if __name__ == '__main__':
    for ones in [ones1, ones2]:
        assert ones(0) == 0
        assert ones(1) == 1
        assert ones(2) == 1
        assert ones(3) == 2
        assert ones(7) == 3
