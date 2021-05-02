#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
# https://leetcode-cn.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (73.26%)
# Likes:    223
# Dislikes: 0
# Total Accepted:    102.5K
# Total Submissions: 140.2K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100]
# 
# 示例 2：
# 
# 
# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 10^4
# -10^4 
# nums 已按 非递减顺序 排序
# 
# 
# 
# 
# 进阶：
# 
# 
# 请你设计时间复杂度为 O(n) 的算法解决本问题
# 
# 
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cut = -1
        for i in range(n):
            if nums[i] >= 0:
                cut = i
                break
        nums = [i*i for i in nums]
        if cut == 0:
            return nums
        if cut == -1:
            return nums[::-1]
        ans = []
        # 排序
        i, j = cut-1, cut
        while i>=0 or j<n:
            if i < 0:
                ans.append(nums[j])
                j += 1
            elif j == n:
                ans.append(nums[i])
                i -= 1
            elif nums[i] < nums[j]:
                ans.append(nums[i])
                i -= 1
            else:
                ans.append(nums[j])
                j += 1 
        return ans
# @lc code=end

