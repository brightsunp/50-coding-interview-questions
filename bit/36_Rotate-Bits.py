#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/1/27'

Given a number, write a function to rotate the bits (ie circular shift).

rotate(0xFFFF0000, 8) = 0x00FFFF00
rotate(0x13579BDF, 12) = 0xBDF13579
rotate(0b10110011100011110000111110000000, 15) = 0b00011111000000010110011100011110
'''


def rotate(xnum, k):
    # last k bits, first (32-k) bits
    res = xnum & ((1 << k) - 1)
    res = (res << (32 - k)) | (xnum >> k)
    return res


if __name__ == '__main__':
    assert rotate(0xFFFF0000, 8) == 0x00FFFF00
    assert rotate(0x13579BDF, 12) == 0xBDF13579
    assert rotate(0b10110011100011110000111110000000, 15) == 0b00011111000000010110011100011110
