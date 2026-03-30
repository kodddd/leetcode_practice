from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 左右指针
        i, j = 0, len(height) - 1
        maxArea = 0
        while i < j:
            maxArea = max((j - i) * min(height[i], height[j]), maxArea)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
