# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 10:55
# @Author  : Liling
"""

"""
import sys

def attack(hp, last, na, ba):
    if hp <= 0:
        return 0
    if last == -1:
        if hp <= ba:
            return 1
        else:
            return 1+attack(hp-ba, 1, na, ba)
    else:
        if hp <= na:
            return 1
        else:
            return min(1+attack(hp-na, 1, na, ba), 1+attack(hp, -1, na, ba))


h = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
print(attack(h, 1, n, b))





