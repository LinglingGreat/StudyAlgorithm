# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 18:30
# @Author  : Liling
"""
小红书笔试题
将重复字符串替换成数字
"""
import sys
ans = sys.stdin.readline().strip()
i = 0
num = 0
res = ''
j = 1
while j < len(ans):
    if ans[j] == ans[i]:
        num += 1
    else:
        res += (str(num) if num>1 else '')+ans[i]
        i = j
        num = 0
    j += 1
res += (str(num) if num > 1 else '')+ans[i]
print(res)

