#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#
# https://leetcode.cn/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (71.16%)
# Likes:    1037
# Dislikes: 0
# Total Accepted:    487.7K
# Total Submissions: 680.7K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你单链表的头结点 head ，请你找出并返回链表的中间结点。
# 
# 如果有两个中间结点，则返回第二个中间结点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5]
# 输出：[3,4,5]
# 解释：链表只有一个中间结点，值为 3 。
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,2,3,4,5,6]
# 输出：[4,5,6]
# 解释：该链表有两个中间结点，值分别为 3 和 4 ，返回第二个结点。
# 
# 
# 
# 
# 提示：
# 
# 
# 链表的结点数范围是 [1, 100]
# 1 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
# @lc code=end

