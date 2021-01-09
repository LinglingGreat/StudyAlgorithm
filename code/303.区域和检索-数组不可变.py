#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        # 每个位置存的是该元素之前所有元素之和（不包括该元素）
        self.sumrange = [0] * (len(nums)+1)
        for i in range(1, (len(nums)+1)):
            self.sumrange[i] = self.sumrange[i-1] + nums[i-1]



    def sumRange(self, i: int, j: int) -> int:
        return self.sumrange[j+1] - self.sumrange[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

