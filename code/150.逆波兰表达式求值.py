#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack1 = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                op2 = stack1.pop()
                op1 = stack1.pop()
                if i == '+':
                    result = op1 + op2
                elif i == '-':
                    result = op1 - op2
                elif i == '*':
                    result = op1 * op2
                else:
                    # 注意python整除是向下取整，所以改用除法
                    result = int(op1 / op2)
                stack1.append(result)
            else:
                stack1.append(int(i))
        return stack1[-1]
# @lc code=end

