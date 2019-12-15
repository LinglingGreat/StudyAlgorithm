# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 18:30
# @Author  : Liling
# -*- coding:utf-8 -*-
"""
小红书笔试题
给定层次遍历和中序遍历，从左到右输出叶子节点，输出前序遍历和后序遍历
"""
class Node:
    def __init__(self, x):
        self.data = x
        self.lchild = None
        self.rchild = None
class Solution:

    def __init__(self):
        self.list1=[]
        self.list2=[]
        self.list3=[]

    def reConstructBinaryTree(self, lev, mid):
        if len(lev)==0 or len(mid)==0:
            self.list2.append(Node(-1))
            return Node(-1)
        data = lev.pop(0)
        root=Node(data)
        #直接得到前序遍历
        self.list1.append(root)

        index=mid.index(data)

        #递归得到后序遍历
        temp_mid1=mid[0:index]
        temp_lev1=[i for i in lev if i in temp_mid1]
        root.lchild=self.reConstructBinaryTree(temp_lev1,temp_mid1)

        temp_mid2 = mid[index+1:]
        temp_lev2 = [i for i in lev if i in temp_mid2]
        root.rchild=self.reConstructBinaryTree(temp_lev2,temp_mid2)
        self.list2.append(root)

        if len(temp_lev1)==0 and len(temp_lev2)==0 and len(temp_mid1)==0 and len(temp_mid2)==0:
            self.list3.append(root)
        return root

lev=[int(i) for i in input().split(' ')]
mid=[int(i) for i in input().split(' ')]

s=Solution()
s.reConstructBinaryTree(lev,mid)

#输出叶子结点
l=[str(i.data) for i in s.list3 if i.data!=-1]
print(' '.join(l))

#输出前序遍历
l=[str(i.data) for i in s.list1 if i.data!=-1]
print(' '.join(l))

#输出树的后序遍历
l=[str(i.data) for i in s.list2 if i.data!=-1]
print(' '.join(l))

