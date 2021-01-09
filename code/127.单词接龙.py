#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            """字典wordId, key是单词，value是单词对应的id"""
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1
        
        def addEdge(word: str):
            """字典edge,key是wordid,value是和word有边(只差一个字母)的虚拟单词"""
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        # 给列表里的每个单词及其虚拟单词以及beginWord创建边
        for word in wordList:
            addEdge(word)
        
        addEdge(beginWord)
        if endWord not in wordId:
            return 0
        
        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0

        que = collections.deque([beginId])   # 队列，先进先出
        while que:
            x = que.popleft()  # 当前单词
            if x == endId:   # 已经到达终点，因为有虚拟单词，所以除以2；因为beginWord没算在内，所以+1
                return dis[endId] // 2 + 1
            for it in edge[x]:  # 遍历和当前单词有边的虚拟单词
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1  # 走到这个单词需要几步
                    que.append(it)   # 遍历所有的可能性，因为是队列所以是广度优先搜索
        
        return 0
        
# @lc code=end

