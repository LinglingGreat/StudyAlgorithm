'''
输入一个链表，输出该链表中倒数第k个结点。
'''

'''
这道题的思路很好
如果在只希望一次遍历的情况下, 寻找倒数第k个结点, 可以设置两个指针
第一个指针先往前走k-1步, 然后从第k步开始第二个指针指向头结点
然后两个指针一起遍历
当第一个指针指向尾节点的时候, 第二个指针正好指向倒数第k个结点
推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,  快指针指到尾部, 慢指针正好指到中间
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if head is None or k <= 0:
            return None

        pAHead = head

        for _ in range(k):
            if pAHead.next:
                pAHead = pAHead.next
            else:   # 越界问题
                return None
        pBehind = head
        while pAHead:
            pAHead = pAHead.next
            pBehind = pBehind.next
        return pBehind

class Solution:
    def FindKthToTail(self, head, k):
        # 用栈，效率会低一些
        l = []
        while head:
            l.append(head)
            head = head.next
        if k>len(l) or k<1:
            return
        return l[-k]
        
node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

S = Solution()
print(S.FindKthToTail(node1, 1).val)