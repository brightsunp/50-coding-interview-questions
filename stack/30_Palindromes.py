#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/26'

Given a linked list, write a function to determine whether the list is a palindrome.

palindrome(1 -> 2 -> 3) = false
palindrome(1 -> 2 -> 1) = true
'''


class LinkNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def is_palindrome1(root):
    # two-pass
    dup, stack = root, []
    while dup:
        stack.append(dup.val)
        dup = dup.next
    while root:
        if root.val != stack.pop():
            return False
        root = root.next
    return True


def is_palindrome2(root):
    # one-pass: slow and fast
    slow, fast, stack = root, root, []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if slow.val != stack.pop():
            return False
        slow = slow.next
    return True


if __name__ == '__main__':
    test1 = LinkNode(1)
    test1.next = LinkNode(2)
    test1.next.next = LinkNode(3)
    test2 = LinkNode(1)
    test2.next = LinkNode(2)
    test2.next.next = LinkNode(1)
    test3 = LinkNode(1)
    test3.next = LinkNode(2)
    test3.next.next = LinkNode(2)
    test3.next.next.next = LinkNode(1)

    for is_palindrome in [is_palindrome1, is_palindrome2]:
        assert not is_palindrome(test1)
        assert is_palindrome(test2)
        assert is_palindrome(test3)
