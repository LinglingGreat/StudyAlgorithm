#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_dict = {'(': ')', '[':']', '{':'}'}
        for i in s:
            if not stack:
                stack.append(i)
            elif i in ['(', '[', '{']:
                stack.append(i)
            else:
                val = valid_dict.get(stack[-1], '')
                if val != i:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        return False
# @lc code=end

