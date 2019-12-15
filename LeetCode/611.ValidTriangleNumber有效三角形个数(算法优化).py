# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-17 17:51:16
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-17 22:20:15
"""
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。
"""
"""
解法一
时间复杂度O(n^3)
空间复杂度O(1)
"""
class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = sorted(nums)
        res = 0
        for i in range(n-2):
        	for j in range(i+1,n-1):
        		for k in range(j+1,n):
        			if nums[i]+nums[j]>nums[k]:
        				res += 1
        return res

"""
解法二
Binary Search
先将数组排序，这样只需比较前两个数字之和是否大于第三个
第一个数字是i，第二个数字是j(范围是i+1到n-2)，第三个数字是k，在j+1后面找到大于前两个数字之和的最小数字，即右端点k
右端点右边的点都比nums[i]+nums[j]大，所以有效的三角形个数就是(j+1,k-1)之间的数字个数，k-1-(j+1)+1
时间复杂度O(n^2*logn)
空间复杂度O(logn)
"""
class Solution:
	def binarySearch(nums, l, r, x):
		while r >= 1 and r < len(nums):
			mid = (1+r)/2
			if nums[mid] >= x:
				r = mid - 1
			else:
				l = mid + 1
		return 1

    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        nums = sorted(nums)
        n = len(nums)
        for i in range(n-2):
        	k = i+2
        	if nums[i] != 0:
        		for j in range(i+1, n-1):
        			# 注意这里是从k开始找，因为每一次的j总比上一次的大或相等
        			k = binarySearch(nums, k, n-1, nums[i]+nums[j])
        			count += k-j-1

        return count

"""
解法三
Linear Scan
改进解法二
时间复杂度O(n^2)
空间复杂度O(logn)
"""
class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        nums = sorted(nums)
        n = len(nums)
        for i in range(n-2):
        	k = i+2
        	if nums[i] != 0:
        		for j in range(i+1, n-1):
        			while k<n and nums[i]+nums[j]>nums[k]:
        				k += 1
        			count += k-j-1

        return count