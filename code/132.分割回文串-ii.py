#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
# https://leetcode-cn.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (49.25%)
# Likes:    472
# Dislikes: 0
# Total Accepted:    48.7K
# Total Submissions: 99K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
# 
# 返回符合要求的 最少分割次数 。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "a"
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：s = "ab"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由小写英文字母组成
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        f = [float("inf")] * n
        for i in range(n):
            if g[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if g[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1)
        
        return f[n - 1]
# @lc code=end

