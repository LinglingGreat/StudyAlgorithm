#coding=utf-8
'''
一个合法的表达式由()包围，()可以嵌套和连接，如(())()也是合法表达式；现在有6对()，它们可以组成的合法表达式的个数为多少？
'''
'''
在不知道Catalan Number的情况下）将其转化成一个数学问题，用一个值（不妨设为s，初值为0）来表示6对括号构成表达式的正确性，
每出现一个左括号+1，右括号-1，如此表达式从左往右，s的值不停地变化。只要构造过程中s不为负，且当出现12个单括号后s为0即可。

作者：Miner
链接：https://www.zhihu.com/question/25072237/answer/40944822
'''
s=[[] for i in range(13)]       #用来记录每前进s的值

i=0

s[i]=[1]                        #第一个括号一定是左括号

while i<=11:                    #计算12个括号引起的值变化
    #print i,s[i]
    for j in s[i]:
        if j-1>=0:              #若出现的右括号多于左括号，则值小于0
            s[i+1].append(j-1)
        s[i+1].append(j+1)
    i=i+1

print(len([i for i in s[11] if i == 0]))   #输出s[11]中0的个数，即为6对括号正确格式的总个数