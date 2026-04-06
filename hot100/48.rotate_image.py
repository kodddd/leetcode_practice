from typing import List


# 划分为四个区域，其实就把一个区域内的点以及三个不同区域对应点的数值更新即可
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                (
                    matrix[i][j],
                    matrix[n - j - 1][i],
                    matrix[n - i - 1][n - j - 1],
                    matrix[j][n - i - 1],
                ) = (
                    matrix[n - j - 1][i],
                    matrix[n - i - 1][n - j - 1],
                    matrix[j][n - i - 1],
                    matrix[i][j],
                )
