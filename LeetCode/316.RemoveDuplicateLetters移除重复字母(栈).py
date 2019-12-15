# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-10 10:44:06
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-10 12:45:30
"""
给定一个仅包含小写字母的字符串，去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1:

输入: "bcabc"
输出: "abc"
示例 2:

输入: "cbacdcbc"
输出: "acdb"
"""
class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [] # max-length is 26
        last_pos = {c: s.rindex(c) for c in set(s)}
        for i, c in enumerate(s):
            if c not in stack:
            	# 如果stack的最后一个字母比这个字母大，且最后一个字母最大index大于这个字母的index，stack的最后一个字母不该取
                while stack and stack[-1] > c and last_pos[stack[-1]] > i:
                    stack.pop()
                stack.append(c)
        return ''.join(stack)

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''        

        # 记录每个字母出现的次数
        cnt = dict().fromkeys(set(list(s)),0)
        pos = 0   # 记录最小的字母所在的位置
        n = len(s)
        for i in s:
        	cnt[i] += 1
        for i in range(s):
        	if s[i]<s[pos]:
        		pos = i
        	cnt[s[i]] -= 1
        	# 当遍历到其中某个字母的最后一个时，结束循环
        	if cnt[s[i]] == 0:
        		break
        return s[pos]+self.removeDuplicateLetters(s[pos+1:].replace(s[pos],""))
