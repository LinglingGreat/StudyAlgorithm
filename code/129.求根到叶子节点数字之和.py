#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, prenum: int) -> int:
            if not root:
                return 0
            total = prenum * 10 + root.val
            if (not root.left) and (not root.right):
                return total
            return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)
# @lc code=end

