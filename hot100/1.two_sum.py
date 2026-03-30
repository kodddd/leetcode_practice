from typing import List


# 灵活运用数据结构
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            else:
                numToIndex[nums[i]] = i
        return [1]


print(Solution().twoSum([3, 2, 4], 6))
