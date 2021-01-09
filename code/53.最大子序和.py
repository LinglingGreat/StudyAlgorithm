#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        premax = 0
        maxres = nums[0]
        for num in nums:
            premax = max(premax+num, num)
            maxres = max(premax, maxres)
        return maxres
# @lc code=end

