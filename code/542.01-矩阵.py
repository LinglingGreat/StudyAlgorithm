#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
# https://leetcode-cn.com/problems/01-matrix/description/
#
# algorithms
# Medium (45.94%)
# Likes:    495
# Dislikes: 0
# Total Accepted:    65.9K
# Total Submissions: 143.6K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
# 
# 两个相邻元素间的距离为 1 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：[[0,0,0],[0,1,0],[0,0,0]]
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
# 输出：[[0,0,0],[0,1,0],[1,2,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# m == mat.length
# n == mat[i].length
# 1 
# 1 
# mat[i][j] is either 0 or 1.
# mat 中至少有一个 0 
# 
# 
#

# @lc code=start
from typing import Collection


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dists = [[float('inf') for i in range(n)] for j in range(m)]
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    dists[i][j] = 0
        while q:
            node = q.popleft()
            dist = dists[node[0]][node[1]]
            matrix = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for t in matrix:
                r, c = node[0]+t[0], node[1]+t[1]
                if 0<=r<m and 0<=c<n:
                    if dists[r][c] > dist+1:
                        dists[r][c] = dist+1
                        q.append((r,c))
        return dists
# @lc code=end

