# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 18:53
# @Author  : Liling
"""
题目描述：
给定一维数组，要求找出数组中一个数，使得该数等于左边之和同时也等于右边之和，如有多个仅输出第一个，如果没有返回False

输入
每行数字（int类型）为一个数组
数组元素用逗号分隔
输出
要求输出为一个数字，或者False

样例输入
3,1,4,4
样例输出
4

Hint
请注意性能，类类型转换
"""
line = input()
array = list(map(int, line.split(',')))
n = len(array)
nsum = array[0]
msum = sum(array[1:])
for i in range(1, n):
    msum = msum - array[i]
    if array[i] == nsum == msum:
        print(array[i])
        break
    nsum = nsum + array[i]
else:
    print('False')