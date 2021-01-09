#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        """结果可能有2种，一种是数字到达1，另一种是陷入循环。定义哈希表存放历史已经计算过的数字，来判断是否陷入第二种情况"""
        numset = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in numset:
                return False
            numset.add(n)
        return True
        
# @lc code=end

