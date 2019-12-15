# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
"""
合法UTF8编码
"""
import sys


def hefa():
    if n == 1:
        if ''.join(binlist).startswith('0'):
            return 1
    else:
        if not ''.join(binlist).startswith('1' * n + '0'):
            return 0
        for i in range(1, n):
            if not binlist[i].startswith('10'):
                return 0
    return 1

n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
arraylist = list(map(int, line.split()))
binlist = []
for a in arraylist:
    b = bin(a)[2:]
    b = b if len(b) == 8 else '0'*(8-len(b))+b
    binlist.append(b)
print(hefa())
