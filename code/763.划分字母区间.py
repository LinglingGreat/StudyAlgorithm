#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(S):
            last[ord(ch) - ord("a")] = i
        partition = list()
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1
        
        return partition

# @lc code=end

