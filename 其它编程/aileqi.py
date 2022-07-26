# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-30 14:58:33
# @Last Modified by:   LL
# @Last Modified time: 2018-09-30 15:03:59
A=[2,7,11,15]
B=[1,10,4,11]
def enhance(A,B):
    a=['F']*len(A)
    A=sorted(A)
    for i in range(len(B)):
        for j in range(len(A)):
            if A[j]>B[i]:
                a[i]=A[j]
                A.pop(j)
                break
    if len(A):
        for i in A:
            for j in range(len(a)):
                if a[j]=='F':
                    a[j]=i
                    break
    return a
A=[12, 24, 8, 32]
B=[13, 25, 32, 11]
print(enhance(A,B))