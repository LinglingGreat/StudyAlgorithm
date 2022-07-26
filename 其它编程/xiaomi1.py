# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 18:58
# @Author  : Liling
"""
现在有一幅扑克牌，去掉大小王52张牌。随机选出4张牌，可以任意改变扑克牌的顺序，并填入 + - * / 四个运算符，不用考虑括号，除法按整数操作，计算过程中没有浮点数，问是否能够求值得到给定的数m。

输入
一行四个数字 （JQK 分别被替换成11，12，13）单空格分割，另一行输入 m

输出
可以输出1

否则输出0


样例输入
13 13 13 13
24
样例输出
0

Hint
注意运算符优先级
"""
numlist = list(map(int, input().split()))
m = int(input())


def tryst(numlist, m):
    if len(numlist) == 1:
        if numlist[0] == m:
            return 1
        else:
            return 0
    for i in range(len(numlist)):
        if tryst(numlist[:i]+numlist[i+1:], m*numlist[i]) or tryst(numlist[:i]+numlist[i+1:], m//numlist[i]) or tryst(numlist[:i]+numlist[i+1:], m+numlist[i]) or tryst(numlist[:i]+numlist[i+1:], m-numlist[i]):
            print(numlist[i], m)
            return 1
    return 0

print(tryst(numlist, m))