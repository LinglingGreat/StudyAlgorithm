#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        minpathsum = [triangle[0][0]]
        for i in range(1, m):
            newpathsum = [minpathsum[0]+triangle[i][0]]
            for j in range(1, i+1):
                if j == i:
                    minsum = minpathsum[j-1] + triangle[i][j]
                else:
                    minsum = min(minpathsum[j-1], minpathsum[j]) + triangle[i][j]
                newpathsum.append(minsum)
            minpathsum = newpathsum
        return min(minpathsum)

# @lc code=end

