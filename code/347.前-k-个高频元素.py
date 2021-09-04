#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i,0) + 1
        sort_dict = sorted(nums_dict.items(),key=lambda x:x[1],reverse=True)
        return [i[0] for i in sort_dict][:k]
        '''
        
        count = collections.Counter(nums)
        # heap = [(val, key) for key, val in count.items()]
        # return [item[1] for item in heapq.nlargest(k, heap)]

        heap = []
        for key, val in count.items():
            if len(heap) >= k:
                if val > heap[0][0]:
                    heapq.heapreplace(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
        return [item[1] for item in heap]


# @lc code=end

