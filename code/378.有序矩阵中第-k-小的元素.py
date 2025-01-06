#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#
# https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (63.85%)
# Likes:    1098
# Dislikes: 0
# Total Accepted:    143.3K
# Total Submissions: 223.6K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# 给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。
# 
# 你必须找到一个内存复杂度优于 O(n^2) 的解决方案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# 输出：13
# 解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[-5]], k = 1
# 输出：-5
# 
# 
# 
# 
# 提示：
# 
# 
# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 300
# -10^9 <= matrix[i][j] <= 10^9
# 题目数据 保证 matrix 中的所有行和列都按 非递减顺序 排列
# 1 <= k <= n^2
# 
# 
# 
# 
# 进阶：
# 
# 
# 你能否用一个恒定的内存(即 O(1) 内存复杂度)来解决这个问题?
# 你能在 O(n) 的时间复杂度下解决这个问题吗?这个方法对于面试来说可能太超前了，但是你会发现阅读这篇文章（ this paper ）很有趣。
# 
# 
#

# @lc code=start
# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译。
# 本代码的正确性已通过力扣验证，如有疑问，可以对照 java 代码查看。

from queue import PriorityQueue

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 存储二元组 (matrix[i][j], i, j)
        # i, j 记录当前元素的索引位置，用于生成下一个节点
        pq = PriorityQueue()

        # 初始化优先级队列，把每一行的第一个元素装进去
        for i in range(len(matrix)):
            pq.put((matrix[i][0], i, 0))

        res = -1
        # 执行合并多个有序链表的逻辑，找到第 k 小的元素
        while not pq.empty() and k > 0:
            cur = pq.get()
            # 按照元素大小升序排序
            res = cur[0]
            k -= 1
            # 链表中的下一个节点加入优先级队列
            i, j = cur[1], cur[2]
            if j + 1 < len(matrix[i]):
                pq.put((matrix[i][j + 1], i, j + 1))
        return res
        
# @lc code=end

