#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i,0) + 1
        sort_dict = sorted(nums_dict.items(),key=lambda x:x[1],reverse=True)
        return [i[0] for i in sort_dict][:k]

# @lc code=end

