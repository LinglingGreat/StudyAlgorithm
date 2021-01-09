#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 翻转一个子链表，并且返回新的头与尾
        def reverse(head, tail):
            prev = tail.next
            p = head
            while prev != tail:
                # nex是当前节点的后继节点，prev是当前节点的前驱节点
                # 当前结点的next指向上一个节点
                nex, p.next = p.next, prev
                # 当前结点变成前驱节点，后继节点变成当前节点
                prev = p
                p = nex
            return tail, head

        # 创建一个哑节点
        dummyhead = ListNode(0)
        dummyhead.next = head
        pre = dummyhead  # 记录最新的末尾的节点
        while head:
            tail = pre
            # 每k个为一组
            for i in range(k):
                tail = tail.next
                # 如果不足k个，说明已经翻转结束
                if not tail:
                    return dummyhead.next
            # 为下一组的开头
            nex = tail.next
            # 这一组的head和tail节点
            head, tail = reverse(head, tail)
            # 翻转的链表接到pre和下一组之间
            pre.next, tail.next = head, nex
            # 更新pre和head
            pre, head = tail, tail.next
        return dummyhead.next

        
# @lc code=end

