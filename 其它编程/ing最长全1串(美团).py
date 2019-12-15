# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
"""
最长全1串
给你一个01字符串，定义答案=该串中最长的连续1的长度，现在你有至多K次机会，每次机会可以将串中的某个0改成1，现在问最大的可能答案
"""
import sys

line = sys.stdin.readline().strip()
n,k = list(map(int, line.split()))
line = sys.stdin.readline().strip()
astr = list(map(int, line.split()))
maxlen = 0
for i in range(n):
    ik = 0
    ilen = 0
    j = i
    while astr[j] == 1 or ik < k:
        if astr[j] == 0:
            ik += 1
        ilen += 1
        j += 1
        if j>=n:
            break
    maxlen = max(maxlen, ilen)
print(maxlen)

