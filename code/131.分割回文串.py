#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (70.14%)
# Likes:    454
# Dislikes: 0
# Total Accepted:    58.1K
# Total Submissions: 82.8K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回 s 所有可能的分割方案。
# 
# 示例:
# 
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def checkPalindrome(str, left, right):
            while left < right:
                if str[left] != str[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(s, start, len):
            if start == len:
                res.append(copy.deepcopy(stack))
                return
            for i in range(start, len):
                # 因为截取字符串是消耗性能的，因此，采用传子串索引的方式判断一个子串是否是回文子串
                # 不是的话，剪枝
                if not checkPalindrome(s, start, i):
                    continue

                stack.append(s[start:i+1])
                backtrack(s, i + 1, len)
                stack.pop()


        res = []
        n = len(s)
        if n == 0:
            return res
        stack = []
        backtrack(s, 0, n)
        return res
# @lc code=end

