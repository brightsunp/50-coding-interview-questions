#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/12'

Implement a Priority Queue
'''


class PriorityQueue(object):
    '''lowest first'''
    def __init__(self):
        self._queue = []

    def size(self):
        return len(self._queue)

    def push(self, item, priority):
        self._queue.append((item, priority))
        self._shiftup(self.size()-1)

    def pop(self):
        last = self._queue.pop()
        if self._queue:
            top = self._queue[0]
            self._queue[0] = last
            self._shiftdown(0)
            return top[0]
        return last[0]

    def _shiftdown(self, pos):
        item, prior = self._queue[pos]
        childpos = (pos << 1) + 1
        while childpos < self.size():
            if childpos < self.size()-1 and self._queue[childpos+1][1] < self._queue[childpos][1]:
                childpos += 1
            if prior <= self._queue[childpos][1]:
                break
            self._queue[pos] = self._queue[childpos]
            pos = childpos
            childpos = (pos << 1) + 1
        self._queue[pos] = (item, prior)

    def _shiftup(self, pos):
        item, prior = self._queue[pos]
        parentpos = (pos - 1) >> 1
        while parentpos >= 0:
            if prior >= self._queue[parentpos][1]:
                break
            self._queue[pos] = self._queue[parentpos]
            pos = parentpos
            parentpos = (pos - 1) >> 1
        self._queue[pos] = (item, prior)


if __name__ == '__main__':
    test = PriorityQueue()
    test.push('fourth', 4)
    test.push('first', 1)
    test.push('second', 2)
    test.push('third', 3)

    assert test.size() == 4
    assert test.pop() == 'first'
    assert test.size() == 3
    assert test.pop() == 'second'
    assert test.pop() == 'third'
    assert test.pop() == 'fourth'
