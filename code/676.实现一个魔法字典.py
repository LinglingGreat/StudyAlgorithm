#
# @lc app=leetcode.cn id=676 lang=python3
#
# [676] 实现一个魔法字典
#
# https://leetcode-cn.com/problems/implement-magic-dictionary/description/
#
# algorithms
# Medium (58.65%)
# Likes:    87
# Dislikes: 0
# Total Accepted:    6.6K
# Total Submissions: 11.3K
# Testcase Example:  '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n' +
  '[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]'
#
# 设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 互不相同 。
# 如果给出一个单词，请判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。
# 
# 实现 MagicDictionary 类：
# 
# 
# MagicDictionary() 初始化对象
# void buildDict(String[] dictionary) 使用字符串数组 dictionary 设定该数据结构，dictionary
# 中的字符串互不相同
# bool search(String searchWord) 给定一个字符串 searchWord ，判定能否只将字符串中 一个
# 字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 true ；否则，返回 false 。
# 
# 
# 
# 
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
# [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
# 输出
# [null, null, false, true, false, false]
# 
# 解释
# MagicDictionary magicDictionary = new MagicDictionary();
# magicDictionary.buildDict(["hello", "leetcode"]);
# magicDictionary.search("hello"); // 返回 False
# magicDictionary.search("hhllo"); // 将第二个 'h' 替换为 'e' 可以匹配 "hello" ，所以返回 True
# magicDictionary.search("hell"); // 返回 False
# magicDictionary.search("leetcoded"); // 返回 False
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# dictionary[i] 仅由小写英文字母组成
# dictionary 中的所有字符串 互不相同
# 1 
# searchWord 仅由小写英文字母组成
# buildDict 仅在 search 之前调用一次
# 最多调用 100 次 search
# 
# 
# 
# 
# 
#

# @lc code=start
'''
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] *26
        self.isEnd = False


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
          node = self
          for w in word:
            index = ord(w)-ord('a')
            if not node.children[index]:
              node.children[index] = MagicDictionary()
            node = node.children[index]
          node.isEnd = True


    def search(self, searchWord: str) -> bool:
      return self.dfs(self, searchWord, 0, 0)
    
    def dfs(self, root, word, i, editt):
      if not root:
        return False
      if root.isEnd and i == len(word) and editt==1:
        return True
      if i < len(word) and editt <= 1:
        found = False
        j = 0
        while j < 26 and (not found):
          next = editt
          if j != ord(word[i]) - ord('a'):
            next = editt + 1
          found = self.dfs(root.children[j], word, i+1, next)
          j += 1
        return found
      return False
'''
'''
class MagicDictionary(object):
    def _genneighbors(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i+1:]

    def buildDict(self, words):
        self.words = set(words)
        self.count = collections.Counter(nei for word in words
                                        for nei in self._genneighbors(word))

    def search(self, word):
        return any(self.count[nei] > 1 or
                   self.count[nei] == 1 and word not in self.words
                   for nei in self._genneighbors(word))
'''
class MagicDictionary(object):
    def __init__(self):
        self.buckets = collections.defaultdict(list)

    def buildDict(self, words):
        for word in words:
            self.buckets[len(word)].append(word)

    def search(self, word):
        return any(sum(a!=b for a,b in zip(word, candidate)) == 1
                   for candidate in self.buckets[len(word)])
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end

