# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 10:55
# @Author  : Liling
"""
奇虎360 2017春招 分金子
A、B两伙马贼意外地在一片沙漠中发现了一处金矿，双方都想独占金矿，但各自的实力都不足以吞下对方，经过谈判后，双方同意用一个公平的方式来处理这片金矿。处理的规则如下：他们把整个金矿分成n段，由A、B开始轮流从最左端或最右端占据一段，直到分完为止。
马贼A想提前知道他们能分到多少金子，因此请你帮忙计算他们最后各自拥有多少金子?（两伙马贼均会采取对己方有利的策略）
输入
测试数据包含多组输入数据。输入数据的第一行为一个正整数T(T<=20)，表示测试数据的组数。然后是T组测试数据，每组测试数据的第一行包含一个整数n，下一行包含n个数（n <= 500 ），表示每段金矿的含金量，保证其数值大小不超过1000。
输出
对于每一组测试数据，输出一行"Case #id: sc1 sc2"，表示第id组数据时马贼A分到金子数量为sc1，马贼B分到金子数量为sc2。详见样例。
样例输入
2
6
4 7 2 9 5 2
10
140 649 340 982 105 86 56 610 340 879
样例输出
Case #1: 18 11
Case #2: 3206 981

解法：
考虑先手和后手在序列a(1); a(2);……; a(n)上博弈：
  ① 如果先手取走了a1，那么问题转化成了两个人在a(2); a(3);……; a(n)上的博弈。
  ② 如果先手取走an，就变成了在a(1); a(2);……; a(n-1)上的博弈。
"""
import sys

if __name__ == "__main__":
    # 读取第一行的t
    t = int(sys.stdin.readline().strip())
    result = []
    for x in range(t):
        # 读取每一行
        n = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        golds = list(map(int, line.split()))
        if n % 2 == 0:
            dp = [[0 for i in range(n)] for j in range(n)]
            for i in range(n - 1, -1, -1):
                for j in range(i, n):
                    if i != j:
                        if (j - i) % 2 == 1:
                            dp[i][j] = max(dp[i + 1][j] + golds[i], dp[i][j - 1] + golds[j])
                        else:
                            dp[i][j] = min(dp[i + 1][j], dp[i][j - 1])

        else:
            dp = [[golds[i] if i == j else 0 for i in range(n)] for j in range(n)]
            for i in range(n - 1, -1, -1):
                for j in range(i, n):
                    if i != j:
                        if (j - i) % 2 == 1:
                            dp[i][j] = min(dp[i + 1][j], dp[i][j - 1])
                        else:
                            dp[i][j] = max(dp[i + 1][j] + golds[i], dp[i][j - 1] + golds[j])

        print("Case #%d: " % x + str(dp[0][n - 1]) + " " + str(sum(golds) - dp[0][n - 1]))



def main():
    case = int(sys.stdin.readline().strip())
    for c in range(case):
        n = int(sys.stdin.readline().strip())
        au = list(map(int, sys.stdin.readline().strip().split()))   # 金子序列

        f = [[0 for i in range(n + 1)] for j in range(n + 1)]   # f[i][j]纪录在序列[i,j]中先手能拿到的最多金子
        sum = [0 for i in range(n + 1)]

        # 计算前i份金子的数量之和
        for i in range(1, n + 1):
            sum[i] = sum[i - 1] + au[i - 1]
            f[i][i] = au[i-1]

        for j in range(n):
            for i in range(1, n):
                if i + j <= n:
                    # sum[i+j]-sum[i-1]表示[i,j]这个序列的金子总数,f[i+1][i+j]表示先手拿走第i+1个金子后后手能拿到的最多金子
                    f[i][i + j] = sum[i + j] - sum[i - 1] - min(f[i + 1][i + j], f[i][i + j - 1])

        print('Case #%d: %d %d'%(c + 1, f[1][n], sum[n] - f[1][n]))

