# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-11 12:51:36
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-11 15:47:14
"""
给出 graph 为有 N 个节点（编号为 0, 1, 2, ..., N-1）的无向连通图。 
graph.length = N，且只有节点 i 和 j 连通时，j != i 在列表 graph[i] 中恰好出现一次。
返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。

示例 1：
输入：[[1,2,3],[0],[0],[0]]
输出：4
解释：一个可能的路径为 [1,0,2,0,3]

示例 2：
输入：[[1],[0,2,4],[1,3,4],[2],[1,2]]
输出：4
解释：一个可能的路径为 [0,1,4,2,3]

注意：
1 <= graph.length <= 12
0 <= graph[i].length < graph.length
"""
"""
Approach #1: Breadth First Search [Accepted]
Intuition

A path 'state' can be represented as the subset of nodes visited, plus the current 'head' node. Then, the problem reduces to a shortest path problem among these states, which can be solved with a breadth-first search.

Algorithm

Let's call the set of nodes visited by a path so far the cover, and the current node as the head. We'll store the cover states using set bits: k is in the cover if the kth bit of cover is 1.

For states state = (cover, head), we can perform a breadth-first search on these states. The neighbors are (cover | (1 << child), child) for each child in graph[head].

If at any point we find a state with all set bits in it's cover, because it is a breadth-first search, we know this must represent the shortest path length.
Time Complexity:O(2^N * N)
Space Complexity:O(2^N * N)
x<<n means x*(2^n)
"""
class Solution:
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        # 1 << x是初始状态，后面x位全0(最高位是1),x是当前点
        queue = collections.deque((1 << x, x) for x in range(n))
        dist = collections.defaultdict(lambda: N*N)    # distance
        for x in range(n): dist[1 << x, x] = 0

        while queue:
        	cover, head = queue.popleft()   # 以head作为当前出发点，cover中的1代表该点是否走过
        	d = dist[cover, head]
        	if cover == 2*n-1:return d   # 如果后面n位全是1，说明已经遍历所有点
        	for child in graph[head]:
        		cover2 = cover | (1 << child)   # 把走过child这个信息加到cover中形成cover2
        		if d+1 < dist[cover2, child]:    # 当前点变为child，浏览路径是cover2, 更新距离字典
        			dist[cover2, child] = d+1
        			queue.append((cover2, child))
"""
Approach #2: Dynamic Programming [Accepted]
Intuition

A path 'state' can be represented as the subset of nodes visited, plus the current 'head' node. As in Approach #1, we have a recurrence in states: answer(cover, head) is min(1 + answer(cover | (1<<child), child) for child in graph[head]). Because these states form a DAG (a directed graph with no cycles), we can do dynamic programming.

Algorithm

Let's call the set of nodes visited by a path so far the cover, and the current node as the head. We'll store dist[cover][head] as the length of the shortest path with that cover and head. We'll store the cover states using set bits, and maintain the loop invariant (on cover), that dist[k][...] is correct for k < cover.

For every state (cover, head), the possible next (neighbor) nodes in the path are found in graph[head]. The new cover2 is the old cover plus next.

For each of these, we perform a "relaxation step" (for those familiar with the Bellman-Ford algorithm), where if the new candidate distance for dist[cover2][next] is larger than dist[cover][head] + 1, we'll update it to dist[cover][head] + 1.

Care must be taken to perform the relaxation step multiple times on the same cover if cover = cover2. This is because a minimum state for dist[cover][head] might only be achieved through multiple steps through some path.

Finally, it should be noted that we are using implicitly the fact that when iterating cover = 0 .. (1<<N) - 1, that each new cover cover2 = cover | 1 << x is such that cover2 >= cover. This implies a topological ordering, which means that the recurrence on these states form a DAG.
Time Complexity:O(2^N * N)
Space Complexity:O(2^N * N)
"""
class Solution(object):
    def shortestPathLength(self, graph):
        N = len(graph)
        # 对于每个结点，它对应的访问路径有2^N种
        dist = [[float('inf')] * N for i in range(1 << N)]
        for x in range(N):
            dist[1<<x][x] = 0

        for cover in range(1 << N):
            repeat = True
            while repeat:
                repeat = False
                for head, d in enumerate(dist[cover]):
                    for nei in graph[head]:
                        cover2 = cover | (1 << nei)
                        if d + 1 < dist[cover2][nei]:
                            dist[cover2][nei] = d + 1
                            if cover == cover2:
                                repeat = True

        return min(dist[2**N - 1])

"""
Heapq Solution
"""
class Solution:
    def shortestPathLength(self, graph):
        memo, final, q = set(), (1 << len(graph)) - 1, [(0, i, 1 << i) for i in range(len(graph))]
        while q:
            steps, node, state = heapq.heappop(q)
            if state == final: return steps
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    heapq.heappush(q, (steps + 1, v, state | 1 << v))
                    memo.add((state | 1 << v, v))
"""
BFS Solution
"""
class Solution:
    def shortestPathLength(self, graph):
        memo, final, q, steps = set(), (1 << len(graph)) - 1, [(i, 1 << i) for i in range(len(graph))], 0
        while True:
            new = []
            for node, state in q:
                if state == final: return steps
                for v in graph[node]:
                    if (state | 1 << v, v) not in memo:
                        new.append((v, state | 1 << v))
                        memo.add((state | 1 << v, v))
            q = new
            steps += 1
"""
Deque Solution
"""
class Solution:
    def shortestPathLength(self, graph):
        memo, final, q, steps = set(), (1 << len(graph)) - 1, collections.deque([(i, 0, 1 << i) for i in range(len(graph))]), 0
        while q:
            node, steps, state = q.popleft()
            if state == final: return steps
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    q.append((v, steps + 1, state | 1 << v))
                    memo.add((state | 1 << v, v))

