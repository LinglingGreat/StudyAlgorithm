#
# @lc app=leetcode.cn id=820 lang=python3
#
# [820] 单词的压缩编码
#
# https://leetcode-cn.com/problems/short-encoding-of-words/description/
#
# algorithms
# Medium (50.56%)
# Likes:    243
# Dislikes: 0
# Total Accepted:    53.8K
# Total Submissions: 106.2K
# Testcase Example:  '["time","me","bell"]'
#
# 单词数组 words 的 有效编码 由任意助记字符串 s 和下标数组 indices 组成，且满足：
# 
# 
# words.length == indices.length
# 助记字符串 s 以 '#' 字符结尾
# 对于每个下标 indices[i] ，s 的一个从 indices[i] 开始、到下一个 '#' 字符结束（但不包括 '#'）的 子字符串 恰好与
# words[i] 相等
# 
# 
# 给你一个单词数组 words ，返回成功对 words 进行编码的最小助记字符串 s 的长度 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：words = ["time", "me", "bell"]
# 输出：10
# 解释：一组有效编码为 s = "time#bell#" 和 indices = [0, 2, 5] 。
# words[0] = "time" ，s 开始于 indices[0] = 0 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
# words[1] = "me" ，s 开始于 indices[1] = 2 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
# words[2] = "bell" ，s 开始于 indices[2] = 5 到下一个 '#' 结束的子字符串，如加粗部分所示
# "time#bell#"
# 
# 
# 示例 2：
# 
# 
# 输入：words = ["t"]
# 输出：2
# 解释：一组有效编码为 s = "t#" 和 indices = [0] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# words[i] 仅由小写字母组成
# 
# 
#

# @lc code=start
class Trie:
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.cnt = 0        #经过这个结点的单词个数

    def insert(self, word: str) -> None:
        root = self
        for c in word[::-1]:
            ID = ord(c) - ord('a')
            if root.child[ID] == None:
                root.child[ID] = Trie()
                root.cnt += 1
            root = root.child[ID]
        root.cnt += 1

    def search(self, word: str) -> int:
        root = self
        for c in word[::-1]:
            ID = ord(c) - ord('a')
            root = root.child[ID]
        return root.cnt 


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        T = Trie()

        words_us = set(words)

        for word in words_us:
            T.insert(word)
        
        res = 0
        for word in words_us:
            if T.search(word) == 1:       #是Trie树里一条路径最长的那个单词
                res += len(word) + 1
        return res
# @lc code=end

