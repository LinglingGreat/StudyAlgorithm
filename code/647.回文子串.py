#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
# https://leetcode-cn.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (65.07%)
# Likes:    561
# Dislikes: 0
# Total Accepted:    92.5K
# Total Submissions: 141.9K
# Testcase Example:  '"abc"'
#
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
# 
# 
# 
# 示例 1：
# 
# 输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
# 
# 
# 示例 2：
# 
# 输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
# 
# 
# 
# 提示：
# 
# 
# 输入的字符串长度不会超过 1000 。
# 
# 
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(2*n-1):
            l = i // 2
            r = i // 2 + i % 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                ans += 1
        return ans
        
# @lc code=end

