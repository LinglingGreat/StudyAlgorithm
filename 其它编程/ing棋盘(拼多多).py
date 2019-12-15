# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 10:55
# @Author  : Liling
"""

"""
import sys
h = sys.stdin.readline().strip().split()
n, m = int(h[0]), int(h[1])
qipan = []
for i in range(n):
    line = sys.stdin.readline().strip()
    line = list(line)
    qipan.append(line)

qipan = list(map(list, zip(*qipan)))
for i in range(m):
    if "x" not in qipan[i]:
        qipan[i] = ["." for j in qipan[i]]
    else:
        xindex = -1
        for j in range(n-1, -1, -1):
            if qipan[i][j] == "x":
                xindex = j
            elif qipan[i][j] == "o":
                if xindex == -1:
                    qipan[i][j] = "."
                else:
                    qipan[i][j] = "."
                    qipan[i][xindex-1] = "o"
                    xindex = xindex-1

qipan = list(map(list, zip(*qipan)))
for line in qipan:
    print("".join(line))



