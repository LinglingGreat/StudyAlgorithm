#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """插入排序，注意创建哑节点，并且维护排序链表的最后一个节点"""
        if not head or not head.next:
            return head
        # 创建哑节点
        newhead = ListNode(0)
        newhead.next = head
        # 维护排序链表的最后一个节点
        lastSorted = head
        res = head.next
        while res:
            # 新节点刚好应该插入排序链表的最后，直接后移即可
            if lastSorted.val <= res.val:
                lastSorted = lastSorted.next
            # 需要从前往后寻找插入的位置
            else:
                prev = newhead
                while prev.next.val <= res.val:
                    prev = prev.next
                # 删除当前节点
                lastSorted.next = res.next
                # 插入当前节点
                res.next, prev.next = prev.next, res
            res = lastSorted.next
        return newhead.next
# @lc code=end

