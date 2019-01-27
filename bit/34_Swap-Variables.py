#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/27'

Given two integers, write a function that swaps them without using any temporary variables.
'''


def swap1(num1, num2):
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2
    return num1, num2


def swap2(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return num1, num2


if __name__ == '__main__':
    for swap in [swap1, swap2]:
        assert swap(1, 2) == (2, 1)
