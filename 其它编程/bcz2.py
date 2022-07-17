# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 19:48
# @Author  : Liling
"""
百词斩
AC
"""
import sys
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
ans = list(map(int, line.split()))
i = 0
s = 0
e = 0
length = 1
res = []
for i in range(1, n):
    if ans[i]-ans[i-1] == 1:
        length += 1
        e = i
    else:
        if e-s >= 2:
            res.append(str(ans[s])+'-'+str(ans[e]))
        else:
            res.extend(ans[s:e + 1])
        s = i
        length = 1
        e = i
if e - s >= 2:
    res.append(str(ans[s]) + '-' + str(ans[e]))
else:
    res.extend(ans[s:e + 1])
print(' '.join(str(i) for i in res))
