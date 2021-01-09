#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        利用三个指针，分别指向两个数组的末尾，以及当前插入数字的位置。
        从后往前比较两个数组的元素，每次将较大的放到nums1的末尾。
        时间复杂度为O(m+n)，空间复杂度为O(1)
        """
        i, j = m-1, n-1
        end = m + n -1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[end] = nums2[j]
                end -= 1
                j -= 1
            else:
                nums1[end] = nums1[i]
                end -= 1
                i -= 1
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]
# @lc code=end

