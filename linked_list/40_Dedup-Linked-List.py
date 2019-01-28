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


def dedup1(root):
    # hashset
    unq = set()
    res, pre = root, None
    while root:
        if root.val in unq:
            pre.next = root.next
        else:
            unq.add(root.val)
            pre = root
        root = root.next
    return res


def dedup2(root):
    # brute
    res = root
    while root:
        cur = root
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        root = root.next
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
