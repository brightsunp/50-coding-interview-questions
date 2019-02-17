#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/17'

Given a binary tree, write a function to test if the tree is a binary search tree.
'''
import sys


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_bst(root):
    return _helper(root, -sys.maxsize-1, sys.maxsize)


def _helper(node, a, b):
    if not node:
        return True
    if node.val < a or node.val > b:
        return False
    return _helper(node.left, a, node.val) and _helper(node.right, node.val, b)
