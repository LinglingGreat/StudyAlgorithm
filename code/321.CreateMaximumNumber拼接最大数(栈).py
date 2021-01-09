# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-10 12:48:58
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-10 13:09:01
"""
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
示例 2:

输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
示例 3:

输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]
"""
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
 
        def get_max_sub_array(nums, k):
            res , n = [] ,len(nums)
            for i in range(n):
                while res and len(res) + n - i > k and nums[i] > res[-1]:
                    res.pop()
                if len(res) < k:
                    res.append(nums[i])
            return res
 
        ans = [0] * k
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            res1 = get_max_sub_array(nums1, i)
            res2 = get_max_sub_array(nums2, k - i)
            ans = max(ans, [max(res1, res2).pop(0) for _ in range(k)])
        return ans