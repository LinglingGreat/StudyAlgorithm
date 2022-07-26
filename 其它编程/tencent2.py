# -*- coding: utf-8 -*-
# @Time    : 2018/9/16 14:21
# @Author  : Liling
"""
腾讯AC
两个人比赛，第n轮赢了的人拿到n分。n=1,2,...
现在有两个人的分数分别是x,y，问分数为x的人至少要赢几轮才能拿到x分，并且另一个人拿到y分
"""
import sys
import math


def findn(s):
    return int(math.sqrt(s*2))


a = sys.stdin.readline().strip().split()
x, y = int(a[0]), int(a[1])
n = findn(x+y)
result = 0
if n*(n+1) != 2*(x+y):
    print(-1)
else:
    for i in range(n, 0, -1):
        if x-i >= 0:
            x -= i
            result += 1
        if x == 0:
            print(result)
            break

