#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        node = root
        while node.left:
            current = node
            while current:
                # left节点的next是right节点
                current.left.next = current.right
                if current.next:
                    current.right.next = current.next.left
                current = current.next
            node = node.left
        return root

        
# @lc code=end

