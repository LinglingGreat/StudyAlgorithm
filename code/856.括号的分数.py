#
# @lc app=leetcode.cn id=856 lang=python3
#
# [856] 括号的分数
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()

# @lc code=end

