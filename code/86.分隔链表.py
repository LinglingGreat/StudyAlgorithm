#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (62.52%)
# Likes:    389
# Dislikes: 0
# Total Accepted:    97.9K
# Total Submissions: 156.1K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
# 
# 你应当 保留 两个分区中每个节点的初始相对位置。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [2,1], x = 2
# 输出：[1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 200] 内
# -100 
# -200 
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyNode = ListNode(0)
        dummyNode.next = head
        pos = dummyNode
        # 找到第一个比x大的结点的前一个结点,作为插入点
        while pos.next and pos.next.val < x:
            pos = pos.next
        newcur = pos
        # 将小的值插入pos后面
        while newcur and newcur.next:
            if newcur.next.val < x:
                tmp1 = pos.next
                tmp2 = newcur.next
                pos.next = newcur.next
                newcur.next = tmp2.next
                tmp2.next = tmp1
                pos = pos.next  # 更新插入点
            else:
                newcur = newcur.next
        return dummyNode.next
# @lc code=end

