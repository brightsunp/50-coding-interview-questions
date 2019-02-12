#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/12'

Given a list of strings, write a function to get the kth most frequently occurring string.

kthMostFrequent({"a","b","c","a","b","a"}, 0) = "a"
kthMostFrequent({"a","b","c","a","b","a"}, 1) = "b"
kthMostFrequent({"a","b","c","a","b","a"}, 2) = "c"
kthMostFrequent({"a","b","c","a","b","a"}, 3) = null
'''


def kth_frequent(arr, k):
    # hashmap
    d = {}
    for s in arr:
        d[s] = d.get(s, 0) + 1
    items = sorted(d.items(), key=lambda item: item[1], reverse=True)
    if k >= len(items):
        return None
    return items[k][0]


if __name__ == '__main__':
    assert kth_frequent(['a', 'b', 'c', 'a', 'b', 'a'], 0) == 'a'
    assert kth_frequent(['a', 'b', 'c', 'a', 'b', 'a'], 1) == 'b'
    assert kth_frequent(['a', 'b', 'c', 'a', 'b', 'a'], 2) == 'c'
    assert not kth_frequent(['a', 'b', 'c', 'a', 'b', 'a'], 3)
