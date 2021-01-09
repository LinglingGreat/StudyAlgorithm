#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = []
        ans = []
        # 初始化
        # 将 temp 中 [0, k - 1] 每个位置 i 设置为 i + 1，即 [0, k - 1] 存 [1, k]
        # 末尾加一位 n + 1 作为哨兵
        for i in range(1, k+1):
            temp.append(i)
        temp.append(n+1)
        
        j = 0
        while j < k:
            ans.append(copy.deepcopy(temp[0:k]))
            j = 0
            # 寻找第一个 temp[j] + 1 != temp[j + 1] 的位置 t
            # 我们需要把 [0, t - 1] 区间内的每个位置重置成 [1, t]
            while j < k and temp[j] + 1 == temp[j + 1]:
                temp[j] = j + 1
                j += 1
            # j 是第一个 temp[j] + 1 != temp[j + 1] 的位置
            temp[j] += 1
        return ans

# @lc code=end

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(cur, n, k):
            # 剪枝：temp 长度加上区间 [cur, n] 的长度小于 k，不可能构造出长度为 k 的 temp
            if len(temp) + (n - cur + 1) < k:
                return
            # 记录合法的答案
            if len(temp) == k:
                res.append(copy.deepcopy(temp))
                return
            # 考虑选择当前位置
            temp.append(cur)
            backtrack(cur + 1, n, k)
            temp.pop()
            # 考虑不选择当前位置
            backtrack(cur + 1, n, k)

        res = []
        temp = []
        backtrack(1, n, k)
        return res