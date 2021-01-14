#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (43.91%)
# Likes:    738
# Dislikes: 0
# Total Accepted:    131.6K
# Total Submissions: 299.5K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
# 
# 
# 
# 提示：
# 
# 
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# 
# 
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, cur):
            if board[i][j] != word[cur]:
                return False
            if cur == len(word) - 1:
                return True
            result = False
            used_rc.add((i, j))
            back_list = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for ii, jj in back_list:
                if 0<=ii<nrows and 0<=jj<ncols:
                    if (ii, jj) not in used_rc:
                        if dfs(ii, jj, cur+1):
                            result = True
                            break
            used_rc.remove((i, j))
            return result
        nrows = len(board)
        ncols = len(board[0])
        used_rc = set()
        for i in range(nrows):
            for j in range(ncols):
                if dfs(i, j, 0):
                    return True
        return False
# @lc code=end

