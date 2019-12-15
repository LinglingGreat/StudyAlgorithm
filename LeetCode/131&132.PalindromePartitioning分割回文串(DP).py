# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-19 09:25:30
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-19 10:51:08
"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution1:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        fin = []
        def pat(st, curr):
            if len(st) == 0:
                fin.append(list(curr))
                return
            for i in range(len(st)):
                now = st[:i+1]
                if now == now[::-1]:
                    curr.append(now)
                    pat(st[i+1:], curr)
                    curr.pop()
        pat(s, [])
        return fin


class Solution:
    def ishuiwen(self, s):
        if s[:] == s[::-1]:
            return True 
        return False
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        n = len(s)
        #s = list(s)
        if n == 0:
            return [[]]
        if n == 1:
            return [[s[0]]]
        for i in range(n):
            if self.ishuiwen(s[:i+1]):
                for j in self.partition(s[i+1:]):
                    res.append([s[:i+1]]+list(j))
        return res

s = Solution()
print(s.partition("aab"))
"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
"""
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cut = [i-1 for i in range(n+1)]
        for i in range(n):
        	# odd length
        	j = 0
        	while i-j >= 0 and i+j <n and s[i-j]==s[i+j]:
        		cut[i+j+1] = min(cut[i+j+1], 1+cut[i-j])
        		j += 1
        	# even length
        	j = 1
        	while i-j+1 >=0 and i+j <n and s[i-j+1]==s[i+j]:
        		cut[i+j+1] = min(cut[i+j+1], 1+cut[i-j+1])
        		j += 1
        return cut[n]

    def minCut2(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = list(range(-1, n))
        for i in range(n):
            for [l, r] in [[i, i], [i, i + 1]]:
                while l >= 0 and r < n and s[l] == s[r]:
                    res[r + 1] = min(res[r + 1], res[l] + 1)
                    l -= 1
                    r += 1
        return res[n]

s = Solution()
print(s.minCut("aab"))