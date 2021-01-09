#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newa, newb = newInterval
        placed = False
        res = []
        for le, ri in intervals:
            if le > newb:   # 当前区间应该在新区间的右侧
                if not placed:
                    res.append([newa, newb])
                    placed = True
                res.append([le, ri])
            elif ri < newa:  # 当前区间应该在新区间的左侧
                res.append([le, ri])
            else:  # 当前区间应该和新区间合并
                newa = min(newa, le)
                newb = max(newb, ri)
        if not placed:
            res.append([newa, newb])
        return res

# @lc code=end

