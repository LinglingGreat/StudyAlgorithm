#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False
        positive = True
        if A[0] >= A[1]:
            return False
        for i in range(1, n-1):
            # 增长趋势转下降趋势
            if positive and A[i] < A[i-1]:
                positive = False
                continue
            # 下降趋势时
            if not positive and A[i] > A[i-1]:
                return False
            if A[i] == A[i-1]:
                return False
        if A[n-2] <= A[n-1]:
            return False
        return True
        
# @lc code=end

