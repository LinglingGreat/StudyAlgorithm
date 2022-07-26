#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的K对数字
#
# https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (42.64%)
# Likes:    212
# Dislikes: 0
# Total Accepted:    19.1K
# Total Submissions: 45K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# 给定两个以升序排列的整数数组 nums1 和 nums2 , 以及一个整数 k 。
# 
# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。
# 
# 请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
# ⁠    [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 
# 
# 示例 2:
# 
# 
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# 
# 
# 示例 3:
# 
# 
# 输入: nums1 = [1,2], nums2 = [3], k = 3 
# 输出: [1,3],[2,3]
# 解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 
# -10^9 
# nums1, nums2 均为升序排列
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        heap = []
        # 官方实现的是最小堆，若想实现最大堆，仅需要将每个元素的 键 值添负号。
        for a in nums1:
            for b in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-(a + b), [a, b]))
                elif -(a + b) > heap[0][0]:
                    heapq.heappushpop(heap, (-(a + b), [a, b]))
                else:
                    break
        ans = []
        while heap:
            t = heapq.heappop(heap, )
            ans.append(t[1])
        ans.reverse()
        return ans
        # return [heapq.heappop(heap)[1] for _ in range(k) if heap]
        '''
        heap = []
        # 最小堆，选出候选中最小的数对
        if len(nums2) > 0:
            for i, a in enumerate(nums1[:k]):
                heapq.heappush(heap, (nums1[i]+nums2[0],i, 0))
        result = []
        while k > 0 and heap:
            t = heapq.heappop(heap)
            result.append([nums1[t[1]], nums2[t[2]]])
            k -= 1
            if t[2] < len(nums2)-1:
                heapq.heappush(heap, (nums1[t[1]]+nums2[t[2]+1],t[1], t[2]+1))
        return result


# @lc code=end

