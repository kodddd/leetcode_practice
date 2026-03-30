from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        if nr == 0 or nc == 0:
            return 0
        islandNum = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    islandNum += 1
                    self.dfs(grid, i, j)
        return islandNum

    def dfs(self, grid: List[List[str]], r, c):
        grid[r][c] = "0"
        nr = len(grid)
        nc = len(grid[0])
        for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= i < nr and 0 <= j < nc and grid[i][j] == "1":
                self.dfs(grid, i, j)


print(
    Solution().numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
