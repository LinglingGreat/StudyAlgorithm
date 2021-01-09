#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        # 快慢指针，当快指针走到末尾的时候，慢指针正好在中间
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # 利用慢指针反转后半部分链表
        # 注意此时slow在前半部分的最后一个结点
        slow = slow.next
        # slow表示当前在处理的结点
        # previous用来记录当前结点的前一个结点，反转后成为当前结点的next
        # 循环结束后，slow是None, previous是它的前一个结点，也就是原始链表的最后一个结点，也是反转后链表的第一个结点
        previous = None
        while slow:
            slow.next, slow, previous = previous, slow.next, slow
        while head and previous:
            if head.val != previous.val:
                return False
            head, previous = head.next, previous.next
        return True

# @lc code=end

