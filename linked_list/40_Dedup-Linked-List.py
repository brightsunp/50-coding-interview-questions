#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/28'

Given an unsorted linked list, write a function to remove all the duplicates.

dedup(1 -> 2 -> 3 -> 2 -> 1) = 1 -> 2 -> 3
'''


class LinkNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def dedup1(head):
    # hashset
    unq = set()
    res, pre = head, None
    while head:
        if head.val in unq:
            pre.next = head.next
        else:
            unq.add(head.val)
            pre = head
        head = head.next
    return res


def dedup2(head):
    # brute
    res = head
    while head:
        cur = head
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        head = head.next
    return res


if __name__ == '__main__':
    test = LinkNode(1)
    test.next = LinkNode(2)
    test.next.next = LinkNode(3)
    test.next.next.next = LinkNode(2)
    test.next.next.next.next = LinkNode(1)

    for dedup in [dedup1, dedup2]:
        node = dedup(test)
        while node:
            print(node.val)
            node = node.next
