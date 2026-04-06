from typing import List


# 利用到set的机制
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = sum(nums)
        longestStreak = 0
        for num in numSet:
            # 判断是否是streak的头
            if num - 1 not in numSet:
                currentNum = num
                currentStreak = 1
                while currentNum + 1 in numSet:
                    currentNum = currentNum + 1
                    currentStreak += 1
                longestStreak = max(longestStreak, currentStreak)
        return longestStreak
