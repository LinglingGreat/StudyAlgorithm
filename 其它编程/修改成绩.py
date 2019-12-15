# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
"""
题目描述：
华老师的n个学生参加了一次模拟测验，考出来的分数很糟糕，但是华老师可以将成绩修改为[0,100]中的任意值，所以他想知道，如果要使所有人的成绩的平均分不少于X分，至少要改动多少个人的分数？

输入
第一行一个数T，共T组数据（T≤10）

接下来对于每组数据：

第一行两个整数n和X。（1≤n≤1000, 0≤X≤100）

第二行n个整数，第i个数Ai表示第i个学生的成绩。（0≤Ai≤100）

输出
共T行，每行一个整数，代表最少的人数。


样例输入
2
5 60
59 20 30 90 100
5 60
59 20 10 10 100
样例输出
1
2

Hint
对于第一组数据，将59改成60即可
"""

t = int(input())
for i in range(t):
    n, x = list(map(int, input().split()))
    score = list(map(int, input().split()))
    s = sum(score)
    if s >= x*n:
        print(0)
        continue
    cs = x*n - s
    score = sorted(score)
    i = 0
    while cs > 0 and i<n:
        adds = min(100-score[i], cs)
        cs -= adds
        i += 1
    print(i)