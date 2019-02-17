#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/13'

Given a stack, reverse the items without creating any additional data structures.

Notes: https://blog.csdn.net/dm_vincent/article/details/8008238
'''


def reverse(stack):
    # double recursive
    if not stack:
        return
    tmp = stack.pop()
    reverse(stack)
    _insert(stack, tmp)


def _insert(stack, num):
    if not stack:
        stack.append(num)
        return
    tmp = stack.pop()
    _insert(stack, num)
    stack.append(tmp)


if __name__ == '__main__':
    test = [1, 2, 3, 4, 5]

    reverse(test)
    assert test == [5, 4, 3, 2, 1]
