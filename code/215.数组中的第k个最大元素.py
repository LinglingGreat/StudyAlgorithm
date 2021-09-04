#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.71%)
# Likes:    1257
# Dislikes: 0
# Total Accepted:    420.7K
# Total Submissions: 650.2K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 
# 
# 提示： 
# 
# 
# 1 
# -10^4 
# 
# 
#

# @lc code=start
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def swap(a, i, j):
            a[i], a[j] = a[j], a[i]
        def partition(a, l, r):
            # x是分割点，i是小于等于分割点的数字个数
            x = a[r]
            i = l - 1
            for j in range(l, r):
                if a[j] <= x:
                    i += 1
                    swap(a, i, j)
            swap(a, i+1, r)
            return i + 1
        def randomPartition(a, l, r):
            i = random.randint(0, r-l)+l
            swap(a, i, r)
            return partition(a, l, r)
        def quickSelect(a, l, r, index):
            q = randomPartition(a, l, r)
            if q == index:
                return a[q]
            elif q < index:
                return quickSelect(a, q+1, r, index)
            else:
                return quickSelect(a, l, q-1, index)
        return quickSelect(nums, 0, len(nums)-1, len(nums)-k)
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def maxHeapify(a, i, heapSize):
            l = i * 2 +1
            r = i*2+2
            largest = i
            if l < heapSize and a[l] > a[largest]:
                largest = l
            if r < heapSize and a[r] > a[largest]:
                largest = r
            if largest != i:
                a[i], a[largest] = a[largest], a[i]
                maxHeapify(a, largest, heapSize)
        def buildMaxHeap(a, heapSize):
            for i in range(heapSize//2, -1, -1):
                maxHeapify(a, i, heapSize)
        heapSize = len(nums)
        buildMaxHeap(nums, heapSize)
        for i in range(len(nums)-1, len(nums)-k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapSize -= 1
            maxHeapify(nums, 0, heapSize)
        return nums[0]
# @lc code=end

