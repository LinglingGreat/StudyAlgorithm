# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 10:55
# @Author  : Liling
# @File    : toutiao3.py
# @Software: PyCharm
import sys

if __name__ == "__main__":
    # 读取第一行的t
    t = int(sys.stdin.readline().strip())
    result = []
    for i in range(t):
        # 读取每一行
        n = int(sys.stdin.readline().strip())
        # 把每一行的数字分隔后转化成int列表
        groupstr = []
        for j in range(n):
            line = sys.stdin.readline().strip()
            groupstr.append(line)
        flag = 0
        for s1 in range(len(groupstr)):
            for s2 in range(s1+1, len(groupstr)):
                if len(groupstr[s1]) == len(groupstr[s2]):
                    s = groupstr[s2] * 2
                    if groupstr[s1] in s or groupstr[s1] in s[::-1]:
                        flag = 1
                        result.append("Yeah")
                        break
            if flag == 1:
                break

        if flag == 0:
            result.append("Sad")
    for i in result:
        print(i)