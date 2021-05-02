#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#
# https://leetcode-cn.com/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (44.20%)
# Likes:    229
# Dislikes: 0
# Total Accepted:    17.4K
# Total Submissions: 39.4K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 在本问题中，有根树指满足以下条件的 有向
# 图。该树只有一个根节点，所有其他节点都是该根节点的后继。该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。
# 
# 输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。附加的边包含在 1 到 n
# 中的两个不同顶点间，这条附加的边不属于树中已存在的边。
# 
# 结果图是一个以边组成的二维数组 edges 。 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，其中 ui 是
# vi 的一个父节点。
# 
# 返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：edges = [[1,2],[1,3],[2,3]]
# 输出：[2,3]
# 
# 
# 示例 2：
# 
# 
# 输入：edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
# 输出：[4,1]
# 
# 
# 
# 
# 提示：
# 
# 
# n == edges.length
# 3 
# edges[i].length == 2
# 1 i, vi 
# 
# 
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.ancestor = list(range(n))
    
    def union(self, index1: int, index2: int):
        self.ancestor[self.find(index1)] = self.find(index2)
    
    def find(self, index: int) -> int:
        if self.ancestor[index] != index:
            self.ancestor[index] = self.find(self.ancestor[index])
        return self.ancestor[index]

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        nodesCount = len(edges)
        uf = UnionFind(nodesCount + 1)
        parent = list(range(nodesCount + 1))
        conflict = -1
        cycle = -1
        for i, (node1, node2) in enumerate(edges):
            if parent[node2] != node2:
                conflict = i
            else:
                parent[node2] = node1
                if uf.find(node1) == uf.find(node2):
                    cycle = i
                else:
                    uf.union(node1, node2)

        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflictEdge = edges[conflict]
            if cycle >= 0:
                return [parent[conflictEdge[1]], conflictEdge[1]]
            else:
                return [conflictEdge[0], conflictEdge[1]]
# @lc code=end

