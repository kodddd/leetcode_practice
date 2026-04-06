from typing import List


# 利用了右上角点的特质：所在行均小于等于该点，所在列均大于等于该点
# 这样就可以删除行或列
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = 0, len(matrix[0]) - 1
        while True:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                x += 1
            elif matrix[x][y] > target:
                y -= 1
            if x >= len(matrix) or y < 0:
                return False


print(
    Solution().searchMatrix(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        20,
    )
)
