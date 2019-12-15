# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
import sys
import math


def getent(ylis):
    entd = 0
    for i in [0, 1]:
        pi = ylis.count(i) / len(ylis)
        if pi != 0:
            entd += pi * math.log(pi, 2)
    return -entd


n = int(sys.stdin.readline().strip())
xlist = []
ylist = []
for i in range(n):
    line = sys.stdin.readline().strip()
    x,y = list(map(int, line.split(',')))
    xlist.append(int(x))
    ylist.append(int(y))

feature = set(xlist)
entdy = getent(ylist)
entdx = 0
for i in feature:
    px = xlist.count(i)/n
    yl = [ylist[j] for j in range(n) if xlist[j] == i]
    entdx += px*getent(yl)
gain = entdy - entdx
print(float('%.2f' % gain))

