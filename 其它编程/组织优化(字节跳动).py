# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
"""
组织优化
"""
import sys

m = int(sys.stdin.readline().strip())
arraylist = []
for i in range(m):
    line = sys.stdin.readline().strip()
    al = list(map(int, line.split()))
    for j in range(len(al)):
        if al[j] == 1:
            for x in range(len(arraylist)):
                if ((i+1,j) in arraylist[x]) or ((i-1,j) in arraylist[x]) or ((i,j+1) in arraylist[x]) or ((i,j-1) in arraylist[x]):
                    arraylist[x].append((i,j))
                    break
            else:
                arraylist.append([(i,j)])

print(len(arraylist))

