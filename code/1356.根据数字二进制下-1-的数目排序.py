#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#

# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        return sorted(arr,key=lambda x:(bin(x).count('1')*10000000+x))
# @lc code=end

