"""
三年二班的同学们要去郊游了，他们决定所有人都从一个地方出发，但是每个人都要有不同的路线，最终完成一次郊游。所以他们想知道，在它们去的公园里，究竟有多少种不同的路线供选择。
公园可以被描述为一个具有N个结点，M条有向边的图，你要做的任务就是，选择其中某个点，使得其能够产生尽量多的从这个点出发的路线。

提示：此处可以利用node代表结点的总数，结点编号从0到node-1。edge用来描述边。你的程序应该返回路径最多的结点对应的路径数。
注意：所有的边都是有向边！数据输入将保证不包含环路，不包括重复的边。

输入数据示例：
node = 4

edge = {{0, 1}, {1, 2}, {2, 3}, {0, 2}}，包含4条有向边

输出结果：5

示例解释：
显然，0号节点应该是起点。
对应的5条路线为：
0 1
0 1 2
0 1 2 3
0 2
0 2 3
时间限制: 3S (C/C++以外的语言为: 5 S)   内存限制: 128M (C/C++以外的语言为: 640 M)
输入:
输入描述
输入数据包含M+2行
第一行 整型 node的个数N，范围1-10000
第二行 描述边是M行2列矩阵大小，M  2
第三行-第M+2行表示edge的数据，其中每行代表一条有向边，实际上可以描述成一个N*2的二维数组，行描述边，列表示结点
输出:
输出描述
最大路径的数:一个整型数字
输入范例:
输入范例 例如下面表示总共4个结点和4条边：
4      (总共4个结点，编号0,1,2,3)
4 2
0 1 （从结点0到结点1的一条有向边）
1 2 （从结点1到结点2的一条有向边）
2 3 （从结点2到结点3的一条有向边）
0 2 （从结点0到结点2的一条有向边）
输出范例:
输出范例 例如：
100
"""
import numpy as np


def findpath(dict, key):
    sum = 0
    if key in dict.keys():
        sum += len(dict[key])
        for list in dict[key]:
            sum += findpath(dict, list[1])
    return sum


nodes = eval(input())
rows, cols = list(map(int, input().split()))
edge = np.zeros((rows, cols))
dict = {}
for i in range(nodes):
    dict[i] = []
for i in range(rows):
    value = list(map(int, input().split()))
    edge[i, :] = value
    dict[value[0]].append(value)

maxpath = 0
for i in range(nodes):
    path = 0
    path += findpath(dict, i)
    if path > maxpath:
        maxpath = path
print(maxpath)



