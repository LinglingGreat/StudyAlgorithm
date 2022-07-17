# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 18:42
# @Author  : Liling
import sys


def merge(p1, p2):
    if not p1:
        return p2
    elif not p2:
        return p1
    n = len(p1)
    m = len(p2)
    i = 0
    j = 0
    p = []
    while i<n and j<m:
        if p1[i]<p2[j]:
            p.append(p1[i])
            i += 1
        elif p1[i]>p2[j]:
            p.append(p2[j])
            j += 1
        else:
            p.append(p1[i])
            p.append(p2[j])
            i += 1
            j += 1
    if i<n:
        p.extend(p1[i:])
    if j<n:
        p.extend(p2[j:])
    return p


line = sys.stdin.readline().strip()
a = list(map(int, line.split()))
line = sys.stdin.readline().strip()
b = list(map(int, line.split()))
print(merge(a, b))
