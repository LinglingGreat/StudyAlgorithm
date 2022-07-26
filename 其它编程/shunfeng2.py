# -*- coding: utf-8 -*-
# @Time    : 2018/9/15 10:00
# @Author  : Liling
"""
顺丰 AC
数组top2和
题目描述：
输出一个整数数组中，频率最高的前2个数的和（频率一致取先出现的数字）

输入
数组长度以及数组元素

输出
频率最高的前2个数的和

样例输入
6
1
1
1
2
2
3
样例输出
3
"""
# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def topk(nums):
    if len(nums) <= 2:
        return sum(nums)
    num = list(set(nums))
    num = sorted(num, key=nums.index)
    count = []
    for i in num:
        c = nums.count(i)
        ind = nums.index(i)
        count.append([ind, c, i])
    count = sorted(count, key=lambda x: x[1], reverse=True)
    return sum(c[2] for c in count[:2])


# ******************************结束写代码******************************


_nums_cnt = 0
_nums_cnt = int(input())
_nums_i = 0
_nums = []
while _nums_i < _nums_cnt:
    _nums_item = int(input())
    _nums.append(_nums_item)
    _nums_i += 1

res = topk(_nums)

print(str(res) + "\n")

