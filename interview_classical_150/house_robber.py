from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        maxNum = 0
        for i in range(len(nums)):
            if i >= 2:
                dp[i] = max(dp[i - 1], (dp[i - 2] + nums[i]))
            elif i == 1:
                dp[i] = max(dp[i - 1], nums[i])
            elif i == 0:
                dp[i] = nums[i]
            maxNum = max(maxNum, dp[i])
        return maxNum
