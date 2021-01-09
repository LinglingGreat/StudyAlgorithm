#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 题目的意思是寻找下一个比当前数大的数
        # 先从后往前找到第一个nums[i] < nums[i+1]的数, i就是要交换的较小数, (i+1, end)是降序
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # 从(i, end)范围里从后往前找，找到第一个比nums[i]大的数，这是为了找到一个尽量小的较大数
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            # 两个数字交换
            nums[i], nums[j] = nums[j], nums[i]
        # 注意，还没结束，要将i后面的数升序排列，也就是反转一下
        nums[i+1:] = nums[i+1:][::-1]
# @lc code=end

