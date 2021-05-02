#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#
# https://leetcode-cn.com/problems/redundant-connection/description/
#
# algorithms
# Medium (66.26%)
# Likes:    318
# Dislikes: 0
# Total Accepted:    45.6K
# Total Submissions: 68.8K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 在本问题中, 树指的是一个连通且无环的无向图。
# 
# 输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N)
# 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
# 
# 结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。
# 
# 返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u <
# v。
# 
# 示例 1：
# 
# 输入: [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 解释: 给定的无向图为:
# ⁠ 1
# ⁠/ \
# 2 - 3
# 
# 
# 示例 2：
# 
# 输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# 输出: [1,4]
# 解释: 给定的无向图为:
# 5 - 1 - 2
# ⁠   |   |
# ⁠   4 - 3
# 
# 
# 注意:
# 
# 
# 输入的二维数组大小在 3 到 1000。
# 二维数组中的整数在1到N之间，其中N是输入数组的大小。
# 
# 
# 更新(2017-09-26):
# 我们已经重新检查了问题描述及测试用例，明确图是无向 图。对于有向图详见冗余连接II。对于造成任何不便，我们深感歉意。
# 
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodesCount = len(edges)
        parent = list(range(nodesCount + 1))

        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        
        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                return [node1, node2]
        
        return []
        
# @lc code=end

