from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        minCount = float("inf")
        for i in range(1, amount + 1):
            currentMin = float("inf")
            for coin in coins:
                if i - coin >= 0:
                    currentMin = min(currentMin, dp[i - coin] + 1)
            dp[i] = currentMin
        print(dp)
        return dp[amount] if dp[amount] != float("inf") else -1


print(Solution().coinChange([1], 0))
