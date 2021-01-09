#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashdict = {}
        for i in arr:
            if i in hashdict:
                hashdict[i] += 1
            else:
                hashdict[i] = 1
        numdict = {}
        for k, v in hashdict.items():
            if v in numdict:
                return False
            numdict[v] = 1
        return True
        
# @lc code=end

