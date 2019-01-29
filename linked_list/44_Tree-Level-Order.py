#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/29'

Given a tree, write a function that prints out the nodes of the tree in level order.
'''


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    res, queue = [], root and [root]
    while queue:
        cur = queue.pop(0)
        res.append(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return res


if __name__ == '__main__':
    test = TreeNode(1)
    test.left = TreeNode(2)
    test.right = TreeNode(3)
    test.left.left = TreeNode(4)
    test.left.right = TreeNode(5)
    test.right.left = TreeNode(6)
    test.right.right = TreeNode(7)

    assert level_order(test) == [1, 2, 3, 4, 5, 6, 7]
