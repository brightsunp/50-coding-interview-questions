#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/12'

Given a string, write a function to compress it by shortening every sequence of the same character to that character followed by the number of repetitions. If the compressed string is longer than the original, you should return the original string.

compress(“a”) = "a"
compress(“aaa”) = "a3"
compress(“aaabbb”) = "a3b3"
compress(“aaabccc”) = "a3b1c3"
'''


def compress(s):
    # count and say
    res = ''
    pre, count = '#', 0
    for i in range(len(s)):
        if s[i] == pre:
            count += 1
        else:
            if pre != '#':
                res += pre + str(count)
            pre, count = s[i], 1
        if i == len(s)-1:
            res += pre + str(count)
    return res if len(res) <= len(s) else s


if __name__ == '__main__':
    assert compress('a') == 'a'
    assert compress('aa') == 'a2'
    assert compress('aaabccc') == 'a3b1c3'
