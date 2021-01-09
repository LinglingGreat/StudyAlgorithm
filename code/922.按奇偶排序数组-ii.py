#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        alist = []
        blist = []
        for i in range(len(A)):
            if i%2==0 and A[i]%2 == 1:
                alist.append(i)
            elif i%2==1 and A[i]%2 == 0:
                blist.append(i)
        for i in range(len(alist)):
            A[alist[i]], A[blist[i]] = A[blist[i]], A[alist[i]]
        return A


        
# @lc code=end

