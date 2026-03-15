from typing import List


# 时间复杂度O(n^2)，空间复杂度O(n)，其中n为nums长度，暴力解法，时间复杂度较高
# 事实上这比暴力解法还要暴力，暴力解法是每个起点向后累加，直到满足条件，时间复杂度O(n^2)，空间复杂度O(1)
class SolutionBad:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        accumulate = [nums[0]]
        minNum = float("inf")
        for i in range(1, len(nums)):
            accumulate.append(0)
            for j in range(0, len(accumulate)):
                accumulate[j] += nums[i]
                if accumulate[j] >= target and (i - j + 1) < minNum:
                    minNum = i - j + 1
        if minNum == float("inf"):
            return 0
        else:
            return minNum


# 时间复杂度O(n)，空间复杂度O(1)，滑动窗口解法，维护一个窗口，窗口内元素和满足条件时尝试缩小窗口，直到不满足条件，再扩大窗口，如此循环，直到窗口右边界到达数组末尾
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        sumNum = nums[0]
        minLength = float("inf")
        while end < len(nums) and start <= end:
            if sumNum >= target:
                minLength = min(minLength, (end - start + 1))
                sumNum -= nums[start]
                start += 1
            else:
                end += 1
                if end >= len(nums):
                    break
                sumNum += nums[end]
        if minLength == float("inf"):
            return 0
        else:
            return minLength


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
