#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
# https://leetcode-cn.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (66.27%)
# Likes:    551
# Dislikes: 0
# Total Accepted:    122.1K
# Total Submissions: 184.1K
# Testcase Example:  '[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]'
#
# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。
# 
# 一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被
# 0（代表水）包围着。
# 
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
# 
# 
# 
# 示例 1:
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# 
# 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
# 
# 示例 2:
# 
# [[0,0,0,0,0,0,0,0]]
# 
# 对于上面这个给定的矩阵, 返回 0。
# 
# 
# 
# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。
# 
#

# @lc code=start
class Solution:
    def dfs(self, grid, cur_i, cur_j) -> int:
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
            return 0
        grid[cur_i][cur_j] = 0
        ans = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = cur_i + di, cur_j + dj
            ans += self.dfs(grid, next_i, next_j)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i, j), ans)
        return ans
# @lc code=end

