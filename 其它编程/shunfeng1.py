# -*- coding: utf-8 -*-
# @Time    : 2018/9/15 10:00
# @Author  : Liling
"""
顺丰 83%
行程安排
题目描述：
我是一个大帅哥，因此有很多粉丝想和我合影，想请我吃饭，也有很多签售会演唱会等着我，总之我很忙。可是，我的秘书非常不靠谱，
他总是把一些日程安排在重复的时间上，比如我今天的日程是: 早上 8:00-10:00 粉丝见面会 早上 9:00-9:30 粉丝早餐会
下午 1:30-5:00 午睡(是的，这很重要) 晚上 8:00-9:30 婚礼表演嘉宾 所以，由于粉丝见面会更重要，我不得不取消粉丝早餐会了，
因为他们在同一时间进行。那么问题来 了，现在我需要一套算法，当我输入一天的行程，我需要这个算法告诉我，今天至少要取消多少个行程
才能让每个日程之间时间不重叠。skrskr~

输入
原始输入为时间点数目（行程数*2）以及各个行程的开始结束时间点。
需要先转化为一个二元组的list，如
list[ (8.0, 10.0), (8.0, 10.0), (8.0, 10.0), (8.0, 10.0), (12.0, 14.5) ]
其中二元组内第一第二个元素分别为事项的开始和结束时间，以float显示，如早上9：00-10：00表示为(9.0,10.0)，
下午1：30-下午5:00表示为(13.5,17.0)。

输出
需要取消多少个行程，以int显示。


样例输入
10
8.0
10.0
8.0
10.0
8.0
10.0
8.0
10.0
12.0
14.5
样例输出
3
"""
# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def schedule(data):
    ans = sorted(data, key=lambda x: x[0])
    n = len(ans)
    if n <= 1:
        return 0
    res = [ans[0]]
    e = ans[0][1]
    for i in range(1, n):
        if ans[i][0] >= e:
            res.append(ans[i])
            e = ans[i][1]
        elif ans[i][1] <= e:
            res.pop()
            res.append(ans[i])
            e = ans[i][1]
    return n-len(res)


# ******************************结束写代码******************************


_data_cnt = 0
_data_cnt = int(input())
_data_i = 0
_data = []
while _data_i < _data_cnt//2:
    _data_item1 = float(input())
    _data_item2 = float(input())
    _data.append([_data_item1,_data_item2])
    _data_i += 1

res = schedule(_data)

print(str(res) + "\n")

