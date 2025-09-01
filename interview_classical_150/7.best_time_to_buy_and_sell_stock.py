# solution: 一次遍历，记录当前最低买入价格和最大利润
# 有点类似于动态规划
# 每次遍历到一个新的价格时，计算如果在这个价格卖出能获得的最大利润，并和当前最大利润比较
# 如果当前价格低于之前记录的最低价格，则更新最低价格
# 时间复杂度O(n), 空间复杂度O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        lowestPrice = prices[0]
        for price in prices:
            if price > lowestPrice:
                if price - lowestPrice > maxProfit:
                    maxProfit = price - lowestPrice
            else:
                if price < lowestPrice:
                    lowestPrice = price
        return maxProfit
