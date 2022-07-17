# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 19:48
# @Author  : Liling
import sys
line = sys.stdin.readline().strip()
findkey = sys.stdin.readline().strip()
findkey = findkey.split('.')[-1]
n = len(findkey)
m = len(line)
for i in range(m-n+1):
    if line[i:i+n] == findkey:
        res = line[i+n+2:]
        res = res.split(';')[0]
        res = res.split('{')[0]
        res = res.split('}')[0]
        res = res.split('>')[-1]
        print(res)
        break
