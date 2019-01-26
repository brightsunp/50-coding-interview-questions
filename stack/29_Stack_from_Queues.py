#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/26'

Implement a LIFO stack with basic functionality (push and pop) using FIFO queues to store the data.
'''


class Stack(object):
    def __init__(self):
        self.store = []

    def push(self, x):
        self.store.append(x)
        for _ in range(len(self.store) - 1):
            self.store.append(self.store.pop(0))

    def pop(self):
        if not self.store:
            raise IndexError
        return self.store.pop(0)


if __name__ == '__main__':
    stack = Stack()

    stack.push(1)
    stack.push(3)
    stack.push(5)
    assert stack.pop() == 5
    stack.push(5)
    assert stack.pop() == 5
    assert stack.pop() == 3
    assert stack.pop() == 1

    try:
        stack.pop()
    except Exception as e:
        assert type(e) == IndexError
