# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-14 22:04:21
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-16 14:14:05
# https://www.jianshu.com/p/0190985635eb
class TreeNode:
	def __init__(self, val=0):
		self.val = val
		self.left = None
		self.right = None

"""
求二叉树的最大深度
"""
def maxDeath(node):
	if not node:
		return 0
	left = maxDeath(node.left)
	right = maxDeath(node.right)
	return max(left, right) + 1

"""
求二叉树的最小深度
"""
def getMin(root):
	if not root:
		return float('inf')
	if not root.left and not root.right:
		return 1
	return min(getMin(root.left), getMin(root.right)) + 1

def getMinDepth(root):
	if not root:
		return 0
	return getMin(root)

'''
求二叉树中节点的个数
'''
def numOfTreeNode(root):
	if not root:
		return 0
	left = numOfTreeNode(root.left)
	right = numOfTreeNode(root.right)
	return left + right + 1

'''
求二叉树中叶子节点的个数
'''
def numsOfNoChildNode(root):
	if not root:
		return 0
	if not root.left and not root.right:
		return 1
	return numsOfNoChildNode(root.left)+numsOfNoChildNode(root.right)

'''
求二叉树中第K层节点的个数
'''
def numsOfkLevelTreeNode(root, k):
	if (not root) or k < 1:
		return 0
	if k == 1:
		return 1
	numsLeft = numsOfkLevelTreeNode(root.left, k-1)
	numsRight = numsOfkLevelTreeNode(root.right, k-1)
	return numsLeft + numsRight

'''
判断二叉树是否是平衡二叉树
'''
def maxDeath2(node):
	if not node:
		return 0
	left = maxDeath2(node.left)
	right = maxDeath2(node.right)
	if left == -1 or right == -1 or abs(left-right)>1: # 子树不平衡
		return -1
	return max(left, right) + 1

def isBalanced(node):
	return maxDeath2(node) != -1

'''
判断二叉树是否是完全二叉树
'''
def isCompleteTreeNode(root):
	if not root:
		return False
	queue = [root]
	result = True
	hasNoChild = False
	while queue:    # 层次遍历
		current = queue.pop(0)
		if hasNoChild:
			if current.left or current.right:
				result = False
				break
		else:
			if current.left and current.right:
				queue.append(current.left)
				queue.append(current.right)
			# 当遇到只有左子树的分支时，看左子树是不是有孩子，如果有，返回False
			elif current.left and not current.right:
				queue.append(current.left)
				hasNoChild = True
			# 如果没有左子树，却有右子树，返回False
			elif not current.left and current.right:
				result = False
				break
			# 如果左右子树都没有，那就看下一个节点是否有左右子树，有，返回False
			else:
				hasNoChild = True

	return result

'''
判断两个二叉树是否完全相同
'''
def isSameTreeNode(t1, t2):
	if not t1 and not t2:
		return True
	elif not t1 or not t2:
		return False
	if t1.val != t2.val:
		return False
	left = isSameTreeNode(t1.left, t2.left)
	right = isSameTreeNode(t1.right, t2.right)
	return left and right

'''
两个二叉树是否互为镜像
'''
def isMirror(t1, t2):
	if not t1 and not t2:
		return True
	if not t1 or not t2:
		return False
	if t1.val != t2.val:
		return False
	return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

'''
翻转二叉树or镜像二叉树
'''
def mirrorTreeNode(root):
	if not root:
		return None 
	left = mirrorTreeNode(root.left)
	right = mirrorTreeNode(root.right)
	root.left = right
	root.right = left
	return root

'''
求两个二叉树的最低公共祖先节点
'''
# 查找节点node是否在当前二叉树中
def findNode(root, node):
	if not root or not node:
		return False
	if root == node:
		return True
	found = findNode(root.left, node)
	if not found:
		found = findNode(root.right, node)
	return found

def getLastCommonParent(root, t1, t2):
	if findNode(root.left, t1):
		if findNode(root.right, t2):
			return root
		else:
			return getLastCommonParent(root.left, t1, t2)
	else:
		if findNode(root.left, t2):
			return root
		else:
			return getLastCommonParent(root.right, t1, t2)

'''
二叉树的前序遍历
'''
# 迭代解法
from collections import deque
def preOrder(root):
	li = list()
	if not root:
		return li
	stack = deque(root)
	while stack:
		node = stack.pop()
		li.append(node.val)
		if node.right:
			stack.append(node.right)
		if node.left:
			stack.append(node.left)
	return li

# 递归解法
def preOrder2(root, result):
	if not root:
		return None
	result.append(root.val)
	preOrder2(root.left, result)
	preOrder2(root.right, result)

def preOrderReverse(root):
	result = []
	preOrder2(root, result)
	return result
'''
二叉树的中序遍历
'''
def inOrder(root):
	li = list()
	current = root
	stack = list()
	while current or stack:
		while current:
			stack.append(current)
			current = current.left
		current = stack[-1]
		stack.pop()
		li.append(current.val)
		current = current.right
	return li

'''
二叉树的后序遍历
'''
def postOrder():
	li = []
	if not root:
		return li
	li.append(postOrder(root.left))
	li.append(postOrder(root.right))
	li.append(root.val)
	return li

