from typing import List


# 利用数值和下标映射关系，这个思想可以借鉴


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] <= len(nums) and nums[i] > 0 and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


print(Solution().firstMissingPositive([3, 4, 1, -1]))
