from typing import List


# 时间复杂度O(m*n)，空间复杂度O(1)，其中m和n分别是矩阵的行数和列数，模拟解法，维护四个边界，每次遍历一个边界后更新边界，直到输出的元素数量等于矩阵元素总数
# 实际上没必要通过ij来一个个遍历，可以用for range来遍历边界上的元素，时间复杂度仍然是O(m*n)，空间复杂度O(1)
# 也没必要维护方向变量，由于是一个循环，所以可以直接按照右、下、左、上的顺序来遍历边界，时间复杂度仍然是O(m*n)，空间复杂度O(1)
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


# 更优算法
class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1
        ans = []
        while top <= bottom and left <= right:
            # top
            if top <= bottom and left <= right:
                for j in range(left, right + 1):
                    ans.append(matrix[top][j])
            top += 1

            # right
            if top <= bottom and left <= right:
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
            right -= 1

            # bottom
            if top <= bottom and left <= right:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])
            bottom -= 1

            # left
            if top <= bottom and left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
            left += 1
        return ans


print(
    Solution().spiralOrder(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20],
            [21, 22, 23, 24],
        ]
    )
)
