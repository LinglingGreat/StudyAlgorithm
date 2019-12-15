# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-10-12 09:00:49
# @Last Modified by:   Liling
# @Last Modified time: 2018-10-12 09:39:05
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""
"""
解法1
中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，则左半段是有序的，
我们只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内，这样就可以确定搜索哪边。
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
        	return -1
        start = 0
        end = len(nums) -1
        while start <= end:
        	mid = (end+start)//2
        	if nums[mid] == target:
        		return mid
        	if nums[mid] < nums[end]:
        		if nums[mid] <target <= nums[end]:
        			start = mid+1
        		else:
        			end = mid-1
        	else:
        		if nums[start]<=target <nums[mid]:
        			end = mid-1
        		else:
        			start = mid+1
        return -1
"""
解法2
先找到旋转点，再进行二分查找
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        lo = 0
        hi = n-1
        while lo<hi:
        	mid = (lo+hi)//2
        	if nums[mid]>nums[hi]:
        		lo = mid+1
        	else:
        		hi = mid
        rot = lo
        lo = 0
        hi = n-1
        while lo<=hi:
        	mid = (lo+hi)//2
        	realmid = (mid+rot)%n   # 原始数组的mid
        	if nums[realmid] == target:
        		return realmid
        	if nums[realmid] < target:
        		lo = mid+1
        	else:
        		hi = mid-1
        return -1

s = Solution()
print(s.search([4,5,6,7,0,1,2],0))