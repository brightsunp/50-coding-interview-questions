#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/3'

Given a string and a dictionary HashSet, write a function to determine the minimum number of characters to delete to make a word.

dictionary: [“a”, “aa”, “aaa”]
query: “abc”
output: 2

Notes: delete one character each time.
'''


def min_deletion(bag, word):
    queue, uniques = [word], {word}
    while queue:
        cur = queue.pop(0)
        if cur in bag:
            return len(word) - len(cur)
        for i in range(len(cur)):
            nxt = cur[:i] + cur[i+1:]
            if nxt and nxt not in uniques:
                queue.append(nxt)
                uniques.add(nxt)
    return -1


if __name__ == '__main__':
    test = {'a', 'aa', 'aaa'}

    assert min_deletion(test, 'abc') == 2
    assert min_deletion(test, 'bac') == 2
    assert min_deletion(test, 'aba') == 1
    assert min_deletion(test, 'd') == -1
