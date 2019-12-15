# -*- coding: utf-8 -*-
# @Time    : 2018/9/9 18:57
# @Author  : Liling
"""
对于仅由小写字母组成的字符串A和B，如果分别存在一个小写字母a到z的排列，使得将A中所有字母a替换为排列的第一个字母，所有字母b替换为排列的第二个字母……所有字母z替换为排列的最后一个字母之后，A和B完全相同，那么称字符串A和B相似，如abcc和xyaa。现在给定仅由小写字母组成且长度不超过105的字符串S和T，求S中有多少子串与T相似？

输入
第一行和第二行分别输入字符串S和T。

输出
输出字符串S中与T相似的子串数目。


样例输入
ababcb
xyx
样例输出
3

Hint
样例解释
S中与T相似的子串分别是aba、bab、bcb，总共3个。
"""
def sim(s,t):
    ss = len(set(s))
    tt = len(set(t))
    ns = len(s)
    nt = len(t)
    if ns != nt:
        return False
    if ss != tt:
        return False
    count1 = []
    count2 = []
    for j in set(s):
        count2.append(s.count(j))
    for j in set(t):
        c = t.count(j)
        count1.append(c)
        if c > 1:
            indexl = [x for x in range(nt) if t[x]==j]
            simst = [s[x] for x in indexl]
            if s.count(simst[0]) != c:
                return False
            simst = set(simst)
            if len(simst) != 1:
                return False
    if sorted(count1) != sorted(count2):
        return False
    return True

def  solve(S, T):
    n = len(T)
    m = len(S)
    res = 0
    if m<n:
        return res
    for i in range(m-n+1):
        if sim(S[i:i+n], T):
            res += 1
    return res

S = input()
T = input()
print(solve(S, T))

