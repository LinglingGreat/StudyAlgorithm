"""
问题描述：给出n个数，求出其最长不下降子序列的长度，比如n=5，5个数是{4,6,5,7,3}；其最长下降子序列就是{4,6,7}，长度为3。
"""
def solution1(num):
	"""O(n^2)"""
	length = [1]*len(num)
	for i in range(1, len(num)):
		for j in range(len(length[:i])):
			if num[j]<num[i] and length[j]+1>length[i]:
				length[i] = length[j]+1
	print(length)

	return max(length)

class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    O(n^2)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if nums == None or len(nums)==0:
            return 0
        l = len(nums)
        sublongest = [0 for i in range(l)]
        sublongest[0] = 1  
        longest = -1
        for i in range(1,l):
            sublong = 0
            for j in range(0,i):
                if nums[j] <= nums[i]:
                    sublong = max(sublongest[j],sublong)
            sublongest[i] = sublong + 1
            longest = max(sublongest[i],longest)
        return longest


class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    O(nlogn)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if nums == None or len(nums) ==0:
            return 0
        lst = list()
        for i in range(len(nums)):
            if len(lst) == 0 or lst[len(lst) - 1] <= nums[i]:
                lst.append(nums[i])
            else:
                index = self.findFirstLargeEqual(lst,nums[i])
                lst[index] = nums[i]
        return len(lst)
        
    def findFirstLargeEqual(self,lst,target):
        left = 0
        right = len(lst) -1 
        while left < right:
            mid = (left + right)/2
            if lst[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left


num = [3,7,9,16,38,24,27,38,44,49,21,52,63,15]
print(solution1(num))
