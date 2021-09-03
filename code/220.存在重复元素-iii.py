#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
# https://leetcode-cn.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (28.71%)
# Likes:    493
# Dislikes: 0
# Total Accepted:    63.1K
# Total Submissions: 219.8K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j])
# ，同时又满足 abs(i - j)  。
# 
# 如果存在则返回 true，不存在返回 false。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true
# 
# 示例 2：
# 
# 
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true
# 
# 示例 3：
# 
# 
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# 0 
# -2^31 
# 0 
# 0 
# 
# 
#

# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        '''
        # O(N logk)
        window = SortedList()
        for i in range(len(nums)):
            # len(window) == k
            if i > k:
                window.remove(nums[i - 1 - k])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])
            if idx > 0 and abs(window[idx] - window[idx-1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx+1] - window[idx]) <= t:
                return True
        return False
        '''
        def getIdx(u):
            return ((u + 1) // size) - 1 if u < 0 else u // size
        
        map = {}
        size = t + 1
        for i,u in enumerate(nums):
            idx = getIdx(u)
            # 目标桶已存在（桶不为空），说明前面已有 [u - t, u + t] 范围的数字
            if idx in map:
                return True
            # 检查相邻的桶
            l, r = idx - 1, idx + 1
            if l in map and abs(u - map[l]) <= t:
                return True
            if r in map and abs(u - map[r]) <= t:
                return True
            # 建立目标桶
            map[idx] = u
            # 维护个数为k
            if i >= k:
                map.pop(getIdx(nums[i-k]))

        return False
# @lc code=end

