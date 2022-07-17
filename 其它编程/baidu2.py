# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 18:58
# @Author  : Liling
"""
魔法师小九有n个从左到右依次排成一行的魔法石，第i个魔法石的大小为Ai，Ai在[1, 10^9]的范围内。同时使用排成一行的n个魔法石可以爆发出很大的威力，但是自己也会受到伤害，自损伤害数值为魔法石大小的逆序对个数，逆序对是指满足i<j且Ai>Aj的 (i,j) 的对数（逆序对严格按照定义，如211，则逆序对为2个）。魔法师小九希望减小伤害，他会选择且仅选择一块魔法石将其大小变成0，请问他最多可以将自损伤害数值降低到多少。

输入
第一行一个数n，表示魔法石的数量。（1≤n≤100000）

接下来一行n个数，第i个数表示Ai。（1≤Ai≤10^9）

输出
两个整数，用一个空格隔开，分别表示最小自损伤害数值和选择的魔法石序号，如果有多种最优选择方案，输出最小的魔法师序号（序号从1开始）。


样例输入
5
2 5 4 3 1
样例输出
5 2

Hint
样例解释
原逆序对数为7，将第二个魔法石变为0后，2 0 4 3 1共有5个逆序对。
"""
n = int(input())
alist = list(map(int, input().split()))
sv = 0
left = [0]*n
right = [0]*n
for j in range(n - 1):
    right[j] = len([i for i in alist[j+1:] if i < alist[j]])
    left[j] = len([i for i in alist[:j] if i > alist[j]])
    sv += right[j]
minv = float('inf')
minind = 0
for i in range(n//2):
    v = sv+i
    v -= right[i]
    v -= left[i]
    if v<minv:
        minv = v
        minind = i+1
print(minv, minind)

