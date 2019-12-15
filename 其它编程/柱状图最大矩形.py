# -*- coding: utf-8 -*-
"""
给定一组非负整数组成的数组h，代表一组柱状图的高度，其中每个柱子的宽度都为1。 在这组柱状图中找到能组成的最大矩形的面积。
入参h为一个整型数组，代表每个柱子的高度，返回面积的值。
输入描述:
输入包括两行,第一行包含一个整数n(1 ≤ n ≤ 10000)
第二行包括n个整数,表示h数组中的每个值,h_i(1 ≤ h_i ≤ 1,000,000)
输出描述:
输出一个整数,表示最大的矩阵面积。
输入例子1:
6
2 1 5 6 2 3
输出例子1:
10
"""
import sys

n = int(sys.stdin.readline().strip())
harray = sys.stdin.readline().strip()
harray = list(map(int,harray.split()))
maxlen = 0
for i in range(n):  # 循环，以柱子i为中心，向两边可扩展的柱子扩展
    j = i-1
    ilen = 1
    while j>=0 and harray[j] >= harray[i]:
        ilen += 1
        j -= 1
    j = i+1
    while j<n and harray[j] >= harray[i]:
        ilen += 1
        j += 1
    ilen *= harray[i]
    if ilen > maxlen:
        maxlen = ilen
print(maxlen)

'''
分治法：最大矩形面积只可能有三种情况：
1. 取决于高度最小的柱子，此时面积等于高度乘总长度；
2. 最大面积出现在高度最小的柱子左边；
3. 最大面积出现在高度最小的柱子右边；
'''
n = int(input())
h = [int(x) for x in input().split()]


def largestarea(a):
    l = len(a)
    idx = a.index(min(a))

    value1 = a[idx] * l

    if idx != 0:
        value2 = largestarea(a[0:idx])
    else:
        value2 = 0
    if idx != l - 1:
        value3 = largestarea(a[idx + 1:l])
    else:
        value3 = 0
    return max(value1, value2, value3)


print(largestarea(h))


"""
https://www.hackerrank.com/challenges/largest-rectangle/forum/comments/418819?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues
如果当前矩形比上一个高时，将其压入栈中；如果比上一个低，将元素出栈直到找到一个比当前矩形低的矩形或者栈为空，
这样就找到了当前矩形区域的左index，将当前矩形的高度及其左index压入栈中。
当开始出栈的时候，说明已经找到一个矩形区域的右index，由此可以计算矩形区域的面积并与当前最大值比较
"""
def largestRectangleArea(self, heights):
    s = []
    ans = 0
    heights.append(0)

    for i in range(len(heights)):
        left_index = i    # 当前矩形区域的左index
        while len(s) > 0 and s[-1][0] >= heights[i]:   # 如果矩形i的高度比前一个矩形低的话，说明
            last = s.pop()   # 出栈
            left_index = last[1]    # 出栈元素的左index
            ans = max(ans, heights[i] * (i + 1 - last[1]))
            ans = max(ans, last[0] * (i - last[1]))
        s.append((heights[i], left_index))    # 如果矩形i的高度比前一个矩形高，记录矩形i的高度及其所在区域的左index

    return ans

"""
https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28905/My-concise-C++-solution-AC-90-ms?page=3
"""
def largestRectangleArea1(self, height):
    height.append(0)
    stack = [0]
    r = 0
    for i in range(1, len(height)):
        while stack and height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i if not stack else i - stack[-1] -1
            r = max(r, w*h)
        stack.append(i)
    return r

