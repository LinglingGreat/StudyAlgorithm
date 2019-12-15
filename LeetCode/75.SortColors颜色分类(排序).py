# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-23 10:52:53
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-23 12:03:49
"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
        	j = i
        	while j-1>=0 and nums[j]<nums[j-1]:
        		nums[j], nums[j-1] = nums[j-1], nums[j]
        		j -= 1
        
"""
涉及到数组和链表的题目，先想想双指针法可不可以用。
这个题目用三个指针：
index 表示当前遍历的元素
p1 记录最后一个0的位置
p2 记录最开始一个2的位置

然后从左到右便利，调整index、p1、p2元素
"""
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = len(nums) - 1
        index = 0
        while index <= p2:
            if nums[index] == 0:
                nums[index] = nums[p1]
                nums[p1] = 0
                p1 += 1
            if nums[index] == 2:
                nums[index] = nums[p2]
                nums[p2] = 2
                p2 -= 1
                index -= 1
            index += 1

"""
Just like the Lomuto partition algorithm usually used in quick sort. We keep a loop invariant that 
[0,i) [i, j) [j, k) are 0s, 1s and 2s sorted in place for [0,k). Here ")" means exclusive. 
We don't need to swap because we know the values we want.
"""
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
        	v = nums[k]
        	nums[k] = 2
        	if v < 2:
        		nums[j] = 1
        		j += 1
        	if v == 0:
        		nums[i] = 0
        		i += 1


s=Solution()
nums = [2,0,2,1,1,0]
s.sortColors(nums)
print(nums)

