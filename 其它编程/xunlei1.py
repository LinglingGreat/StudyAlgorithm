# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 18:53
# @Author  : Liling
"""
题目描述：
给定两个乱序数组，长度分别为M,N要求打印出和最大的K个数，和是由两个数组中各一个数相加而得。

输入
每行数字短横符-分隔两个数组,冒号分隔:参数K
输出
输出为和最大的K个数，和是两个数组中各一个数相加而得

样例输入
2,4,2,7,7-3,2,5,6,1,9:6
样例输出
16,16,13,13,13,12

Hint
注意性能
"""

line = input()
array, k = line.split(':')
k = int(k)
array1, array2 = array.split('-')
array1 = list(map(int, array1.split(',')))
array2 = list(map(int, array2.split(',')))
array1 = sorted(array1, reverse=True)
array2 = sorted(array2, reverse=True)
m = len(array1)
n = len(array2)
maxlist = []
for i in range(min(m, k)):
    for j in range(min(n, k)):
        maxlist.append(array1[i]+array2[j])
maxlist = sorted(maxlist, reverse=True)
maxlist = list(map(str, maxlist))
print(','.join(maxlist[:k]))
