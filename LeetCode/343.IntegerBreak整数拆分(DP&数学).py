# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-15 16:33:36
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-15 17:16:08
"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
"""
"""
棒！自己想出来的，终于开窍了！
"""
class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 2:
        	return 1
        maxmul = 0
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(2, n+1):
        	for j in range(1, i):
        		dp[i] = max(dp[i], j*dp[i-j], j*(i-j))
        # print(dp)
        return dp[n]

s=Solution()
print(s.integerBreak(10))

"""
其它解法
O(N)
整数分解成两个数时，两个数相等的时候乘积最大
一个很大的整数分解成若干个数的时候，也是这若干个数相等的时候乘积最大
在某个点如果要break，必须保证(N/2)*(N/2)>=N,解出n>=4
或者(N-1)/2*(N+1)/2>=N,解出N>=5（对于奇数）
这说明当N<4时，不需要拆分，所以可拆分的因子有1,2,3.
显然，1不用考虑，最好的拆分数应该是2或者3
那么为什么是3呢，对于6，有3*3>2*2*2，因此，最优的拆分不应该包括多于两个2
https://leetcode.com/problems/integer-break/discuss/80689/A-simple-explanation-of-the-math-part-and-a-O(n)-solution
https://leetcode.com/problems/integer-break/discuss/80721/Why-factor-2-or-3-The-math-behind-this-problem.
"""
class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
        	return 1
        if n==3:
        	return 2
        product = 1
        while n>4:
        	product *= 3
        	n -= 3
        product *= n
        return product