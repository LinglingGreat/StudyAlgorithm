import pandas as pd 
import numpy as np 

#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    a = sys.stdin.readline().strip().split()
    n, k = int(a[0]), int(a[1])
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    height = list(map(int, line.split()))
    movelist = []
    i = 0
    maxv = max(height)
    minv = min(height)
    while i < k or maxv!=minv:
        maxvi = height.index(maxv)
        minvi = height.index(minv)
        movelist.append([maxvi, minvi])
        height[maxvi] -= 1
        height[minvi] += 1
        i += 1
        maxv = max(height)
        minv = min(height)
    print(max(height)-min(height), i)
    for j in movelist:
        print(j[0]+1, j[1]+1)
