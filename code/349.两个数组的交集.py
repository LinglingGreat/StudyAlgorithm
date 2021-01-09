#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return set(nums1)&set(nums2)
        dic = {}
        res = set()
        for i in nums1:
            dic[i] = 1
        for i in nums2:
            if i in dic:
                res.add(i)
        return list(res)

        
# @lc code=end

