# -*- coding: utf-8 -*-
# @Time    : 2018/9/16 14:21
# @Author  : Liling
"""
腾讯40%
三元组，定义合法三元组(a,b,c)是可以组成三角形的三个数字，且有序，比如(3,4,5)和(3,5,4)是两个合法的三元组，而(1,2,3)不是
输入x,y,z，有多少个合法的三元组满足1<=a<=x,1<=b<=y,1<=c<=z
"""
import sys
a = sys.stdin.readline().strip().split()
x, y, z = int(a[0]), int(a[1]), int(a[2])
res = 0
x, y, z = sorted([x, y, z])
for i in range(1, x+1):
    for j in range(1, y+1):
        for k in range(1, min(i+j,z+1)):
            this = sorted([i, j, k])
            if this[0]+this[1] > this[2]:
                res += 1

print(res%1000000007)