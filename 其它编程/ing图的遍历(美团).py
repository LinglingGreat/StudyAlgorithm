# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
"""
图的遍历
给定一张包含N个点、N-1条边的无向连通图，节点从1到N编号，每条边的长度均为1。假设你从1号节点出发并打算遍历所有节点，那么总路程至少是多少？
https://www.nowcoder.com/discuss/104837
"""
import sys

n = int(sys.stdin.readline().strip())
edgearray = [[0]*(n+1) for i in range(n+1)]
print(edgearray)
for n in range(n-1):
    line = sys.stdin.readline().strip()
    a = list(map(int, line.split()))
    edgearray[a[0]][a[1]] = 1
    edgearray[a[1]][a[0]] = 1


