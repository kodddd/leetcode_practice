from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowSet = set()
            colSet = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rowSet:
                        return False
                    else:
                        rowSet.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in colSet:
                        return False
                    else:
                        colSet.add(board[j][i])
        # 检查每个 3x3 的子块
        # 3x3 的子块的起始位置为 (i*3, j*3)，其中 i 和 j 分别为 0、1、2
        for i in range(3):
            for j in range(3):
                blockSet = set()
                for k in range(3):
                    for l in range(3):
                        if board[i * 3 + k][j * 3 + l] != ".":
                            if board[i * 3 + k][j * 3 + l] in blockSet:
                                return False
                            else:
                                blockSet.add(board[i * 3 + k][j * 3 + l])
        return True
