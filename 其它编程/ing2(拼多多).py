# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 10:55
# @Author  : Liling
"""

"""
import sys
h = sys.stdin.readline().strip().split()
n, l = int(h[0]), int(h[1])
wordlist = []
for i in range(n):
    line = sys.stdin.readline().strip()
    line = list(line)
    wordlist.append(line)

wordlist = list(map(list, zip(*wordlist)))
w = ""
for line in wordlist:
    w += min(line)
wordlist = list(map(list, zip(*wordlist)))
flag = 1
for line in wordlist:
    if w == "".join(line):
        flag = 0
        break
if flag:
    print(w)
else:
    print("-")

