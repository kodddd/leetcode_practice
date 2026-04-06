from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        startRow, endRow = -1, len(matrix)
        startCol, endCol = -1, len(matrix[0])
        output = []
        i, j = 0, 0
        direction = 0  # 0右，1下，2左，3上
        while len(output) < len(matrix) * len(matrix[0]):
            output.append(matrix[i][j])
            if direction == 0:  # to right
                if j + 1 == endCol:
                    direction = 1
                    startRow += 1
                    i += 1
                else:
                    j += 1
            elif direction == 1:
                if i + 1 == endRow:
                    direction = 2
                    endCol -= 1
                    j -= 1
                else:
                    i += 1
            elif direction == 2:
                if j - 1 == startCol:
                    direction = 3
                    endRow -= 1
                    i -= 1
                else:
                    j -= 1
            elif direction == 3:
                if i - 1 == startRow:
                    direction = 0
                    startCol += 1
                    j += 1
                else:
                    i -= 1
        return output
