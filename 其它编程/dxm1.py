# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 14:58
# @Author  : Liling
"""
题目描述：
有一天，小A和小B玩了一个神奇的游戏，游戏开始时，桌面上有a0个不同盒子和b0个不同的物品，每个回合，两个人可以选择增加一个新的盒子或者一个新的物品(所有物品和盒子都不同)，记当前桌子上的盒子数量为a，物品数量为b，当把b个物品放入a个盒子的方案数不小于n时，游戏结束，此时最后一位操作者判负。

给出a0，b0，n，如果小A先手，两个人都采用最优策略，谁能获胜，如果A获胜输出“A”，如果B获胜，输出“B”，如果是平局，输出“A&B”。

输入
输入第一行是一个数据组数T(T<=10)。

接下来T行，每行描述一个测试数据，包含三个整数a0,b0,n(1<=a0<=10000,1<=b0<=30,2<=n<=10^9)。分别表示桌子上初始的盒子数，球数和n值。

输出
对于每个测试数据，输出一行，仅包含一个字符串，即“A”，“B”或“A&B”。


样例输入
3
2 2 10
3 1 4
1 4 10
样例输出
B
A
A&B
"""


def boyi(b, a):
    num = a**b
    return num


t = int(input())
for i in range(t):
    a0, b0, n = list(map(int, input().split()))
    a, b = a0, b0
    num = boyi(b, a)
    i = 0
    while num < n and i<100:
        num1 = boyi(b+1, a)
        num2 = boyi(b, a+1)
        if max(num1, num2) < n:
            if num1 >= num2:
                num = num1
                a, b = a, b+1
            elif num1 < num2:
                num = num2
                a, b = a+1, b
        elif min(num1, num2) < n:
            if num1 >= num2:
                num = num2
                a, b = a+1, b+1
            elif num1 < num2:
                num = num1
                a, b = a, b+1
        else:
            num = n
            print('B' if i % 2 else 'A')
        i += 1
    if i>=100:
        print('A&B')



