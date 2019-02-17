#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/17'

Given a binary tree, write a function to determine whether the tree is balanced.

- all branches are same height(±1).
- all subtrees are balanced.
'''


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root):
    return _balanced_height(root) > -1


def _balanced_height(root):
    if not root:
        return 0
    h1 = _balanced_height(root.left)
    h2 = _balanced_height(root.right)
    if h1 == -1 or h2 == -1:
        return -1
    if abs(h1-h2) > 1:
        return -1
    return max(h1, h2) + 1
