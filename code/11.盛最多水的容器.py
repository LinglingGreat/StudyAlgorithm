#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        用双指针分别指向区域的左边和右边，区域的面积是两点之间的距离*较小的高度。
        因为区域面积取决于较小的高度，所以移动高度较小的指针，才能使得区域面积可能变大。
        """
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            aera = min(height[left], height[right]) * (right-left)
            ans = max(ans, aera)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans

# @lc code=end

