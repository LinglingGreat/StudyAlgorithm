# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 10:55
# @Author  : Liling
"""
奇虎360 2017春招 剪气球串
小明买了一些彩色的气球用绳子串在一条线上，想要装饰房间，每个气球都染上了一种颜色，每个气球的形状都是各不相同的。我们用1到9一共9个数字表示不同的颜色，如12345则表示一串5个颜色各不相同的气球串。但小明希望得到不出现重复颜色的气球串，那么现在小明需要将这个气球串剪成多个较短的气球串，小明一共有多少种剪法？如原气球串12345的一种是剪法是剪成12和345两个气球串。
注意每种剪法需满足最后的子串中气球颜色各不相同（如果满足该条件，允许不剪，即保留原串）。两种剪法不同当且仅当存在一个位置，在一种剪法里剪开了，而在另一种中没剪开。详见样例分析。

输入
第一行输入一个正整数n（1≤n≤100000），表示气球的数量。
第二行输入n个整数a1，a2，a3...an，ai表示该气球串上第i个气球的颜色。对于任意i，有1≤ai≤9。
输出
输出一行，第一行输出一个整数，表示满足要求的剪法，输出最终结果除以1000000007后的余数。
样例输入
3
1 2 3
样例输出
4

解法：
记数组dp[i]，表示长度为n的这个数组的前i个数组成的数组可以有多少种剪法。数组初始全为0。dp[1] = 1。
那么在计算dp[i]时，我们需要考虑第i个数可以和前面的哪些数分到一组。
1）第i个数自己一组，那么dp[i] += dp[i-1];
2）第i个数和第i-1个数一组，这个需要考虑第i和第i-1个数能不能一组，当两个数字（气球的颜色）相同时，由于要求子串中不能出现重复数字，所以不能一起，此时dp[i]计算结束；当两个气球颜色不相同时，可以一组，那么dp[i] += dp[i-2];
3）依次类推。
"""

n = int(input())
a = [int(i) for i in input().split()]
dp = [1]  # dp[i]表示长度为n的这个数组的前i个数组成的数组可以有多少种剪法
for i in range(1, n + 1):
    d = 0   # 长度为i的气球串的剪法初始化为0
    col = [0] * 10
    for j in range(i):   # 计算dp[i]
        col[a[i - j - 1]] += 1   # 统计每种颜色的气球数量
        if col[a[i - j - 1]] > 1:   # 相同颜色的气球不能在同一子串
            break
        d += dp[i - 1 - j]    # 不同颜色的气球可以在同一子串，气球i和i-j-1一组
    dp.append(d)
print(dp[-1] % 1000000007)
