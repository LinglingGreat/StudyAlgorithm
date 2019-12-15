# -*- coding: utf-8 -*-
# @Author  : Liling
"""
360 2018年秋招笔试
小明有一个花园，花园里面一共有m朵花，对于每一朵花，都是不一样的，小明用1～m中的一个整数表示每一朵花。
他很喜欢去看这些花，有一天他看了n次，并将n次他看花的种类是什么按照时间顺序记录下来。
记录用a[i]表示，表示第i次他看了a[i]这朵花。
小红很好奇，她有Q个问题,问[l,r]的时间内，小明一共看了多少朵不同的花儿，小明因为在忙着欣赏他的花儿，所以想请你帮他回答这些问题。

输入
输入两个数n,m;(1<=n<=2000,1<=m<=100);分别表示n次看花，m表示一共有m朵花儿。
接下来输入n个数a[1]~a[n]，a[i]表示第i次，小明看的花的种类;
输入一个数Q(1<=Q<=1000000);表示小红的问题数量。
输入Q行 每行两个数 l,r(1<=l<=r<=n); 表示小红想知道在第l次到第r次，小明一共看了多少不同的花儿。
输出
一共Q行
每一行输出一个数 表示小明在[l,r]的时间内看了多少种花。

样例输入
5 3
1 2 3 2 2
3
1 4
2 4
1 5
样例输出
3
2
3

"""
import sys

if __name__ == "__main__":
    # 读取第一行的t
    t = sys.stdin.readline().strip().split()
    n, m = int(t[0]), int(t[1])
    line = sys.stdin.readline().strip()
    a = list(map(int, line.split()))
    q = int(sys.stdin.readline().strip())
    for i in range(q):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        apart = a[values[0]-1:values[1]]
        print(len(set(apart)))