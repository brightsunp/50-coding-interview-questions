#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/17'

Given a linked list, write a function that prints the nodes of the list in reverse order.

printReversedList(1 -> 2 -> 3)
3
2
1
'''
from copy import deepcopy


class LinkNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_rl1(head):
    # auxiliary stack
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    while stack:
        print(stack.pop())


def print_rl2(head):
    # iterative
    new_head = None
    while head:
        tmp = head.next
        head.next = new_head
        new_head = head
        head = tmp
    while new_head:
        print(new_head.val)
        new_head = new_head.next


def print_rl3(head):
    # recursive
    if not head:
        return
    print_rl3(head.next)
    print(head.val)


if __name__ == '__main__':
    test = LinkNode(1)
    test.next = LinkNode(2)
    test.next.next = LinkNode(3)

    for print_func in [print_rl1, print_rl2, print_rl3]:
        dup = deepcopy(test)
        print('Output of {}:'.format(print_func.__name__))
        print_func(dup)
