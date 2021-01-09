# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-10-12 09:00:49
# @Last Modified by:   Liling
# @Last Modified time: 2018-10-12 10:07:26
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
"""
"""
解法1
不能通过比较A[mid]和边缘值来确定哪边是有序的，会出现A[mid]与边缘值相等的状态。当中间值与边缘值相等时，
让指向边缘值的指针分别往前移动，忽略掉这个相同点，再用之前的方法判断即可。
而如果解决掉重复之后，利用一个性质，旋转后两部分一定有一部分有序，那么通过判断左边还是右边有序分为两种情况。
然后再判断向左走还是向右走。

这一改变增加了时间复杂度，试想一个数组有同一数字组成{1，1，1，1，1}，target=2, 那么这个算法就会将整个数组遍历，
时间复杂度由O(logn)升到O(n)。
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # 重复了，跳过
            if nums[mid] == nums[left]:
                left += 1
            elif nums[mid] > nums[left]:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


s = Solution()
print(s.search([4,5,6,7,0,1,2],0))