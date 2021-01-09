#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ishuiwen(s):
            start = 0
            end = len(s) - 1
            while start<end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return ishuiwen(s[low+1:high+1]) or ishuiwen(s[low:high])
        return True

        
        
# @lc code=end

