# -*- coding: utf-8 -*-
"""
给你六种面额 1、5、10、20、50、100 元的纸币，假设每种币值的数量都足够多，编写程序求组成N元（N为0~10000的非负整数）的不同组合的个数。
输入描述:
输入包括一个整数n(1 ≤ n ≤ 10000)
输出描述:
输出一个整数,表示不同的组合方案数
输入例子1:
1
输出例子1:
1
https://blog.csdn.net/lizhentao0707/article/details/82414522
"""
import sys

n = int(sys.stdin.readline().strip())
molist = [1,5,10,20,50,100]
dp=[0]*n
dp[0]=1
for i in range(6):
    for j in range(molist[i],n+1):
        dp[j] += dp[j-molist[i]]
print(dp[n])

