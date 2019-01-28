#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/28'

Given a linked list, and an input n, write a function that returns the nth-to-last element of the linked list.

list = 1 -> 2 -> 3 -> 4 -> 5 -> null
nthToLast(list, 0) = 5
nthToLast(list, 1) = 4
nthToLast(list, 4) = 1
nthToLast(list, 5) = null
'''


class LinkNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def nth2last(root, n):
    fir, sec = root, root
    for _ in range(n):
        if not sec:
            return None
        sec = sec.next
    if not sec:
        return None
    while sec.next:
        fir, sec = fir.next, sec.next
    return fir


if __name__ == '__main__':
    test = LinkNode(1)
    test.next = LinkNode(2)
    test.next.next = LinkNode(3)
    test.next.next.next = LinkNode(4)
    test.next.next.next.next = LinkNode(5)

    assert nth2last(test, 0).val == 5
    assert nth2last(test, 1).val == 4
    assert nth2last(test, 4).val == 1
    assert not nth2last(test, 5)
