# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-14 13:56:56
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-14 14:39:48
"""
给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。
如果有多个目标子集，返回其中任何一个均可。

示例 1:
输入: [1,2,3]
输出: [1,2] (当然, [1,3] 也正确)

示例 2:
输入: [1,2,4,8]
输出: [1,2,4,8]
"""
class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        S = {-1:set()}    # 记录每个元素能够被整除的那些元素，包括自己
        for x in sorted(nums):
        	S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
        print(S)
        return list(max(S.values(), key=len))

S=Solution()
print(S.largestDivisibleSubset([1,2,4,8]))
"""
DP解法
"""
class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        count = [0]*n
        pre = [0]*n
        nums = sorted(nums)
        maxn = 0
        index = -1
        for i in range(n):
        	count[i] = 1
        	pre[i] = -1
        	for j in range(i-1, -1, -1):
        		if nums[i] % nums[j] == 0:
        			if 1+count[j]>count[i]:
        				count[i] = count[j]+1
        				pre[i] = j
        	if count[i]>maxn:
        		maxn = count[i]
        		index = i

        res = []
        while index != -1:
        	res.append(nums[index])
        	index = pre[index]
        return res
