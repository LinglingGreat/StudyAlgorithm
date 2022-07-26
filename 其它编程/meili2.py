# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 18:42
# @Author  : Liling
import sys
ans = sys.stdin.readline().strip()
num = int(sys.stdin.readline().strip())
n = len(ans)
res = []
if num<=0:
	print(-1)
elif n>=num:
    for i in range(len(ans)-num+1):
        res.append(ans[i:i+num])
    print(' '.join(res))

else:
    print(-1)
