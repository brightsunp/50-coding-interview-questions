#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/26'

Given a stack, sort the elements in the stack using one additional stack.
'''


def sort1(stack):
    # two additional stacks
    buf1, buf2 = [], []
    while stack:
        top = stack.pop()
        while buf1 and buf1[-1] > top:
            buf2.append(buf1.pop())
        buf1.append(top)
        while buf2:
            buf1.append(buf2.pop())
    return buf1


def sort2(stack):
    # one additional stack
    buf = []
    while stack:
        top = stack.pop()
        while buf and buf[-1] > top:
            stack.append(buf.pop())
        buf.append(top)
    return buf


if __name__ == '__main__':
    for sort in [sort1, sort2]:
        assert sort([1, 3, 2, 4]) == [1, 2, 3, 4]
