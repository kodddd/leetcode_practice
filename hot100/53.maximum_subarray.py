from typing import List


# 参考了560的用前缀和相减 计算得出连续子串的和的思想
# 为了不需要遍历过去的前缀和，用一个值来存储过去最小的前缀和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_min = 0
        max_sum = -float("inf")
        prev = 0
        for i in range(len(nums)):
            prev += nums[i]
            max_sum = max(max_sum, prev - prev_min)
            prev_min = min(prev_min, prev)
        return max_sum


print(Solution().maxSubArray([5, 4, -1, 7, 8]))
