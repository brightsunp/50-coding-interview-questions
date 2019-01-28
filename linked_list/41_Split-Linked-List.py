#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/28'

Given a linked list, write a function to split the list into two equal halves.

divide(1 -> 2 -> 3 -> 4) = 1 -> 2, 3 -> 4
divide(1 -> 2 -> 3 -> 4 -> 5) = 1 -> 2 -> 3, 4 -> 5
'''

from copy import deepcopy


class LinkNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def divide(root):
    fir, slow, fast = root, root, root.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    sec = slow.next
    slow.next = None
    return fir, sec


if __name__ == '__main__':
    test = LinkNode(1)
    test.next = LinkNode(2)
    test.next.next = LinkNode(3)
    test.next.next.next = LinkNode(4)

    test1 = deepcopy(test)
    fir1, sec1 = divide(test1)
    assert fir1.val == 1
    assert fir1.next.val == 2
    assert not fir1.next.next
    assert sec1.val == 3
    assert sec1.next.val == 4
    assert not sec1.next.next

    test2 = deepcopy(test)
    test2.next.next.next.next = LinkNode(5)
    fir2, sec2 = divide(test2)
    assert fir2.val == 1
    assert fir2.next.val == 2
    assert fir2.next.next.val == 3
    assert not fir2.next.next.next
    assert sec2.val == 4
    assert sec2.next.val == 5
    assert not sec2.next.next
