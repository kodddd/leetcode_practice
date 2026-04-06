from typing import List


# 花空间o(m+n)，优化算法是用第一行/列作为这个算法中的ml和nl，之前还纠结于可能这会导致原本的数据更改了
# 但转念一想，转化为指示数组，就等于提前把第一行和第一列给setzero了，不会让最终结果有错
# 而它们可能因为包含0而完全置0（这个判断需要在转换为指示数组之前），那么就先遍历一遍判断是否全为0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        mL = [False] * m
        nL = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    mL[i] = True
                    nL[j] = True
        print(mL, nL)
        for i in range(m):
            for j in range(n):
                if mL[i] == True or nL[j] == True:
                    matrix[i][j] = 0


print(Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
