# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 9:26
# @Author  : Liling
# @File    : toutiao.py
# @Software: PyCharm
#coding=utf-8
import sys
a = sys.stdin.readline().strip().split()
n, t = int(a[0]),int(a[1])
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
values = values * t
sortvalues = sorted(values)
maxl = 0
for i in range(len(values)):
    v = values[i]
    l = [v]
    for j in values[i+1:]:
        if j >= v:
            l.append(j)
            v = j
    if len(l)>maxl:
        maxl = len(l)
        maxlist = l
print(maxl)
print(maxlist)
