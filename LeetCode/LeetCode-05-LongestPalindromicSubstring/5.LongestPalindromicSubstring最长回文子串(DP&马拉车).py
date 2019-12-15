# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-10-02 22:15:06
# @Last Modified by:   Liling
# @Last Modified time: 2018-10-02 23:45:18
"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""
"""
动态规划
时间复杂度O(n^2),空间复杂度O(n^2)
"""
class Solution(object):
    def __init__(self):
        self.maxlen = 0
        self.lo = 0
    def extendPalindrome(self, s, j, k):
        while j>=0 and k<len(s) and s[j]==s[k]:
            j -= 1
            k += 1
        if self.maxlen < k-j-1:
            self.lo = j+1
            self.maxlen = k-j-1
    def longestPalindrome(self, s):
        n = len(s)
        if n<2:
            return s
        for i in range(n-1):
            self.extendPalindrome(s,i,i)
            self.extendPalindrome(s,i,i+1)
        return s[self.lo:self.lo+self.maxlen]

class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        if n<2:
            return s
        min_start = 0
        max_len = 1
        for i in range(n):
        	if n-i<=max_len/2:
        		break
        	j=i
        	k=i
        	while k<n-1 and s[k+1]==s[k]:   # 跳过重复字符
        		k += 1
        	i = k+1
        	while k<n-1 and j>0 and s[k+1]==s[j-1]:
        		k += 1
        		j -= 1
        	new_len = k-j+1
        	if new_len>max_len:
        		min_start = j
        		max_len = new_len
        return s[min_start:min_start+max_len]

"""
马拉车算法
https://mp.weixin.qq.com/s/9Of0Qh8SWmySKJBG76vJrQ
"""
# 使用manacher算法进行字长回文串的判断
class Solution(object):
    def longestPalindrome(self, s):
        if s == None or len(s) <= 0:
            return s
        newS = '#' + '#'.join(s) + '#'

        length, center, rightMost, maxCenter, maxLen, i = len(newS), 0, 0, 0, 0, 0
        pArr = [0] * length
        for i in range(length):
            pArr[i] = 1 if rightMost < i else min(rightMost-i, pArr[(center << 1) - i])
            while i + pArr[i] < length and i - pArr[i] > -1 and newS[i + pArr[i]] == newS[i - pArr[i]]:
                pArr[i] += 1
            if i + pArr[i] > rightMost:
                center = i
                rightMost = i + pArr[i]
                if pArr[i] > maxLen:
                    maxLen = pArr[i]
                    maxCenter = i
        start = (maxCenter - maxLen + 1) >> 1
        return s[start: start + maxLen - 1]

    def manacher(s):
        # 预处理,新字符串的回文特性和原串等价
        s = '#' + '#'.join(s) + '#'

        RL = [0] * len(s)    # 记录以该字符为中心的回文长度的一半(向下取整)
        MaxRight = 0   # 已知回文串的右边界
        pos = 0     # 记录右边界对应的回文串中心
        MaxLen = 0
        for i in range(len(s)):
        	# 如果在右边界的覆盖之内
            if i < MaxRight:
            	# 等于相对pos的对称位置的回文长度，即RL[i]=RL[2*pos-i]
            	# 但是如果超过了右边界，即RL[i]+i>maxRight时，进行调整
                RL[i] = min(RL[2 * pos - i], MaxRight - i)
            else:
                RL[i] = 1
            # 尝试扩展，注意处理边界
            while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
                RL[i] += 1
            # 更新MaxRight,pos
            if RL[i] + i - 1 > MaxRight:
                MaxRight = RL[i] + i - 1
                pos = i
            # 更新最长回文串的长度
            MaxLen = max(MaxLen, RL[i])
        return MaxLen - 1

test = 'aaaba'
s = Solution()
print(s.longestPalindrome(test))