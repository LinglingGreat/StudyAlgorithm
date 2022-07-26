#
# @lc app=leetcode.cn id=421 lang=python3
#
# [421] 数组中两个数的最大异或值
#
# https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (62.25%)
# Likes:    385
# Dislikes: 0
# Total Accepted:    32.6K
# Total Submissions: 52.4K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
# 
# 进阶：你可以在 O(n) 的时间解决这个问题吗？
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28.
# 
# 示例 2：
# 
# 
# 输入：nums = [0]
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [2,4]
# 输出：6
# 
# 
# 示例 4：
# 
# 
# 输入：nums = [8,10,2]
# 输出：10
# 
# 
# 示例 5：
# 
# 
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
# 
# 
#

# @lc code=start
class Trie:
    def __init__(self):
        # 左子树指向表示 0 的子节点
        self.left = None
        # 右子树指向表示 1 的子节点
        self.right = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # 字典树的根节点
        root = Trie()
        # 最高位的二进制位编号为 30
        HIGH_BIT = 30

        def add(num: int):
            cur = root
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    if not cur.left:
                        cur.left = Trie()
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Trie()
                    cur = cur.right

        def check(num: int) -> int:
            cur = root
            x = 0
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    # a_i 的第 k 个二进制位为 0，应当往表示 1 的子节点 right 走
                    if cur.right:
                        cur = cur.right
                        x = x * 2 + 1
                    else:
                        cur = cur.left
                        x = x * 2
                else:
                    # a_i 的第 k 个二进制位为 1，应当往表示 0 的子节点 left 走
                    if cur.left:
                        cur = cur.left
                        x = x * 2 + 1
                    else:
                        cur = cur.right
                        x = x * 2
            return x

        n = len(nums)
        x = 0
        for i in range(1, n):
            # 将 nums[i-1] 放入字典树，此时 nums[0 .. i-1] 都在字典树中
            add(nums[i - 1])
            # 将 nums[i] 看作 ai，找出最大的 x 更新答案
            x = max(x, check(nums[i]))

        return x
# @lc code=end

