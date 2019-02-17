#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/17'

Given a tree, write a function to find the length of the longest branch of nodes in increasing consecutive order.
'''


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lis(root):
    if not root:
        return 0
    return max(_helper(root.left, root.val, 1), _helper(root.right, root.val, 1))


def _helper(node, pre, length):
    if not node:
        return length
    if node.val == pre + 1:
        return max(_helper(node.left, node.val, length+1), _helper(node.right, node.val, length+1))
    return max(_helper(node.left, node.val, 1), _helper(node.right, node.val, 1), length)
