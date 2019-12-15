# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 14:43
# @Author  : Liling
"""
比较两个版本字符串version1和version2
题目描述：
如果version1 > version2 返回1，如果 version1 < version2 返回-1，不然返回0.

输入的version字符串非空，只包含数字和字符.。.字符不代表通常意义上的小数点，只是用来区分数字序列。例如字符串2.5并不代表二点五，只是代表版本是第一级版本号是2，第二级版本号是5.

输入
两个字符串，用空格分割。

每个字符串为一个version字符串，非空，只包含数字和字符.

输出
只能输出1, -1，或0


样例输入
0.1 1.1
样例输出
-1
"""
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def compareVersionNumber():
    v1, v2 = list(map(str, input().split()))
    v1 = list(v1.split('.'))
    v2 = list(v2.split('.'))
    n1 = len(v1)
    n2 = len(v2)
    n = min(n1, n2)
    for i in range(n):
        if int(v1[i]) < int(v2[i]):
            return -1
        elif int(v1[i]) > int(v2[i]):
            return 1
    if n1>n2:
        return 1
    elif n1<n2:
        return -1
    return 0


# ******************************结束写代码******************************


res = compareVersionNumber()

print(str(res) + "\n")
