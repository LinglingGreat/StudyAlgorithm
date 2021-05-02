#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            # 先中间，再左结点，再右结点
            current = stack.pop()
            res.append(current.val)
            # 栈是先入后出，所以先入右结点
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return res


        
# @lc code=end

