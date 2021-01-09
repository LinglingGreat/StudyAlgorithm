# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-10 15:46:54
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-10 16:25:59
"""
一个机器人位于一个 m x n 网格的左上角。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。
问总共有多少条不同的路径？
说明：m 和 n 的值均不超过 100。

示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:
输入: m = 7, n = 3
输出: 28
"""
"""
排列组合
From the top-left to the bottom-right, we will have to move down n-1 times and move right m-1 times (total of m+n-2 moves).
"""
class Solution:
    def uniquePaths(self, m, n):
        return(int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1))))
"""
动态规划问题
Since the robot can only move right and down, when it arrives at a point, there are only two possibilities:

It arrives at that point from above (moving down to that point);
It arrives at that point from left (moving right to that point).
Thus, we have the following state equations: suppose the number of paths to arrive at a point (i, j) is denoted as 
P[i][j], it is easily concluded that P[i][j] = P[i - 1][j] + P[i][j - 1].
"""
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
        	for j in range(1, n):
        		aux[i][j] = aux[i][j-1] + aux[i-1][j]
        return aux[-1][-1]
"""
优化空间复杂度
"""
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m>n: return self.uniquePaths(n,m)
        aux = [1 for x in range(m)]
        for j in range(1, n):
        	for i in range(1, m):
        		aux[i] += aux[i-1]
        return aux[-1]
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        aux = [0 for x in range(n)]
        aux[0] = 1
        for i in range(m):
        	for j in range(n):
        		if obstacleGrid[i][j] == 1:
        			aux[j] = 0
        		elif j>0:
        			aux[j] += aux[j-1]
        return aux[-1]
