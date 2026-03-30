class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 100000
        maxProfit = 0

        for i in range(len(prices)):
            maxprofit = 0
            if minPrice > prices[i]:
                minPrice = prices[i]
            elif maxProfit < prices[i] - minPrice:
                maxProfit = prices[i] - minPrice

        return maxProfit