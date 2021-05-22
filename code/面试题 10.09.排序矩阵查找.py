# 给定M×N矩阵，每一行、每一列都按升序排列，请编写代码找出某元素。 
# 
#  示例: 
# 
#  现有矩阵 matrix 如下： 
# 
#  [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#  
# 
#  给定 target = 5，返回 true。 
# 
#  给定 target = 20，返回 false。 
#  Related Topics 双指针 二分查找 分治算法 
#  👍 27 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows = len(matrix)
        if nrows == 0:
            return False
        ncols = len(matrix[0])
        row, col = nrows - 1, 0
        while row >= 0 and col < ncols:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
