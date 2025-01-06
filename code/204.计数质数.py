#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode.cn/problems/count-primes/description/
#
# algorithms
# Medium (37.01%)
# Likes:    1199
# Dislikes: 0
# Total Accepted:    295K
# Total Submissions: 797.5K
# Testcase Example:  '10'
#
# 给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 0
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：n = 1
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 5 * 10^6
# 
# 
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False

        count = 0
        for i in range(2, n):
            if isPrime[i]: 
                count += 1

        return count
        
# @lc code=end

