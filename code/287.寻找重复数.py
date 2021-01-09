#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """二分查找"""
        n = len(nums)
        l, r, ans = 1, n-1, -1
        while l <= r:
            mid = (l+r) >> 1
            cnt = 0
            for i in range(n):
                if nums[i] <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid
        return ans
# @lc code=end

