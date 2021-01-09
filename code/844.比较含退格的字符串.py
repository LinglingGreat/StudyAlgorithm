#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        trueS = ''
        trueT = ''
        for i in S:
            if i != '#':
                trueS += i
            elif len(trueS) >= 1:
                trueS = trueS[:-1]
        for i in T:
            if i != '#':
                trueT += i
            elif len(trueT) >= 1:
                trueT = trueT[:-1]
        if trueS == trueT:
            return True
        return False
        
# @lc code=end

