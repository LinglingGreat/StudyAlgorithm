# 2021-09-02 09:23:26
# 剑指 Offer II 053
# 二叉搜索树中的中序后继, P5rCT8

# 给定一棵二叉搜索树和其中的一个节点 p ，找到该节点在树中的中序后继。如果节点没有中序后继，请返回 null 。 
# 
#  节点 p 的后继是值比 p.val 大的节点中键值最小的节点，即按中序遍历的顺序节点 p 的下一个节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [2,1,3], p = 1
# 输出：2
# 解释：这里 1 的中序后继是 2。请注意 p 和返回值都应是 TreeNode 类型。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [5,3,6,2,4,null,null,1], p = 6
# 输出：null
# 解释：因为给出的节点没有中序后继，所以答案就返回 null 了。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在范围 [1, 10⁴] 内。 
#  -10⁵ <= Node.val <= 10⁵ 
#  树中各节点的值均保证唯一。 
#  
# 
#  
# 
#  注意：本题与主站 285 题相同： https://leetcode-cn.com/problems/inorder-successor-in-bst/ 
# 
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 3 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        '''
        stack = []
        cur = root
        flag = False  # 标记是否找到
        # 中序遍历，找到p后，终须遍历的下一个节点就是
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if flag:
                break
            elif cur == p:
                flag = True
            cur = cur.right
        return cur
        '''
        # 记录比p大的节点
        res = None
        cur = root
        while cur:
            # 如果当前节点比p大，记录下当前节点，然后往左走找比p大但是更小的下一个节点
            if cur.val > p.val:
                res = cur
                cur = cur.left
            # 如果小于等于p，那么往右走才能找到比p大的节点
            else:
                cur = cur.right
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
