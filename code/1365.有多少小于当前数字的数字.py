#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101
        for num in nums:
            count[num] += 1
        # 存储小于等于这个数的所有数字
        for i in range(1, 101):
            count[i] += count[i-1]
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = 0 if nums[i]==0 else count[nums[i]-1]
        return res
# @lc code=end

