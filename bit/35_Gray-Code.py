#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/27'

Given two integers, write a function to determine whether or not their binary representations differ by a single bit.

gray(0, 1) = true
gray(1, 2) = false
'''


def gray1(num1, num2):
    # count '1' in XOR result
    calc = num1 ^ num2
    count = 0
    while calc:
        calc &= calc-1
        count += 1
    return count == 1


def gray2(num1, num2):
    # no need to operate until 0
    calc = num1 ^ num2
    return calc and (calc & (calc-1) == 0)


if __name__ == '__main__':
    for gray in [gray1, gray2]:
        assert gray(0, 1)
        assert not gray(1, 2)
        assert not gray(1, 1)
