# -*- coding: utf-8 -*-
# @Time    : 2021/9/27 16:14
# @Author  : LiLing

# 将字符串公式去括号,默认公式是有效的。a,b,c,d....代表集合，四则运算只有+ - ()
# 示例
# 示例 1:
# 输入: "(a+(b+c))"
# 输出: a+b+c
# 示例 2:
# 输入: "a+(b+c)-(d+e)"
# 输出: a+b+c-d-e
# 示例 3:
# 输入: "a-((b+c)-(d+e))+f"
# 输出: a-b-c+d+e+f

# https://www.jianshu.com/p/1eb72aed71ee
def remove(expre):
    ss = []
    n = len(expre)
    # 从第一个开始处理，遇到'('号交给process_bracket，括号里的正负号由ss的最后一个字符决定
    ci = 0
    while ci < n:
        if expre[ci] == ')':
            ci += 1
            continue
        if expre[ci] != '(':
            ss.append(expre[ci])
            ci += 1
        else:
            ci = process_bracket(ci+1, ss, expre)  # 括号的下一个字符ci+1，返回处理后的索引
    return "".join(ss)


def process_bracket(index, ss, expre):
    """处理从index开始的字符，ss是index之前已经处理好的字符"""
    cur = expre[index]
    if ss[-1] == "-":  # 处理括号前是-号的情况，由于是可能存在嵌套括号，这里选择的是ss的正负号
        while cur != ")":  # 处理括号里面所有的字符
            if cur == "-":
                ss.append("+")
            elif cur == '+':
                ss.append("-")
            elif cur == '(':   # 存在嵌套，迭代求解
                index = process_bracket(index+1, ss, expre)
            else:
                ss.append(cur)
            index += 1
            cur = expre[index]
    else:  # 处理括号前是+号的情况
        while cur != ")":
            if cur == '(':   # 存在嵌套，迭代求解
                index = process_bracket(index+1, ss, expre)
            else:
                ss.append(cur)
            index += 1
            cur = expre[index]
    return index


def remove_parentheses(s):
    n = len(s)
    s = list(s)
    for i in range(n):
        if (s[i] == '-') and (s[i + 1] == '('):
            s[i + 1] = ' '
            count = 1
            for j in range(i+2, n):
                if s[j] == '(':
                    count += 1
                    s[j] = ' '
                elif count < 1:
                    break
                elif s[j] == ')':
                    count -= 1
                    s[j] = ' '
                elif count == 1 and s[j] == '+':
                    s[j] = '-'
                elif count == 1 and s[j] == '-':
                    s[j] = '+'
        elif s[i] == '(' or s[i] == ')':
            s[i] = ' '
    res = ""
    for i in range(n):
        if s[i] != ' ':
            res += s[i]
    return res

# https://www.cnblogs.com/ilovezyg/p/6431627.html
def remove2(s):
    if not s:
        return s
    stk = [1]  # assume there this a `()` outside the string
    ret = []
    sign = 1
    for i in range(len(s)):
        c = s[i]
        if c == '+':
            sign = 1 
        elif c == '-':
            sign = -1
        elif c == '(':
            stk.append(sign * stk[-1])
            sign = 1  # remember to reset the sign
        elif c == ')':
            stk.pop()
        else:
            if sign*stk[-1] == 1:
                ret.append("+")
            elif sign*stk[-1] == -1:
                ret.append("-")
            ret.append(c)
    return "".join(ret[1:])

if __name__ == "__main__":
    s = "a+b-(c+d+(e+f-(c+d))-(g-e))-d"   # a+b-c-d-e-f+c+d+g-e-d
    #s = "a+b-((b+c)-(a-d))"
    #s = "a-((b+c)-(d+e))+f"  # a-b-c+d+e+f
    print(remove(s))
    print(remove_parentheses(s))
    print(remove2(s))
