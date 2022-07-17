# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 10:28
# @Author  : Liling
import sys
def ishuiwen(ans):
    if ans == ans[::-1]:
        return True
    return False


t = int(sys.stdin.readline().strip())
for i in range(t):
    line = sys.stdin.readline().strip()
    n = len(line)
    if ishuiwen(line):
        print(-1)
        continue
    for j in range(n):
        if ishuiwen(line[:j]+line[j+1:]):
            print(j)
            break
