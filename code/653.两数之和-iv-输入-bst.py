#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#
# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (59.46%)
# Likes:    273
# Dislikes: 0
# Total Accepted:    38.7K
# Total Submissions: 65.1K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# 给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
# 
# 
# 
# 示例 1：
# 
# 
# 输入: root = [5,3,6,2,4,null,7], k = 9
# 输出: true
# 
# 
# 示例 2：
# 
# 
# 输入: root = [5,3,6,2,4,null,7], k = 28
# 输出: false
# 
# 
# 示例 3：
# 
# 
# 输入: root = [2,1,3], k = 4
# 输出: true
# 
# 
# 示例 4：
# 
# 
# 输入: root = [2,1,3], k = 1
# 输出: false
# 
# 
# 示例 5：
# 
# 
# 输入: root = [2,1,3], k = 3
# 输出: true
# 
# 
# 
# 
# 提示:
# 
# 
# 二叉树的节点个数的范围是  [1, 10^4].
# -10^4 
# root 为二叉搜索树
# -10^5 
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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        valset = set()
        cur = root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if k-cur.val in valset:
                return True
            else:
                valset.add(cur.val)
            cur = cur.right
        return False

class BSTIterator(object):

    def __init__(self, root):
        self.stack = []
        self.cur = root

    def next(self):
        # 每次取next的时候，中序遍历
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left  
        self.cur = self.stack.pop()
        val = self.cur.val
        self.cur = self.cur.right
        return val

    def hasNext(self):
        return (self.cur!=None) or len(self.stack) > 0

class BSTIteratorReversed(object):

    def __init__(self, root):
        self.stack = []
        self.cur = root

    def next(self):
        # 每次取next的时候，中序遍历
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.right  
        self.cur = self.stack.pop()
        val = self.cur.val
        self.cur = self.cur.left
        return val

    def hasNext(self):
        return (self.cur!=None) or len(self.stack) > 0

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        itersmaller = BSTIterator(root)  # 从小到大
        iterbigger = BSTIteratorReversed(root)   # 从大到小
        smaller = itersmaller.next()
        bigger = iterbigger.next()
        while smaller != bigger:
            if smaller+bigger == k:
                return True
            elif smaller+bigger < k:
                smaller = itersmaller.next()
            else:
                bigger = iterbigger.next()
        return False
        
# @lc code=end

