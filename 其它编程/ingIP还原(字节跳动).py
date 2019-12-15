# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
"""
IP还原
"""
import sys


def ishf(ip):
    ip = ''.join(ip)
    if (not ip.startswith('0') or len(ip) == 1) and 0 <= int(ip) <= 255:
        return True
    return False


def huanyuan(iplist, k):
    n = len(iplist)
    if n<=k:
        return 1
    else:
        m = n-k
        sum = 0
        for i in range(1, m+2):
            if ishf(iplist[:m]):
                sum += huanyuan(iplist[m+1:],k-1)
        return sum


line = sys.stdin.readline().strip()
iplist = list(map(int, line.split()))
print(huanyuan(iplist,4))



