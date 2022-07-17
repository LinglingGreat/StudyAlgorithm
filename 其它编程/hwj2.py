# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 10:28
# @Author  : Liling
import sys
n = int(sys.stdin.readline().strip())
a = sys.stdin.readline().strip()
a = list(map(int, a.split()))
b = sys.stdin.readline().strip()
b = list(map(int, b.split()))
taga = [0]*n
tagb = [0]*n
res = 0
# setb = [0]*n
# anb = [i for i in a if i not in b]
# for i in range(n):
#     if setb[b[i]] == 0:
#         setb[b[i]] = 1
#     else:
#         b[i] = anb[0]
#         break
for i in range(n):
    for j in range(n):
        if a[i] == b[j] and taga[i] == 0 and tagb[j] == 0:
            taga[i] = 1
            tagb[j] = 1
            res += 1
flag = 0
for i in range(n):
    for j in range(n):
        if taga[i] == 0 and tagb[j] == 0:
            res += 1
            flag = 1
            break
    if flag == 1:
        break
print(res)
