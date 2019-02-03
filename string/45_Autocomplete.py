#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/3'

Write an autocomplete class that returns all dictionary words with a given prefix.

dict:   {"abc", "acd", "bcd", "def", "a", "aba"}
prefix: "a" -> "abc", "acd", "a", "aba"
prefix: "b" -> "bcd"

Notes: fetch all words recursively.
'''
from collections import Counter


class Trie(object):
    def __init__(self, words):
        self.d = {}
        self._build(words)

    def autocomplete(self, prefix):
        res = []
        cur = self.d
        for char in prefix:
            cur = cur.get(char)
            if not cur:
                return res
        self._fetch(cur, res)
        return res

    def _build(self, words):
        for word in words:
            cur = self.d
            for char in word:
                cur = cur.setdefault(char, {})
            cur['#'] = word

    def _fetch(self, cur, res):
        for k, v in cur.items():
            if k == '#':
                res.append(v)
            else:
                self._fetch(v, res)


if __name__ == '__main__':
    test = {"abc", "acd", "bcd", "def", "a", "aba"}
    trie = Trie(test)

    assert Counter(trie.autocomplete('a')) == Counter(["abc", "acd", "a", "aba"])
    assert Counter(trie.autocomplete('b')) == Counter(['bcd'])
    assert Counter(trie.autocomplete('ab')) == Counter(['abc', 'aba'])
