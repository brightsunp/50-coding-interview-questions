#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/26'

Given a binary search tree, print out the elements of the tree in order without using recursion.
'''


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    res, stack = [], []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmp = stack.pop()
            res.append(tmp.val)
            root = tmp.right
    return res


if __name__ == '__main__':
    test = TreeNode(5)
    test.left = TreeNode(2)
    test.left.left = TreeNode(1)
    test.left.right = TreeNode(3)
    test.right = TreeNode(7)
    test.right.left = TreeNode(6)
    test.right.right = TreeNode(8)

    assert inorder_traversal(test) == [1, 2, 3, 5, 6, 7, 8]
