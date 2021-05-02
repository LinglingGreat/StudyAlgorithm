#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#
# https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/description/
#
# algorithms
# Easy (79.41%)
# Likes:    90
# Dislikes: 0
# Total Accepted:    35.5K
# Total Submissions: 44.6K
# Testcase Example:  '"RLRRLLRLRL"'
#
# 在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。
# 
# 给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
# 
# 注意：分割得到的每个字符串都必须是平衡字符串。
# 
# 返回可以通过分割得到的平衡字符串的 最大数量 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "RLRRLLRLRL"
# 输出：4
# 解释：s 可以分割为 "RL"、"RRLL"、"RL"、"RL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "RLLLLRRRLR"
# 输出：3
# 解释：s 可以分割为 "RL"、"LLLRRR"、"LR" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "LLLLRRRR"
# 输出：1
# 解释：s 只能保持原样 "LLLLRRRR".
# 
# 
# 示例 4：
# 
# 
# 输入：s = "RLRRRLLRLL"
# 输出：2
# 解释：s 可以分割为 "RL"、"RRRLLRLL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s[i] = 'L' 或 'R'
# s 是一个 平衡 字符串
# 
# 
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        nums = 0
        ans = 0
        for i in s:
            if i == 'L':
                nums += 1
            else:
                nums -= 1
            if nums == 0:
                ans += 1
        return ans
# @lc code=end

