# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
"""
抖音红人的数量
"""
import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
line = list(map(int, line.split()))
if n == 1:
    print(1)
else:
    array = [[0]*(n+1) for i in range(n+1)]
    for i in range(0, m*2-1, 2):
        x = line[i]
        y = line[i+1]
        array[x][y] = 1
    for i in range(n+1):
        array[i][i] = 1
    for i in range(n+1):
        for j in range(n+1):
            if array[i][j] == 1:
                for x in range(n+1):
                    if array[j][x] == 1:
                        array[i][x] = 1

    array = list(map(list, zip(*array)))
    hr = 0
    for i in range(n+1):
        if array[i].count(1) == n:
            hr += 1
    print(hr)
