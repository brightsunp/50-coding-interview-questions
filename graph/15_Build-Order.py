#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/20'

Given a list of packages that need to be built and the dependencies for each package, determine a valid order in which to build the packages.

0:
1: 0
2: 0
3: 1, 2
4: 3

output: 4, 3, 1, 2, 0
'''
from collections import defaultdict


class Graph(object):
    def __init__(self, n_vertices):
        self.graph = defaultdict(list)
        self.V = n_vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def top_sort(self):
        indegrees = [0 for _ in range(self.V)]
        for i in self.graph:
            for j in self.graph[i]:
                indegrees[j] += 1
        queue = []
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
        order = []
        while queue:
            u = queue.pop(0)
            order.append(u)
            for i in self.graph[u]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
        return order


if __name__ == '__main__':
    test = Graph(5)
    test.add_edge(1, 0)
    test.add_edge(2, 0)
    test.add_edge(3, 1)
    test.add_edge(3, 2)
    test.add_edge(4, 3)

    assert test.top_sort() == [4, 3, 1, 2, 0]
