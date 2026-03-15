from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maxNum = 0
        while i < j:
            maxNum = max(maxNum, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxNum


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
