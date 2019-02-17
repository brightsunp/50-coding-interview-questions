#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/28'

Given a linked list, determine whether it contains a cycle.

1 -> 2 -> 3 -> 4
     ^         |
     |_________|
'''


class LinkNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def contains(head):
    # Floyd Cycle Detection Algorithm
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    test = LinkNode(1)
    test.next = LinkNode(2)
    test.next.next = LinkNode(3)
    test.next.next.next = LinkNode(4)
    assert not contains(test)

    test.next.next.next.next = test.next
    assert contains(test)
