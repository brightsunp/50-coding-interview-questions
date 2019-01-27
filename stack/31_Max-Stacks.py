#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/26'

Implement a LIFO stack that has a push(), pop(), and max() function, where max() returns the maximum value in the stack. All of these functions should run in O(1) time.
'''


class Node(object):
    def __init__(self, val, next=None, pre_max=None):
        self.val = val
        self.next = next
        self.pre_max = pre_max


class MaxStack(object):
    '''
    LinkNode: add/remove in O(1) time
    '''
    def __init__(self):
        self.stack = None
        self.cur_max = None

    def push(self, x):
        p = Node(x)
        p.next = self.stack
        # self.stack == head
        self.stack = p

        p.pre_max = self.cur_max
        if not self.cur_max or p.val > self.cur_max.val:
            self.cur_max = p

    def pop(self):
        if not self.stack:
            raise ValueError

        head = self.stack
        self.stack = head.next
        self.cur_max = head.pre_max
        return head.val

    def max(self):
        if not self.cur_max:
            raise ValueError

        return self.cur_max.val


if __name__ == '__main__':
    test = MaxStack()

    test.push(1)
    assert test.max() == 1
    test.push(2)
    assert test.max() == 2
    test.push(1)
    assert test.max() == 2
    assert test.pop() == 1
    assert test.max() == 2
    assert test.pop() == 2
    assert test.max() == 1
    assert test.pop() == 1

    try:
        test.max()
    except Exception as e:
        assert type(e) == ValueError

    try:
        test.pop()
    except Exception as e:
        assert type(e) == ValueError
