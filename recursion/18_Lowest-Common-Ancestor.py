#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/13'

Given two nodes in a binary tree, write a function to find the lowest common ancestor.
'''


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca(root, node1, node2):
    if not root:
        return None
    if root == node1 or root == node2:
        return root
    left_res = lca(root.left, node1, node2)
    right_res = lca(root.right, node1, node2)
    if left_res and right_res:
        return root
    return left_res or right_res


if __name__ == '__main__':
    test = TreeNode(1)
    test.left = TreeNode(2)
    test.right = TreeNode(3)
    test.left.left = TreeNode(4)
    test.left.right = TreeNode(5)
    test.right.left = TreeNode(6)
    test.right.right = TreeNode(7)

    left1 = test.left.left
    left2 = test.left.right
    right1 = test.right.left
    assert lca(test, left1, right1) == test
    assert lca(test, left1, left2) == test.left
