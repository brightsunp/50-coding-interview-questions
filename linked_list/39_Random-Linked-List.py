#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/28'

Given a linked list where each node has two pointers, one to the next node and one to a random node in the list, clone the linked list.

1 -> 2 -> 3 -> 4 -> null
|    |    |    |
v    v    v    v
3    1    3    2
'''

from random import randint


class LinkNode(object):
    def __init__(self, val, next=None, rand=None):
        self.val = val
        self.next = next
        self.rand = rand


def clone(root):
    dup = root
    cur = dup
    while cur:
        cur.rand = _get_random(root)
        cur = cur.next
    return dup


def _get_random(root):
    # Reservoir Sampling
    cur, r, i = root, None, 0
    while cur:
        if randint(0, i) == 0:
            r = cur
        cur, i = cur.next, i+1
    return r


if __name__ == '__main__':
    test = LinkNode(1)
    test.next = LinkNode(2)
    test.next.next = LinkNode(3)
    test.next.next.next = LinkNode(4)

    node = clone(test)
    while node:
        print(node.val, '->', node.rand.val)
        node = node.next
