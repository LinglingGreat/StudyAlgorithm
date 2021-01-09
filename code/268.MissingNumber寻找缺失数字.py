# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-06 23:02:52
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-10 15:31:05

"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
示例 1:
输入: [3,0,1]
输出: 2
示例 2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
"""
Gauss' Formula
Time complexity : O(n)
Space complexity : O(1)
"""
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = sum(nums)
        ts = (1+n)*n//2
        return ts-s
"""
Approach #1 Sorting [Accepted]
Intuition

If nums were in order, it would be easy to see which number is missing.

Algorithm

First, we sort nums. Then, we check the two special cases that can be handled in constant time - ensuring 
that 0 is at the beginning and that nn is at the end. Given that those assumptions hold, the missing number 
must somewhere between (but not including) 0 and nn. To find it, we ensure that the number we expect to be 
at each index is indeed there. Because we handled the edge cases, this is simply the previous number plus 1. 
Thus, as soon as we find an unexpected number, we can simply return the expected number.
Time complexity : O(nlgn)
Space complexity : O(1) (or O(n))
"""
class Solution:
    def missingNumber(self, nums):
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num

"""
Approach #2 HashSet [Accepted]
Intuition

A brute force method for solving this problem would be to simply check for the presence of each number that 
we expect to be present. The naive implementation might use a linear scan of the array to check for containment, 
but we can use a HashSet to get constant time containment queries and overall linear runtime.

Algorithm

This algorithm is almost identical to the brute force approach, except we first insert each element of nums 
into a set, allowing us to later query for containment in O(1) time.
Time complexity : O(n)
Space complexity : O(n)
"""
class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
"""
Approach #3 Bit Manipulation [Accepted]
Intuition

We can harness the fact that XOR is its own inverse to find the missing element in linear time.

Algorithm

Because we know that nums contains nn numbers and that it is missing exactly one number on the range 
[0..n-1][0..n−1], we know that nn definitely replaces the missing number in nums. Therefore, if we 
initialize an integer to nn and XOR it with every index and value, we will be left with the missing number.
Time complexity : O(n)
Space complexity : O(1)
"""
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
