# 实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），假定你只能访问该节点。 
# 
#  
# 
#  示例： 
# 
#  输入：单向链表a->b->c->d->e->f中的节点c
# 结果：不返回任何数据，但该链表变为a->b->d->e->f
#  
#  Related Topics 链表 
#  👍 94 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 只能访问该结点，那么删除该结点的方式就是将该结点变成下一个结点，然后删除下一个。
        node.val = node.next.val
        node.next = node.next.next
        
# leetcode submit region end(Prohibit modification and deletion)