'''
前序遍历和中序遍历构造二叉树,注意：已知前序和后序无法确定二叉树
'''
def findPosition(arr, start, end, key):
	for i in range(start, end+1):
		if arr[i] == key:
			return i
	return -1

def myBuildTree(inorder, instart, inend, preorder, prestart, preend):
	if instart > inend:
		return None
	# 前序遍历的第一个节点就是根节点
	root = TreeNode(preorder[prestart])
	# 找到前序遍历的起始节点在中序遍历中的位置，将中序遍历分成两部分
	position = findPosition(inorder, instart, inend, preorder[prestart])
	# 第一部分是根节点之前的遍历，是根节点的左子树
	root.left = myBuildTree(inorder, instart, position-1, preorder, prestart+1, prestart+position-instart)
	# 第二部分是根节点之后的遍历，是根节点的右子树
	root.right = myBuildTree(inorder, position+1, inend, preorder, position-inend+preend+1, preend)
	return root

def bulidTreeNode(preorder, inorder):
	if len(preorder) != len(inorder):
		return None
	return myBuildTree(inorder, 0, len(inorder)-1, preorder, 0, len(preorder)-1)

'''
在二叉树中插入节点
'''
def insertNode(root, node):
	if root == node:
		return node
	tmp = root
	last = None
	# 找到插入节点的位置
	while tmp:
		last = tmp
		if tmp.val > node.val:
			tmp = tmp.left
		else:
			tmp = tmp.right
	if last:
		if last.val>node.val:
			last.left = node
		else:
			last.right = node
	return root

'''
输入一个二叉树和一个整数，打印出二叉树中节点值的和等于输入整数所有的路径
'''
def findPath(r, i, stack, currentSum):
	currentSum += r.val
	stack.append(r.val)
	# 左右子树为空时，检验是否已经找到完整路径，输出路径
	if not r.left and not r.right:
		if currentSum == i:
			for p in stack:
				print(p)
	# 左子树中找
	if r.left:
		findPath(r.left, i, stack, currentSum)
	# 右子树中找
	if r.right:
		findPath(r.right, i, stack, currentSum)
	# stack的最后一个节点的后续路径已检测完，删掉该节点
	stack.pop()

def findAllPath(r, i):
	if not root:
		return None
	stack = []
	currentSum = 0
	findPath(r, i, stack, currentSum)

'''
二叉树的搜索区间
给定两个值 k1 和 k2（k1 < k2）和一个二叉查找树的根节点。找到树中所有值在 k1 到 k2 范围内的节点。
即打印所有x (k1 <= x <= k2) 其中 x 是二叉查找树的中的节点值。返回所有升序的节点值。
'''
def searchHelper(root, k1, k2):
	if not root:
		return None
	if root.val > k1:
		searchHelper(root.left, k1, k2)
	if root.val >= k1 and root.val <= k2:
		result.append(root.val)
	if root.val < k2:
		serachHelper(root.right, k1, k2)

def searchRange(root, k1, k2):
	result = list()
	searchHelper(root, k1, k2)
	return result

'''
二叉树的层次遍历
'''
def leverOrder(root):
	result = list()
	if not root:
		return result
	queue = list()
	queue.append(root)
	while queue:
		size = len(queue)
		level = list()
		for i in range(size):
			node = queue.pop(0)
			level.append(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		result.extend(level)
	return result

'''
二叉树内两个节点的最长距离
二叉树中两个节点的最长距离可能有三种情况：
1.左子树的最大深度+右子树的最大深度为二叉树的最长距离
2.左子树中的最长距离即为二叉树的最长距离
3.右子树中的最长距离即为二叉树的最长距离
因此，递归求解即可
'''
class Result:
	def __init__(self, maxDistance=0, maxDepth=0):
		self.maxDistance = maxDistance
		self.maxDepth = maxDepth

def getMaxDistanceResult(root):
	if not root:
		empty = Result(0, -1)
		return empty
	lmd = getMaxDIstanceResult(root.left)
	rmd = getMaxDistanceResult(root.right)
	result = Result()
	result.maxDepth = max(lmd.maxDepth, rmd.maxDepth) + 1
	result.maxDistance = max(lmd.maxDepth + rmd.maxDepth, max(lmd.maxDistance, rmd.maxDistance))
	return result

def getMaxDistance(root):
	return getMaxDistanceResult(root).maxDistance

'''
不同的二叉树
给出 n，问由 1…n 为节点组成的不同的二叉查找树有多少种？
'''
def numTrees(n):
	counts = [0]*(n+1)
	counts[0] = 1
	counts[1] = 1
	for i in range(2, n+1):
		for j in range(i):
			counts[i] += counts[j] * counts[i-j-1]
	return counts[n]

'''
判断二叉树是否是合法的二叉查找树(BST)
一棵BST定义为：
节点的左子树中的值要严格小于该节点的值。
节点的右子树中的值要严格大于该节点的值。
左右子树也必须是二叉查找树。
一个节点的树也是二叉查找树。
'''
lastVal = float('inf')
firstNode = True
def isValidBST(root):
	if not root:   # 空
		return True
	if not isValidBST(root.left):    # 左子树是否合法
		return False
	if not firstNode and lastVal >= root.val:    # lastVal是root的根节点的值
		return False
	firstNode = False
	lastVal = root.val
	if not isValidBST(root.right):    # 右子树是否合法
		return False
	return True
