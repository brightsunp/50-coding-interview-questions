#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/13'

Given a tree, write a function to convert it into a circular doubly linked list from left to right by only modifying the existing pointers.
'''


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DllNode(object):
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def convert(root):
    # InOrder + DllNode
    head, pre = None, None
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            cur = DllNode(node.val)
            cur.prev = pre
            if pre:
                pre.next = cur
            pre = cur
            if not head:
                head = cur
            root = node.right
    return head


if __name__ == '__main__':
    test = TreeNode(4)
    test.left = TreeNode(2)
    test.right = TreeNode(6)
    test.left.left = TreeNode(1)
    test.left.right = TreeNode(3)
    test.right.left = TreeNode(5)
    test.right.right = TreeNode(7)

    res = convert(test)
    outs = []
    while res:
        outs.append(res.val)
        res = res.next
    assert outs == [1, 2, 3, 4, 5, 6, 7]
