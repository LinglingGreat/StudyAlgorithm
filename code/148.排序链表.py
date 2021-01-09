#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        首先根据时间复杂度想到二分法，进而想到归并排序，那么需要将链表分成2个部分（利用快慢指针找到中点）
        递归地调用归并排序
        """
        # 边界条件，直接返回
        if not head or not head.next:
            return head
        # 快慢指针,找到中间结点
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
        # 从中间切断，mid开始是后半段
        mid, slow.next = slow.next, None
        # 排序两个部分
        left, right = self.sortList(head), self.sortList(mid)
        # 两个部分的合并
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next
# @lc code=end

