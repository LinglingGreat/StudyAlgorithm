#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """哈希表判重"""
        # return len(set(nums)) != len(nums)
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
# @lc code=end

