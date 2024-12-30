#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
# https://leetcode.cn/problems/zigzag-conversion/description/
#
# algorithms
# Medium (53.01%)
# Likes:    2342
# Dislikes: 0
# Total Accepted:    698.7K
# Total Submissions: 1.3M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
# 
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
# 
# 请你实现这个将字符串进行指定行数变换的函数：
# 
# 
# string convert(string s, int numRows);
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
# 
# 示例 2：
# 
# 
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
# 
# 示例 3：
# 
# 
# 输入：s = "A", numRows = 1
# 输出："A"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 由英文字母（小写和大写）、',' 和 '.' 组成
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        # 每行元素存储到res中
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)

# @lc code=end

