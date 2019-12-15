# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
"""
precision和recall
20
1 0.999
1 0.998
1 0.997
1 0.996
1 0.995
1 0.991
1 0.992
1 0.993
1 0.994
1 0.990
0 0.001
0 0.002
0 0.003
0 0.004
0 0.005
0 0.008
0 0.010
0 0.110
0 0.201
0 0.111
"""
import sys

n = int(sys.stdin.readline().strip())
examples = []
ponum = 0
for i in range(n):
    line = sys.stdin.readline().strip()
    exa = list(map(eval, line.split()))
    examples.append(exa)
    if exa[0] == 1:
        ponum += 1

relist = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
examples = sorted(examples, key=lambda x: x[1], reverse=True)
for i in relist:
    po = ponum * i
    j = 0
    e = 0
    while j < po:
        if examples[e][0] == 1:
            j += 1
        e += 1
    poexa = [exa[0] for exa in examples[:e]]
    print(round(sum(poexa)/len(poexa)*100))





