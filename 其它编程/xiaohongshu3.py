# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 18:30
# @Author  : Liling
"""

"""
import sys

def com(n,m,oldn):
    nlen = len(n)
    res = 0
    res += (nlen-1)*(10**(nlen-2))
    if nlen > 2:
        res += com(n[1:], m, oldn)
    else:
        n = int(oldn)
        for i in range(m+1, n+1):
            res += list(str(i)).count('1')
    return int(res)


n = sys.stdin.readline().strip()
nlen = len(n)
# m = 10 ** (nlen - 1)
# print(com(n,m,n))

res = 0
n = int(n)
m = 10**(nlen-1)
for i in range(m, n+1):
    res += list(str(i)).count('1')
res += (nlen-1)*10**(nlen-2)
print(int(res))


# for i in range(nlen):
#     ans *= (int(n[i])+1)
# for i in range(nlen):
#     if int(n[i]) >= 1:
#         res += ans/(int(n[i])+1)
# print(int(res))

