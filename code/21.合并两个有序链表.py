#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """使用两个指针指向两个链表，递归地比较，将较小的赋给新链表的下一个结点。注意边界条件"""
        if not l1:
            return l2
        if not l2:
            return l1
        p1, p2 = l1, l2
        if p1.val <= p2.val:
            l = p1
            p1 = p1.next
        else:
            l = p2
            p2 = p2.next
        p = l
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return l

        
# @lc code=end

