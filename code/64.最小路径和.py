#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)   # 行
        n = len(grid[0])   # 列
        minsum = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    minsum[i][j] = grid[i][j]
                elif i == 0:
                    minsum[i][j] = minsum[i][j-1] + grid[i][j]
                elif j == 0:
                    minsum[i][j] = minsum[i-1][j] + grid[i][j]
                else:
                    minsum[i][j] = min(minsum[i-1][j], minsum[i][j-1])+grid[i][j]
        return minsum[m-1][n-1]
# @lc code=end

