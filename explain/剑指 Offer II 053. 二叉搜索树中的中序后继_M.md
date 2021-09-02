#### [剑指 Offer II 053. 二叉搜索树中的中序后继](https://leetcode-cn.com/problems/P5rCT8/)

难度：中等

标签：[树](../Topic/树.md)，[深度优先搜索](../Topic/深度优先搜索.md)

给定一棵二叉搜索树和其中的一个节点 p ，找到该节点在树中的中序后继。如果节点没有中序后继，请返回 null 。

节点 p 的后继是值比 p.val 大的节点中键值最小的节点，即按中序遍历的顺序节点 p 的下一个节点。

 本题与主站 285 题相同： [285. 二叉搜索树中的中序后继](https://leetcode-cn.com/problems/inorder-successor-in-bst)（要会员解锁）


示例 1：


输入：root = [2,1,3], p = 1
输出：2
解释：这里 1 的中序后继是 2。请注意 p 和返回值都应是 TreeNode 类型。
示例 2：


输入：root = [5,3,6,2,4,null,null,1], p = 6
输出：null
解释：因为给出的节点没有中序后继，所以答案就返回 null 了。


提示：

树中节点的数目在范围 [1, 10^4] 内。
-10^5 <= Node.val <= 10^5
树中各节点的值均保证唯一。



#### 解法一：中序遍历

解决这个问题的最直观的思路就是采用二叉树的中序遍历。可以用一个布尔变量found来记录已经遍历到节点p。该变量初始化为false，遍历到节点p就将它设为true。在这个变量变成true之后遍历到的第1个节点就是要找的节点。

```python
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = []
        cur = root
        flag = False  # 标记是否找到
        # 中序遍历，找到p后，终须遍历的下一个节点就是
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if flag:
                break
            elif cur == p:
                flag = True
            cur = cur.right
        return cur
```

由于中序遍历会逐一遍历二叉树的每个节点，如果二叉树有n个节点，那么这种思路的时间复杂度就是O（n）。同时，需要用一个栈保存顺着指向左子节点的指针的路径上的所有节点，因此空间复杂度为O（h），其中h为二叉树的深度。

#### 解法二

下面换一个角度来看待二叉搜索树中节点p的中序遍历下一个节点。首先下一个节点的值一定不会小于节点p的值，而且还是大于或等于节点p的值的所有节点中值最小的一个。

下面按照在二叉搜索树中根据节点的值查找节点的思路来分析。从根节点开始，每到达一个节点就比较根节点的值和节点p的值。如果当前节点的值小于或等于节点p的值，那么节点p的下一个节点应该在它的右子树。如果当前节点的值大于节点p的值，那么当前节点有可能是它的下一个节点。此时当前节点的值比节点p的值大，但节点p的下一个节点是所有比它大的节点中值最小的一个，因此接下来前往当前节点的左子树，确定是否能找到值更小但仍然大于节点p的值的节点。重复这样的比较，直至找到最后一个大于节点p的值的节点，就是节点p的下一个节点。

```python
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # 记录比p大的节点
        res = None
        cur = root
        while cur:
            # 如果当前节点比p大，记录下当前节点，然后往左走找比p大但是更小的下一个节点
            if cur.val > p.val:
                res = cur
                cur = cur.left
            # 如果小于等于p，那么往右走才能找到比p大的节点
            else:
                cur = cur.right
        return res
```





由于while循环每运行一次都会顺着指向左子节点或右子节点的指针前往下一层节点，因此while循环执行的次数等于二叉搜索树的深度。如果把二叉树的深度记为h，那么该算法的时间复杂度为O（h）。同时，上述代码除几个变量外没有其他内存开销，因此空间复杂度是O（1）。
