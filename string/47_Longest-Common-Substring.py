#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/7'

Given two strings, write a function that returns the longest common substring.

longestSubstring("ABAB", "BABA") = "ABA"
'''


def lcs1(s1, s2):
    # brute
    l1, l2 = len(s1), len(s2)
    start, max_len = 0, 0
    for i in range(l1):
        for j in range(l2):
            cur1, cur2, cur_len = i, j, 0
            while cur1 < l1 and cur2 < l2 and s1[cur1] == s2[cur2]:
                cur1, cur2, cur_len = cur1+1, cur2+1, cur_len+1
            if cur_len > max_len:
                start, max_len = i, cur_len
    return s1[start:start+max_len]


def lcs2(s1, s2):
    # dp(cache)
    l1, l2 = len(s1), len(s2)
    end, max_len = 0, 0
    cache = [[0 for _ in range(l2)] for _ in range(l1)]
    for i in range(l1):
        for j in range(l2):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    cache[i][j] = 1
                else:
                    cache[i][j] = cache[i-1][j-1] + 1
            if cache[i][j] > max_len:
                end, max_len = i+1, cache[i][j]
    return s1[end-max_len:end]


if __name__ == '__main__':
    for lcs in [lcs1, lcs2]:
        assert lcs('ABC', 'DEF') == ''
        assert lcs('ABAB', 'BABA') == 'ABA'
        assert lcs('ABAB', 'BABAB') == 'ABAB'
