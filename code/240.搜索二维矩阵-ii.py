#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (43.33%)
# Likes:    526
# Dislikes: 0
# Total Accepted:    100.4K
# Total Submissions: 229.8K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
  '5'
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 
# 
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -10^9 
# 每行的所有元素从左到右升序排列
# 每列的所有元素从上到下升序排列
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      rows, cols = len(matrix), len(matrix[0])
      if rows == 0 or cols == 0:
        return False

      # 从左下角开始搜索，从右上角也可
      r = rows - 1
      c = 0

      while c < cols and r >= 0:
        # 大于target值，行-1
        if matrix[r][c] > target:
          r -= 1
        # 小于target值，列+1
        elif matrix[r][c] < target:
          c += 1
        else:
          return True
      return False
      
        
# @lc code=end

