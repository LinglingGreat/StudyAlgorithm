# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-10-07 17:10:00
# @Last Modified by:   Liling
# @Last Modified time: 2018-10-07 17:50:51
"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""
"""
解法一
算法及复杂度(3 ms)
题目要求使用回溯法.回溯法的过程十分简单，就是按照要求的次序进行搜索（通常是深度优先搜索）
得到一个答案或者无法继续搜索时则进行回溯，之后继续搜索，直到穷尽所有可能的要求的次序.
本题采用递归的方法，搜索过程中记录本次数字代表的字母次序，过程采用深度优先搜索的方法，每层进行一个数字代表的不同字母的尝试。
先尝试一个字母，然后递归这个字母被选定情况下的所有搜索，之后把这个字母换成这个数字代表的下一个字母，直到搜索完这个字母代表的所有字母，然后返回上一层.
时间复杂度: 最差为O(4^n). 算法的过程实质上等价于枚举，最坏的情况下每个数字代表4个字母，一共有n个数字.

举个例子

// 输入字符串, n = 2digits = "23"
// 其中2映射为字母"abc", 3映射为字母"def"，初始状态如下temp = "", result = []
// temp长度不等于n，则abc分别进入temp，在temp中追加2，进入下一层temp = "a", result = []
// temp长度不等于n，则def分别进入temp，在temp中追加d，进入下一层temp = "ad", result = []
// temp长度等于n = 2，在result中追加temp，之后返回上一层temp = "ad", result = ["ad"]
// temp删除最后一个元素，进行下一次循环，在temp中追加e，进入下一层temp = "ae",  result = ["ad"]
// temp长度等于n = 2，在result中追加temp，之后返回上一层temp = "ae", result = ["ad", "ae"]
// 之后过程类似，直到搜索完所有的顺序，最后返回result
"""
class Solution:
    def work(self, digits, temp, result, dic):
        lent = len(temp)
        lend = len(digits)
        if lent == lend:
            result.append(temp)
            return result
        for i in range(len(dic[digits[lent]])):
            temp += dic[digits[lent]][i]
            result = self.work(digits, temp, result, dic)
            temp = temp[:-1]
        return result

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        result = []
        if len(digits) == 0:
            return result

        temp = ""
        result = self.work(digits, temp, result, dic)
        return result

"""
解法二
"""
class Solution1:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        if len(digits) == 0:
            return ans
        mapping = ["0","1","abc","def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans.append("")
        while len(ans[0])!=len(digits):
            t = ans.pop(0)
            x = int(digits[len(t)])
            for s in mapping[x]:
                ans.append(t+s)
        return ans

s=Solution1()
print(s.letterCombinations("23"))