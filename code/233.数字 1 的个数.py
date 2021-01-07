# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 13:45
# @Author  : LiLing
"""
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
示例:
输入: 13
输出: 6
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
https://leetcode.com/problems/number-of-digit-one/
https://leetcode-cn.com/problems/number-of-digit-one/
"""
class Solution:
    def countDigitOne(self, n: 'int') -> 'int':
        if n <= 0:
            return 0
        q, place, ans = n, 1, 0
        while q > 0:
            digit = q % 10
            q //= 10
            ans += q * place
            if digit == 1:
                ans += n % place + 1
            elif digit > 1:
                ans += place
            place *= 10
        return ans


