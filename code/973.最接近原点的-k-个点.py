#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#

# @lc code=start
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # Python的优先队列为小根堆，所以这里计算相反数
        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:K])]
        heapq.heapify(q)

        n = len(points)
        for i in range(K, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            # 如果当前点的距离平方比堆顶的点的距离平方要小，就把堆顶的点弹出，再插入当前的点。
            heapq.heappushpop(q, (dist, i))
        
        ans = [points[identity] for (_, identity) in q]
        return ans
        


        
# @lc code=end

