#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/13'

Implement a binary tree with a method getRandomNode() that returns a random node.

getRandomNode() = 5
getRandomNode() = 8
getRandomNode() = 1
'''
from random import randint


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def random_node(root):
    # LevelOrder + ReservoirSampling
    r, i = None, 0
    queue = root and [root]
    while queue:
        cur = queue.pop(0)
        if randint(0, i) == 0:
            r = cur
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
        i += 1
    return r


if __name__ == '__main__':
    test = TreeNode(1)
    test.left = TreeNode(2)
    test.right = TreeNode(3)
    test.left.left = TreeNode(4)
    test.left.right = TreeNode(5)
    test.right.left = TreeNode(6)
    test.right.right = TreeNode(7)

    n_experiments = 100000
    res_probability = 1 / 7
    res_arr = [0 for _ in range(7)]
    for _ in range(n_experiments):
        res = random_node(test)
        res_arr[res.val-1] += 1
    for res in res_arr:
        assert round(res / n_experiments, 2) == round(res_probability, 2)
