#
# @lc app=leetcode.cn id=854 lang=python3
#
# [854] 相似度为 K 的字符串
#
# https://leetcode-cn.com/problems/k-similar-strings/description/
#
# algorithms
# Hard (34.32%)
# Likes:    85
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 10K
# Testcase Example:  '"ab"\n"ba"'
#
# 如果可以通过将 A 中的两个小写字母精确地交换位置 K 次得到与 B 相等的字符串，我们称字符串 A 和 B 的相似度为 K（K 为非负整数）。
# 
# 给定两个字母异位词 A 和 B ，返回 A 和 B 的相似度 K 的最小值。
# 
# 
# 
# 示例 1：
# 
# 输入：A = "ab", B = "ba"
# 输出：1
# 
# 
# 示例 2：
# 
# 输入：A = "abc", B = "bca"
# 输出：2
# 
# 
# 示例 3：
# 
# 输入：A = "abac", B = "baca"
# 输出：2
# 
# 
# 示例 4：
# 
# 输入：A = "aabc", B = "abca"
# 输出：2
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length == B.length <= 20
# A 和 B 只包含集合 {'a', 'b', 'c', 'd', 'e', 'f'} 中的小写字母。
# 
# 
#

# @lc code=start
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def neighbors(S):
            for i, c in enumerate(S):
                if c != B[i]:
                    break

            T = list(S)
            for j in range(i+1, len(S)):
                if S[j] == B[i]:
                    T[i], T[j] = T[j], T[i]
                    yield "".join(T)
                    T[j], T[i] = T[i], T[j]

        queue = collections.deque([A])
        seen = {A: 0}
        while queue:
            S = queue.popleft()
            if S == B: return seen[S]
            for T in neighbors(S):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)
        
# @lc code=end

