#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nrows = len(board)
        ncols = len(board[0])
        # 每一行
        for i in range(nrows):
            thisrow = board[i]
            thisrow = [i for i in thisrow if i !='.']
            if len(thisrow) != len(set(thisrow)):
                return False
        # 每一列
        for j in range(ncols):
            thiscol = [board[i][j] for i in range(nrows) if board[i][j]!='.']
            if len(thiscol) != len(set(thiscol)):
                return False
        # 每个九宫格
        for i in range(0, nrows,3):
            for j in range(0, ncols, 3):
                thissquare = [board[i+p][j+q] for p in range(3) for q in range(3) if board[i+p][j+q]!='.']
                if len(thissquare) != len(set(thissquare)):
                    return False
        return True
# @lc code=end

