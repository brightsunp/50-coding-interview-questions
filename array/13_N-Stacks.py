#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/26'

Implement N > 0 stacks using a single array to store all stack data (you may use auxiliary arrays in your stack object, but all of the objects in all of the stacks must be in the same array). No stack should be full unless the entire array is full.

N = 3;
capacity = 10;
Stacks stacks = new Stacks(N, capacity);
stacks.push(0, 10);
stacks.push(2, 11);
stacks.pop(0) = 10;
stacks.pop(2) = 11;
'''


class Stacks2(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.top1 = -1
        self.top2 = capacity
        self.store = [None] * capacity

    def push(self, id, num):
        if self.top1 == self.top2 - 1:
            raise OverflowError('Stack Overflow!')

        if id == 1:
            self.top1 += 1
            self.store[self.top1] = num
        else:
            self.top2 -= 1
            self.store[self.top2] = num

    def pop(self, id):
        # no need to remove self.store[top]
        if (id == 1 and self.top1 == -1) or (id == 2 and self.top2 == self.cap):
            raise OverflowError('Stack Underflow!')

        if id == 1:
            num = self.store[self.top1]
            self.top1 -= 1
            return num
        else:
            num = self.store[self.top2]
            self.top2 += 1
            return num


class StacksK(object):
    def __init__(self, N, capacity):
        self.k = N
        self.cap = capacity
        self.avail = 0
        self.tops = [-1 for _ in range(N)]
        self.avails = [i+1 for i in range(capacity-1)]
        self.avails.append(-1)
        self.store = [None] * capacity

    def push(self, id, num):
        if id not in range(self.k):
            raise IndexError
        if self.avail == -1:
            raise OverflowError('Stack Overflow!')

        cur = self.avail
        self.store[cur] = num
        self.avail = self.avails[cur]
        self.avails[cur] = self.tops[id]
        self.tops[id] = cur

    def pop(self, id):
        # reverse push
        if id not in range(self.k):
            raise IndexError
        if self.tops[id] == -1:
            raise OverflowError('Stack Underflow!')

        top = self.tops[id]
        self.tops[id] = self.avails[top]
        self.avails[top] = self.avail
        self.avail = top
        return self.store[top]


if __name__ == '__main__':
    test = StacksK(3, 10)
    test.push(0, 10)
    test.push(2, 11)

    assert test.pop(0) == 10
    assert test.pop(2) == 11

    try:
        test.pop(1)
    except Exception as e:
        assert type(e) == OverflowError
        assert str(e) == 'Stack Underflow!'
    else:
        print('OverflowError not raised.')
