# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-11 10:53:24
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-11 12:48:54
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#
# https://leetcode-cn.com/problems/is-graph-bipartite/description/
#
# algorithms
# Medium (50.49%)
# Likes:    238
# Dislikes: 0
# Total Accepted:    32.1K
# Total Submissions: 63.6K
# Testcase Example:  '[[1,2,3],[0,2],[0,1,3],[0,2]]'
#
# 存在一个 无向图 ，图中有 n 个节点。其中每个节点都有一个介于 0 到 n - 1 之间的唯一编号。给你一个二维数组 graph ，其中
# graph[u] 是一个节点数组，由节点 u 的邻接节点组成。形式上，对于 graph[u] 中的每个 v ，都存在一条位于节点 u 和节点 v
# 之间的无向边。该无向图同时具有以下属性：
# 
# 不存在自环（graph[u] 不包含 u）。
# 不存在平行边（graph[u] 不包含重复值）。
# 如果 v 在 graph[u] 内，那么 u 也应该在 graph[v] 内（该图是无向图）
# 这个图可能不是连通图，也就是说两个节点 u 和 v 之间可能不存在一条连通彼此的路径。
# 
# 
# 二分图 定义：如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，并使图中的每一条边的两个节点一个来自 A 集合，一个来自 B
# 集合，就将这个图称为 二分图 。
# 
# 如果图是二分图，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# 输出：false
# 解释：不能将节点分割成两个独立的子集，以使每条边都连通一个子集中的一个节点与另一个子集中的一个节点。
# 
# 示例 2：
# 
# 
# 输入：graph = [[1,3],[0,2],[1,3],[0,2]]
# 输出：true
# 解释：可以将节点分成两组: {0, 2} 和 {1, 3} 。
# 
# 
# 
# 提示：
# 
# 
# graph.length == n
# 1 
# 0 
# 0 
# graph[u] 不会包含 u
# graph[u] 的所有值 互不相同
# 如果 graph[u] 包含 v，那么 graph[v] 也会包含 u
"""
给定一个无向图graph，当这个图为二分图时返回true。
如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边： 
graph[i] 中不存在i，并且graph[i]中没有重复的值。


示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true
解释: 
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。

示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false
解释: 
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。
注意:

graph 的长度范围为 [1, 100]。
graph[i] 中的元素的范围为 [0, graph.length - 1]。
graph[i] 不会包含 i 或者有重复的值。
图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。
"""
class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def validColor(graph, colors, color, node):
            if colors[node] != -1:
                return colors[node] == color
            colors[node] =color
            for j in graph[node]:
                if not validColor(graph, colors, 1 - color, j):
                    return False
            return True
            
        n = len(graph)
        colors = [-1]*n
        for i in range(n):
            if colors[i]==-1 and not validColor(graph, colors, 0, i):
                return False

        return True

class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        WHITE, BLACK = range(2)

        if not graph:
            return True

        def dfs(node, color=WHITE):
            if node in colormap:
                return colormap[node] == color
            # assign color to node
            colormap[node] = color
            # toggle color
            color = BLACK if color == WHITE else WHITE
            # check following nodes
            return all(dfs(neighbor, color) for neighbor in graph[node])

        colormap = {}
        # check graph nodes
        return all(dfs(node) for node in range(len(graph)) if node not in colormap)

s=Solution()
print(s.isBipartite([[1],[0,3],[3],[1,2]]))