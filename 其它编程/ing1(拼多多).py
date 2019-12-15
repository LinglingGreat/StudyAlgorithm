# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 10:55
# @Author  : Liling
"""

"""
import sys
h = sys.stdin.readline().strip().split()
cx, bcx = int(h[0]), int(h[1])
result = cx/bcx
rel = list(str(result).split(".")[1])
if len(rel) == 0:
    print(str(0)+ " "+str(0))
else:
    for i in range(len(rel)):
        newrel = rel[i+1:]
        try:
            nexti = newrel.index(rel[i]) + i + 1
            dis = nexti - i
            ti = "".join(rel[i:nexti])
            j = i
            flag = 1
            while j < len(rel):
                if "".join(rel[j:j+dis]) != ti:
                    flag = 0
                    break
                j = j+dis
            if flag == 1:
                print(str(i)+" "+str(dis))
                break
        except:
            continue
    else:
        print(str(len(rel))+ " "+str(0))


