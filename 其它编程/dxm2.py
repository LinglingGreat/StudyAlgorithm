# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 14:56
# @Author  : Liling
"""
n个点连成一条链，从左往右依次从1到n编号。相邻点之间有边相连，一共有n-1条边。所有的边从1到n-1编号，第i条边连接了点i和i+1。

第i个点有点权ai，定义第i条边的权重为wi：有多少点对x，y满足在第i条边的左侧（x≤i），y在第i条边的右侧（y>i），且x和y的点权不同。

给出每个点的点权，请求出所有边的边权。

输入
第一行输入一个数n。(2≤n≤100000)

第二行输入n个数，a1,a2,…,an (1≤ai≤109)

输出
输出n-1个数，依次为每条边的权重，不要在行末输出多余的空格。


样例输入
3
1 2 1
样例输出
1 1
"""
n = int(input())
alist = list(map(int, input().split()))
tlist = [[0 for i in range(n)] for j in range(n-1)]
wlist = [0]*(n-1)
for i in range(n-1):
    for j in range(n):
        tlist[i][j] = (0 if alist[j] == alist[i] else 1)
for i in range(n-1):
    wlist[i] += sum(tlist[i][i+1:])
    for j in range(i):
        wlist[i] += sum(tlist[j][i+1:])

# for i in range(n-1):
#     left = alist[:i+1]
#     right = alist[i+1:]
#     for j in left:
#         wlist[i] += len([k for k in right if k != j])
print(' '.join(str(i) for i in wlist))
