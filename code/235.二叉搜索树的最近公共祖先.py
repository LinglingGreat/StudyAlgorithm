#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (65.96%)
# Likes:    519
# Dislikes: 0
# Total Accepted:    118.2K
# Total Submissions: 179.1K
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 
# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6 
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
# 
# 
# 示例 2:
# 
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
# 
# 
# 
# 说明:
# 
# 
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 二叉搜索树：左子树上所有结点的值均小于它的根结点的值，右子树上所有结点的值均大于它的根结点的值
        ancestor = root
        while True:
            # 如果都在左子树
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            # 如果都在右子树
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            # 分别在左右子树，或者当前节点就是其中一个节点，此时已找到共同父节点
            else:
                break
        return ancestor
        
# @lc code=end

