# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
import sys
import math
import numpy as np


line = sys.stdin.readline().strip()
p = list(map(int, line.split()))
line = sys.stdin.readline().strip()
q = list(map(int, line.split()))
allv = set(p+q)
np = len(p)
nq = len(q)
kldis = 0
for v in allv:
    pv = p.count(v)/np
    qv = q.count(v)/nq
    if pv > 0 and qv > 0:
        kldis += pv*math.log(pv/qv,2)
print(round(kldis,2))

