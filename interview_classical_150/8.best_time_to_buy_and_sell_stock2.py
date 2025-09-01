# solution: 动态规划
# 当前的最优情况可分为持有股票和不持有股票两种情况
# dp[i][0]表示第i天结束时不持有股票的最大利润
# dp[i][1]表示第i天结束时持有股票的最大利润
# 1.满足子问题独立：第i天的最优收益只和第i-1天的最优收益有关
# 2.决策过程可拆分
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[len(prices) - 1][0]
