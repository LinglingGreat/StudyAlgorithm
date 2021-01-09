# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-25 14:34:09
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-25 19:00:16
"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution:
    def backtrack(self, res, n, nums, k, current):
        if len(current) == k:
            res.append(current.copy())
        else:
            for i in range(nums, n + 1):
                current.append(i)
                self.backtrack(res, n, i + 1, k, current)
                current.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(res, n, 1, k, [])
        return res

class Solution1:              
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 先固定前面几个数，最后一个数递增
        i = 0
        p = [0]*k
        res = []
        while i>=0:
        	p[i] += 1
        	if p[i] > n: 
        		i -= 1
        	elif i == k-1:
        		res.append(p.copy())
        	else:
        		i += 1
        		p[i] = p[i-1]
        return res

s=Solution1()
print(s.combine(4,2))