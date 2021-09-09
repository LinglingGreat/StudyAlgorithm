# @lc code=start
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        a0 = costs[0][0]
        a1 = costs[0][1]
        a2 = costs[0][2]
        
        for i in range(1, n):
            b0 = min(a1, a2) + costs[i][0]
            b1 = min(a0, a2) + costs[i][1]
            b2 = min(a0, a1) + costs[i][2]
            a0, a1, a2 = b0, b1, b2
            
        return min(a0, a1, a2)
# @lc code=end