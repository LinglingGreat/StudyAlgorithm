# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
"""
每次最多走m个台阶，走到第n个台阶的方法个数
"""
import sys

line = sys.stdin.readline().strip()
n, m = list(map(int, line.split()))
dp = [0]*(n+1)
for i in range(1, min(n,m)+1):
    dp[i] = 1
for i in range(2, n+1):
    # if i>m+1:
    #     dp[i] += 2*dp[i-1]
    #     if i-m-1>0:
    #         dp[i] += dp[i-m-1]
    # else:
    for j in range(1, m+1):
        if i-j > 0:
            dp[i] += dp[i-j]
print(dp[n]%10007)
