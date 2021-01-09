#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    temp = 4
                    # 当旁边数字为1的时候不算周长，两个网格是相互的，可以只看网格的上方和左方一次减去2
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        temp -= 2
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        temp -= 2
                    res += temp
        return res
# @lc code=end

