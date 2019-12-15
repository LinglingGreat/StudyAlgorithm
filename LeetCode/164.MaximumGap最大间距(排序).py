# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-10-05 21:41:30
# @Last Modified by:   Liling
# @Last Modified time: 2018-10-06 22:05:14
"""
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
"""
"""
可以用常见的排序方式对数组排序，如冒泡、快排、归并等，但这些方式时间复杂度最小的也要O(nlogn)，不满足要求。

换一种方法，我们使用基数排序的思想，先根据个位数的大小把所有元素分散到10个数组。

然后按个位数从小到大的顺序取出这些元素并根据十位数的大小分散到10个数组。

再按十位数从小到大的顺序取出这些元素并根据百位数的大小分散到10个数组。

依次类推，由于32位有符号整型数最大值为2147483647，因此只需进行10次分散操作即可

然后再按照排好的顺序取相邻两个数差的最大值，复杂度满足线性要求。
下面举一个简单例子走一遍算法帮助理解：[104,14,15,5,4]。

按个位数排列：第4个数组中有[104,14,4]，第5个数组中有[15,5]；

按十位数排列：第0个数组中有[104,4,5]，第1个数组中有[14,15]；

按百位数排列：第0个数组中有[4,5,14,15]，第1个数组中有[104]；

按千位数排列：第0个数组中有[4,5,14,15,104]；

后续操作均不再发生变化，接着比较相邻两个数的差：5-4=1,14-5=9,15-14=1,104-15=89，因此最终结果为89。
"""
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return 0
        num = [0]*length
        idarr = [[[] for j in range(10)] for i in range(10)]   # 用于存每次基数排序后的元素下标
        # print(idarr)
        for i in range(length):
            num[i] = nums[i]  # 将所有元素复制一份，方便每次排序时比较
            idarr[0][num[i]%10].append(i)   # 按个位排序，将下标存到对应数组
            num[i] = num[i] // 10   # 将个位丢弃，为十位比较做准备

        for i in range(1,10):   # 依次从十位开始往高位比较
            for j in range(10):   # 从前一次比较最小的元素开始
                nowlen = len(idarr[i-1][j])
                for k in range(nowlen):
                    nowid = idarr[i-1][j][k]   # 取id
                    idarr[i][num[nowid]%10].append(nowid)   # 将下标存到对应数组
                    num[nowid] = num[nowid] // 10   # 将当前位丢弃，为下一位比较做准备

        last = -1
        ans = 0
        for i in range(10):
            nowlen = len(idarr[9][i])
            for j in range(nowlen):
                nowid = idarr[9][i][j]
                if last == -1:
                    last = nums[nowid]  # 当前是最小的数
                else:
                    ans = max(ans, nums[nowid]-last)   # 更新最大的差
                last = nums[nowid]

        return ans
"""
Radix Sort基数排序
Time complexity: O(d·(n + k))≈O(n).
Space complexity: O(n + k)≈O(n) extra space.
"""
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return 0
        maxVal = max(nums)
        exp = 1   # 1, 10, 100, 1000 ...
        radix = 10   # base 10 system
        aux = [0]*length

        # LSD Radix Sort
        while maxVal // exp > 0:   # Go through all digits from LSD to MSD
            count = [0]*radix
            for i in range(len(nums)):   # Counting sort
                count[(nums[i] // exp)%10] += 1
            for i in range(1, len(count)):    # you could also use partial_sum()
                count[i] += count[i-1]
            for i in range(len(nums)-1, -1, -1):
                j = (nums[i]//exp)%10
                count[j] -= 1
                aux[count[j]] = nums[i]
            for i in range(len(nums)):
                nums[i] = aux[i]
            exp *= 10

        maxGap = 0
        for i in range(len(nums)-1):
            maxGap = max(nums[i+1]-nums[i], maxGap)
        return maxGap
        
"""
https://leetcode.com/problems/maximum-gap/solution/
Buckets and The Pigeonhole Principle
The Pigeonhole Principle states that if n items are put into m containers, with n>m, 
then at least one container must contain more than one item.

We choose a bucket size b such that 1<b≤(max−min)/(n−1). Let's just choose b=⌊(max−min)/(n−1)⌋.

Thus all the nn elements would be divided among k=⌈(max−min)/b⌉ buckets.

Hence the ith bucket would hold the range of values: [min+(i−1)∗b, min+i∗b) (1-based indexing).

It is trivial to calculate the index of the bucket to which a particular element belongs. That is given by 
⌊(num−min)/b⌋ (0-based indexing) where num is the element in question.

Once all n elements have been distributed, we compare k-1 adjacent bucket pairs to find the maximum gap.

Time complexity: O(n+b)≈O(n).
Space complexity: O(2⋅b)≈O(b) extra space.
"""
import sys
class Bucket:
    def __init__(self):
        self.used = False
        self.minval = sys.maxsize
        self.maxval = -self.minval
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return 0
        mini = min(nums)
        maxi = max(nums)

        bucketSize = max(1, (maxi - mini) // (int(length)-1))
        bucketNum = (maxi - mini) // bucketSize + 1
        buckets = [Bucket() for i in range(bucketNum)]

        for num in nums:
            bucketIdx = (num - mini) // bucketSize
            buckets[bucketIdx].used = True
            buckets[bucketIdx].minval = min(num, buckets[bucketIdx].minval)
            buckets[bucketIdx].maxval = max(num, buckets[bucketIdx].maxval)

        preBucketMax = mini
        maxGap = 0
        for bucket in buckets:
            if not bucket.used:
                continue
            maxGap = max(maxGap, bucket.minval - preBucketMax)
            preBucketMax = bucket.maxval
        return maxGap


s = Solution()
print(s.maximumGap([3,6,9,1]))