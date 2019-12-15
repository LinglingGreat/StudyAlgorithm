# -*- coding: utf-8 -*-
# @Author  : Liling
"""
360 2018年秋招笔试
有一个城市需要修建，给你N个民居的坐标X,Y，
问把这么多民居全都包进城市的话，城市所需最小面积是多少（注意，城市为平行于坐标轴的正方形）
输入
第一行为N，表示民居数目（2≤N≤1000）
下面为N行，每行两个数字Xi，Yi，表示该居民的坐标（-1e9≤xi,yi≤1e9）
输出
城市所需最小面积

样例输入
2
0 0
2 2
样例输出
4

Hint
补充样例
输入样例2
2
0 0
0 3
输出样例2
9
"""
import sys
if __name__ == "__main__":
    # 读取第一行的t
    n = int(sys.stdin.readline().strip())
    minx, maxx, miny, maxy = 1e9, -1e9, 1e9, -1e9
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        if values[0] > maxx:
            maxx = values[0]
        if values[0] < minx:
            minx = values[0]
        if values[1] > maxy:
            maxy = values[1]
        if values[1] < miny:
            miny = values[1]

    x = abs(maxx - minx)
    y = abs(maxy - miny)
    bc = max(x,y)
    result = bc*bc
    print(result)

