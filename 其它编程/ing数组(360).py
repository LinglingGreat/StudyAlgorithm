# -*- coding: utf-8 -*-
# @Author  : Liling
"""
360 2018年秋招笔试
时间限制：C/C++语言 3000MS；其他语言 5000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
小红有两个长度为n的排列A和B。每个排列由[1,n]数组成，且里面的数字都是不同的。
现在要找到一个新的序列C，要求这个新序列中任意两个位置(i,j)满足:
如果在A数组中C[i]这个数在C[j]的后面，那么在B数组中需要C[i]这个数在C[j]的前面。
请问C序列的长度最长为多少呢？
输入
第一行一个整数，表示N。
第二行N个整数，表示A序列。
第三行N个整数，表示B序列。
满足:N<=50000
输出
输出最大的长度
样例输入
5
1 2 4 3 5
5 2 3 4 1
样例输出
2
"""
import sys

def findmaxlen(nowlist, a, b):
    flag = 0
    for i in a:
        for j in nowlist:
            if (a.index(i)-a.index(j))*(b.index(i)-b.index(j))>0:
                flag = 1
                break
        if flag == 0:
            nowlist.append(i)
    return len(nowlist)

if __name__ == "__main__":
    # 读取第一行的t
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    a = list(map(int, line.split()))
    line = sys.stdin.readline().strip()
    b = list(map(int, line.split()))
    lena = len(a)
    bigram = [[]*n]
    for i in range(lena):
        for j in range(lena):
            if b.index(a[i]) > b.index(a[j]):
                bigram.append([a[i], a[j]])
    maxlen = 1
    for t in bigram:
        if len(t)!= 0:
            ml = findmaxlen(t, a, b)
            if ml> maxlen:
                maxlen = ml


    nowlist = [a[0]]
    flag = 0
    for i in a[1:]:
        for j in nowlist:
            if (a.index(i)-a.index(j))*(b.index(i)-b.index(j)) > 0:
                flag = 1
                break
        if flag == 0:
            nowlist.append(i)
    print(len(nowlist), nowlist)


