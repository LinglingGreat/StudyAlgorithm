#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
#
# https://leetcode-cn.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (74.55%)
# Likes:    241
# Dislikes: 0
# Total Accepted:    61.1K
# Total Submissions: 81.9K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
#
# 给你一棵二叉搜索树，请你 按中序遍历
# 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# 
# 
# 示例 2：
# 
# 
# 输入：root = [5,1,7]
# 输出：[1,null,5,null,7]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数的取值范围是 [1, 100]
# 0 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        first = None
        prev = None
        cur = root 
        # 中序遍历
        while cur or stack:
            # 先找到最左边的节点
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            # 如果存在前一个节点，right指向当前节点，否则当前节点就是根节点
            if prev:
                prev.right = cur
            else:
                first = cur  
            prev = cur 
            # left是None
            cur.left = None
            # 下一个节点
            cur = cur.right
        return first


# @lc code=end

