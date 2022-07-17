# -*- coding: utf-8 -*-
# @Time    : 2018/9/16 14:20
# @Author  : Liling
"""
腾讯90%
A，B两个字符串，统计A中所有长度为k的子串在B中出现的次数之和
"""
import sys
from collections import defaultdict
k = int(sys.stdin.readline().strip())
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
asubstr = list(set([a[j:j+k] for j in range(len(a)-k+1)]))
bdic = defaultdict(int)
for i in range(len(b)-k+1):
    bdic[b[i:i+k]] += 1
print(sum([bdic[i] for i in asubstr]))

"""
别人的AC代码
"""
k = int(input().strip())
A = input().strip()
B = input().strip()
la = len(A)
lb = len(B)


def getnext(ps):
    nextarr = [-1 for i in range(len(ps))]
    nextarr[0] = -1
    j = 0
    k = -1
    while j < len(ps)-1:
        if k == -1 or (k >= 0 and ps[j] == ps[k]):
            j += 1
            k += 1
            if ps[j] == ps[k]:
                nextarr[j] = nextarr[k]
            else:
                nextarr[j] = k
        else:
            k = nextarr[k]
    return nextarr


def kmp(ts, ps):
    i, j = 0, 0
    nextarr = getnext(ps)
    count = 0
    while i < len(ts):
        if j == -1 or ts[i] == ps[j]:
            i += 1
            j += 1
        else:
            j = nextarr[j]
        if j == len(ps):
            i = i-j+1
            j = 0
            count += 1
    return count


zichuan = {}
i = 0
res = 0
while i < la-k+1:
    cur = A[i:i+k]   # 当前子串
    if cur not in zichuan:
        zichuan[cur] = 1
        count = kmp(B, cur)   # 统计子串在B中的出现次数
        res += count
    i += 1
print(res)
