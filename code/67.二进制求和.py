#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (54.41%)
# Likes:    601
# Dislikes: 0
# Total Accepted:    162.6K
# Total Submissions: 299K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 
# 输入为 非空 字符串且只包含数字 1 和 0。
# 
# 
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
# 
# 
# 提示：
# 
# 
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        carry = 0
        ans = []
        for i in range(n):
            # 倒数第i个字符
            if i < len(a):
                carry += int(a[len(a)-1-i])
            if i < len(b):
                carry += int(b[len(b)-1-i])
            ans.append(str(carry % 2))
            # 进位
            carry //= 2
        if carry > 0:
            ans.append('1')
        return "".join(ans[::-1])
            
# @lc code=end

