# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 19:48
# @Author  : Liling
import sys
line = sys.stdin.readline().strip()
a = list(map(int, line.split(':')))
line = sys.stdin.readline().strip()
b = list(map(int, line.split(':')))
an = a[0]*3600+a[1]*60+a[2]
bn = b[0]*3600+b[1]*60+b[2]
dif = bn-an
shizhen = dif/3600/12*360
fenzhen = dif/60/60*360
miaozhen = dif/60*360
l1 = b[0]-a[0]+ (0 if b[1]>=a[1] else -1)
l2 = b[1]-a[1]+ (0 if b[2]>=a[2] else -1)
# fenzhen = (l1*60+l2)/60*360
# miaozhen = (l1*3600+l2*60)/60*360
print(int(shizhen))
print(int(fenzhen))
print(int(miaozhen))
# print(str(shizhen).split('.')[0])
# print(str(fenzhen).split('.')[0])
# print(str(miaozhen).split('.')[0])
