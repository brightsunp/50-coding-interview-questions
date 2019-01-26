#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/26'

Given two strings, write a function to determine whether they are anagrams.

isAnagram("", "") = true
isAnagram("A", "A") = true
isAnagram("A", "B") = false
isAnagram("ab", "ba") = true
isAnagram("AB", "ab") = true

Notes: ignore uppercase and characters' order
'''


def is_anagram(s1, s2):
    # counting array[128]
    if len(s1) != len(s2):
        return False
    counts = [0 for _ in range(128)]
    for c in s1.lower():
        counts[ord(c)] += 1
    for c in s2.lower():
        counts[ord(c)] -= 1
    return not any(counts)


if __name__ == '__main__':
    assert is_anagram('', '')
    assert is_anagram('A', 'A')
    assert not is_anagram('A', 'B')
    assert is_anagram('ab', 'ba')
    assert is_anagram('AB', 'ab')
