# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
"""
最长不重复子串
"""
import sys

line = sys.stdin.readline().strip()
n = len(line)
maxstr = 0
for i in range(n):
    istr = [line[i]]
    j = i+1
    while j <= n-1 and line[j] not in istr:
        istr.append(line[j])
        j += 1
    maxstr =max(maxstr, len(istr))

print(maxstr)
