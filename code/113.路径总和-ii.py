#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (61.37%)
# Likes:    405
# Dislikes: 0
# Total Accepted:    110.2K
# Total Submissions: 179.5K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 返回:
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        tmp = []
        def dfs(node, tmpsum):
            # 当前结点
            if not node:
                return
            tmp.append(node.val)
            tmpsum += node.val
            # 当前结点是叶子结点时，为什么这里不return，因为后面还要回溯
            if not node.left and not node.right:
                if tmpsum == sum:
                    res.append(tmp[:])
            # 深度遍历当前结点的左右结点
            dfs(node.left, tmpsum)
            dfs(node.right, tmpsum)
            # 记得回溯
            tmp.pop()

        dfs(root, 0)
        return res
                
            
# @lc code=end

