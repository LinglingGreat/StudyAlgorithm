#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#
# https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (69.65%)
# Likes:    432
# Dislikes: 0
# Total Accepted:    42.9K
# Total Submissions: 61.4K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# 给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
# 
# 找到所有出现两次的元素。
# 
# 你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
# 
# 示例：
# 
# 
# 输入:
# [4,3,2,7,8,2,3,1]
# 
# 输出:
# [2,3]
# 
# 
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            index = abs(nums[i])-1
            if nums[index] > 0:
                nums[index] = -nums[index]
            else:
                res.append(index+1)
        return res
# @lc code=end

