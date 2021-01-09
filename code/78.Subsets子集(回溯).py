# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-26 12:57:48
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-26 13:02:11
"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
"""
全排列，部分排列这些问题都是回溯的题目。这个题目每个状态都是解，包括空list也是解，
所以直接都加进去就好。
"""
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list = []
        nums.sort()
        self.bracktrack(list, [], nums, 0)
        return list

    def bracktrack(self, list, tempList, nums, start):
    	list.append(tempList.copy())
    	for i in range(start, len(nums)):
    		tempList.append(nums[i])
    		self.bracktrack(list, tempList, nums, i+1)
    		tempList.pop()

