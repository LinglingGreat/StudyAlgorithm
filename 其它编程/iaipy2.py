"""
爱奇艺AC
题目描述：
散散掌控着一片森林，这片森林有N棵树，高度分别为ai，现在散散想要长度为m的木头，散散的锯子有一个缺陷，必须同时切割所有的树木，即如果有高度为10，15，12的树木，散散只能确定锯子的高度，如果锯子的高度为13，那么只能将高度为15的树木切下长度为2的木头，锯子高度为8，则分别切下2，7，4的木头，共13长度。

请问锯子的高度最高可以多高呢？

n <= 10^5

m<= 10^9

ai <= 10^9

输入
第一行n和m

第二行n个整数ai

输出
一个高度


样例输入
5 20
4 42 40 26 46
样例输出
36
"""
import math
line = input().split()
n, m = int(line[0]), int(line[1])
height = list(map(int, input().split()))
height = sorted(height, reverse=True)
ind = 0
reslist = [0]*n
res = 0
for i in range(1, n):
    reslist[i] = reslist[i-1]+(height[i-1]-height[i])*i
    if reslist[i] >= m:
        ind = i-1
        break
else:
    ind = n-1
res = reslist[ind]
pr = height[ind] - math.ceil((m - res)/(ind+1))
print(pr)
