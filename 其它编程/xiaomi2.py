# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 18:58
# @Author  : Liling
"""
小米食堂每年都会举办一次厨艺大赛，假设参赛的厨师一共有n位（n < 1000），比赛结束后没有公布评分，但是站在领奖台上的一排厨师中每位厨师都能看到与自己相邻的厨师（左或者右）里评分比自己低（看不到比自己分数高的人的分数）的评分。比赛结束之后要发奖金，以1K为单位，每位厨师至少会发1K的奖金，另外，如果一个厨师发现自己的奖金没有高于比自己评分低的厨师的奖金，就会不满意，作为比赛组织方，小米食堂至少需要发放多少奖金才能让所有厨师满意。

输入
每组数据为n+1个正整数单空格分割，其中第一个数为参赛厨师的人数，后面n个数为每位厨师的得分（0-100）

输出
输出至少需要多少K的奖金


样例输入
10 60 76 66 76 85 55 61 71 84 62
样例输出
20
"""
line = list(map(int, input().split()))
n, scorelist = line[0], line[1:]
res = [1]*n
for i in range(n):
    for j in range(i, -1, -1):
        if j+1 < n and scorelist[j+1] < scorelist[j]:
            res[j] = max(res[j], res[j+1]+1)
        if j-1 >= 0 and scorelist[j-1] < scorelist[j]:
            res[j] = max(res[j], res[j-1]+1)
        # print(j, res[j])
print(sum(res))

